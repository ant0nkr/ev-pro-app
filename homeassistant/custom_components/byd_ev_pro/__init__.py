"""BYD EV Pro integration — receives vehicle telemetry via webhook."""

from __future__ import annotations

import hashlib
import hmac
import logging
from typing import Any

from homeassistant.components.webhook import (
    async_register as webhook_register,
    async_unregister as webhook_unregister,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from aiohttp.web import Request, Response, json_response

from .const import DOMAIN, MANUFACTURER

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR, Platform.DEVICE_TRACKER]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up BYD EV Pro from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "sensors": {},
        "location": {},
        "device_info": {},
    }

    # Register webhook.
    webhook_id = entry.data["webhook_id"]
    webhook_register(
        hass,
        DOMAIN,
        "BYD EV Pro",
        webhook_id,
        _handle_webhook,
    )
    _LOGGER.info("Registered webhook %s for %s", webhook_id, entry.title)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    webhook_unregister(hass, entry.data["webhook_id"])
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok


async def _handle_webhook(
    hass: HomeAssistant, webhook_id: str, request: Request
) -> Response:
    """Handle incoming webhook from the car."""
    # Find the config entry for this webhook.
    entry = _find_entry_by_webhook(hass, webhook_id)
    if entry is None:
        _LOGGER.warning("Received webhook for unknown ID: %s", webhook_id)
        return json_response({"error": "unknown_webhook"}, status=404)

    try:
        raw_body = await request.read()
        import json as _json
        payload: dict[str, Any] = _json.loads(raw_body)
    except (ValueError, KeyError):
        return json_response({"error": "invalid_json"}, status=400)

    # HMAC verification — reject entirely if secret is configured but signature is wrong.
    options = entry.options or {}
    webhook_secret = options.get("webhook_secret", "")
    if webhook_secret:
        expected = hmac.new(
            webhook_secret.encode(), raw_body, hashlib.sha256
        ).hexdigest()
        received = request.headers.get("X-Webhook-Signature", "")
        if not hmac.compare_digest(expected, received):
            _LOGGER.warning("Invalid HMAC signature for webhook %s", webhook_id)
            return json_response({"error": "invalid_signature"}, status=403)

    data = hass.data[DOMAIN][entry.entry_id]
    changed = False

    # Update sensor data — only flag changed if values actually differ.
    sensors = payload.get("sensors")
    if isinstance(sensors, dict) and sensors:
        for key, value in sensors.items():
            if data["sensors"].get(key) != value:
                data["sensors"][key] = value
                changed = True

    # Update location.
    location = payload.get("location")
    if isinstance(location, dict) and location:
        for key, value in location.items():
            if data["location"].get(key) != value:
                data["location"][key] = value
                changed = True

    # Update device info and device registry.
    device_info = payload.get("device_info")
    if isinstance(device_info, dict) and device_info:
        data["device_info"].update(device_info)
        _update_device_registry(hass, entry, device_info)
        changed = True

    # Notify entities only when data actually changed.
    if changed:
        from homeassistant.helpers.dispatcher import async_dispatcher_send

        async_dispatcher_send(hass, f"{DOMAIN}_{entry.entry_id}_update")

    # Build response with config (token, actions).
    response: dict[str, Any] = {"status": "ok"}
    config_block: dict[str, Any] = {}

    token = options.get("token", "")
    if token:
        config_block["token"] = token

    actions = options.get("actions", [])
    if actions:
        config_block["actions"] = actions

    if config_block:
        response["config"] = config_block

    return json_response(response)


def _find_entry_by_webhook(
    hass: HomeAssistant, webhook_id: str
) -> ConfigEntry | None:
    """Find config entry matching the webhook ID."""
    for entry in hass.config_entries.async_entries(DOMAIN):
        if entry.data.get("webhook_id") == webhook_id:
            return entry
    return None


def _update_device_registry(
    hass: HomeAssistant, entry: ConfigEntry, device_info: dict[str, Any]
) -> None:
    """Update device registry with info from payload."""
    registry = dr.async_get(hass)
    registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.entry_id)},
        name=entry.title,
        manufacturer=MANUFACTURER,
        model=device_info.get("model", "BYD EV"),
        sw_version=device_info.get("app_version"),
        hw_version=device_info.get("firmware"),
    )

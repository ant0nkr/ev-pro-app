"""Device tracker platform for BYD EV Pro integration."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.device_tracker import SourceType, TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, MANUFACTURER

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up BYD EV Pro device tracker."""
    async_add_entities([BydEvProTracker(hass, entry)])


class BydEvProTracker(TrackerEntity):
    """GPS tracker entity updated via webhook."""

    _attr_has_entity_name = True
    _attr_name = "Location"

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self._hass = hass
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_location"

    @property
    def device_info(self) -> DeviceInfo:
        """Link this entity to the BYD EV Pro device."""
        info = self._hass.data[DOMAIN][self._entry.entry_id].get("device_info", {})
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name=self._entry.title,
            manufacturer=MANUFACTURER,
            model=info.get("model", "BYD EV"),
            sw_version=info.get("app_version"),
            hw_version=info.get("firmware"),
        )

    @property
    def source_type(self) -> SourceType:
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        loc = self._hass.data[DOMAIN][self._entry.entry_id].get("location", {})
        return loc.get("latitude")

    @property
    def longitude(self) -> float | None:
        loc = self._hass.data[DOMAIN][self._entry.entry_id].get("location", {})
        return loc.get("longitude")

    @property
    def location_accuracy(self) -> int:
        return 10  # metres; DiLink GPS doesn't expose accuracy

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        loc = self._hass.data[DOMAIN][self._entry.entry_id].get("location", {})
        attrs: dict[str, Any] = {}
        if "heading" in loc:
            attrs["heading"] = loc["heading"]
        if "altitude" in loc:
            attrs["altitude"] = loc["altitude"]
        if "gps_fix" in loc:
            attrs["gps_fix"] = loc["gps_fix"]
        # Include battery SOC for map card display.
        sensors = self._hass.data[DOMAIN][self._entry.entry_id].get("sensors", {})
        if "battery_soc" in sensors:
            attrs["battery_level"] = sensors["battery_soc"]
        return attrs

    @property
    def icon(self) -> str:
        return "mdi:car-electric"

    async def async_added_to_hass(self) -> None:
        """Register update dispatcher."""
        self.async_on_remove(
            async_dispatcher_connect(
                self._hass,
                f"{DOMAIN}_{self._entry.entry_id}_update",
                self._handle_update,
            )
        )

    @callback
    def _handle_update(self) -> None:
        """Handle updated data from webhook."""
        self.async_write_ha_state()

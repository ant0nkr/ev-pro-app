"""Sensor platform for BYD EV Pro integration."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    MANUFACTURER,
    SENSOR_DEFINITIONS,
    VEHICLE_STATE_MAP,
    CHARGING_STATE_MAP,
    GUN_STATE_MAP,
    AC_POWER_MAP,
    SEAT_HEAT_MAP,
    STEERING_HEAT_MAP,
)

_LOGGER = logging.getLogger(__name__)

# Sensors that should use human-readable text instead of raw values.
_STATE_MAP_SENSORS: dict[str, dict[int, str]] = {
    "vehicle_state": VEHICLE_STATE_MAP,
    "charging_state": CHARGING_STATE_MAP,
    "charging_gun": GUN_STATE_MAP,
    "ac_power": AC_POWER_MAP,
    "driver_seat_heat": SEAT_HEAT_MAP,
    "steering_heat": STEERING_HEAT_MAP,
}

# Map string names to HA enums.
_DEVICE_CLASS_MAP: dict[str, SensorDeviceClass] = {
    "battery": SensorDeviceClass.BATTERY,
    "voltage": SensorDeviceClass.VOLTAGE,
    "current": SensorDeviceClass.CURRENT,
    "power": SensorDeviceClass.POWER,
    "temperature": SensorDeviceClass.TEMPERATURE,
    "distance": SensorDeviceClass.DISTANCE,
    "speed": SensorDeviceClass.SPEED,
}

_STATE_CLASS_MAP: dict[str, SensorStateClass] = {
    "measurement": SensorStateClass.MEASUREMENT,
    "total_increasing": SensorStateClass.TOTAL_INCREASING,
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up BYD EV Pro sensor entities."""
    entities = [
        BydEvProSensor(hass, entry, key, name, device_class, unit, state_class, icon, precision)
        for key, name, device_class, unit, state_class, icon, precision in SENSOR_DEFINITIONS
    ]
    async_add_entities(entities)


class BydEvProSensor(SensorEntity):
    """A sensor entity updated via webhook data."""

    _attr_has_entity_name = True

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        key: str,
        name: str,
        device_class: str | None,
        unit: str | None,
        state_class: str | None,
        icon: str | None,
        precision: int | None = None,
    ) -> None:
        self._hass = hass
        self._entry = entry
        self._key = key
        self._attr_name = name
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_icon = icon

        if device_class and device_class in _DEVICE_CLASS_MAP:
            self._attr_device_class = _DEVICE_CLASS_MAP[device_class]
        if unit:
            self._attr_native_unit_of_measurement = unit
        if state_class and state_class in _STATE_CLASS_MAP:
            self._attr_state_class = _STATE_CLASS_MAP[state_class]
        if precision is not None:
            self._attr_suggested_display_precision = precision

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
    def native_value(self) -> Any:
        """Return the current sensor value."""
        sensors = self._hass.data[DOMAIN][self._entry.entry_id].get("sensors", {})
        raw = sensors.get(self._key)
        if raw is None:
            return None

        # Map numeric states to human-readable text.
        state_map = _STATE_MAP_SENSORS.get(self._key)
        if state_map is not None:
            int_val = int(raw) if isinstance(raw, (int, float)) else None
            if int_val is not None and int_val in state_map:
                return state_map[int_val]
            return str(raw)

        return raw

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

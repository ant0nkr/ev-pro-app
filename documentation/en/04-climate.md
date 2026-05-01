# Climate Control

The Climate screen provides full HVAC control for the vehicle. All controls read the current state from the car and write changes back immediately. When the app is not connected, all controls show `--` and are disabled.

---

## Temperature Zone

| Control | Type | Range | Notes |
|---|---|---|---|
| Driver Temperature | +/- buttons | 16 -- 32 C | Always visible when AC is on |
| Passenger Temperature | +/- buttons | 16 -- 32 C | Only active when Dual Zone is enabled |
| Inside Temperature | Read-only | -40 to 60 C | Cabin air temperature sensor |
| Outside Temperature | Read-only | -40 to 60 C | Ambient outside temperature sensor |

Temperature changes are applied immediately when you tap a button.

---

## AC Controls

| Control | Values | Description |
|---|---|---|
| A/C Power | On / Off | Master switch for the entire climate system |
| Auto Mode | Auto / Manual | Auto: the system manages fan speed and temperature. Manual: you control fan speed independently. |
| Recirculation | Fresh / Recirc | Fresh: outside air intake. Recirc: recirculate cabin air. |
| Dual Zone | On / Off | Links or unlinks driver and passenger temperature. When off, both zones follow the driver setting. |
| Front Defrost | On / Off | Activates windscreen defogging |
| Rear Defrost | On / Off | Activates the rear window heating element |

---

## Fan Controls

| Control | Values | Notes |
|---|---|---|
| Fan Speed | A (auto) + 1 -- 7 | "A" is shown when Auto Mode is active. In Manual mode, select 1 through 7. |
| Wind Mode | 4 modes | Face, Face + Legs, Legs only, Legs + Windscreen |

Fan speed and wind mode controls are grayed out when Auto Mode is active.

---

## Comfort Controls

> [!NOTE]
> Steering wheel heat and seat controls adapt to your vehicle's supported levels. Most vehicles support 2 levels; select models (Sea Lion 05/06, Seal 05/06 GT, Dolphin 25, Seagull 25) support 3 levels for seat heat and ventilation, and 2 levels for steering wheel heat.

| Control | Levels |
|---|---|
| Steering Wheel Heat | Off / On (most models) or Off / Level 1 / Level 2 (select models) |
| Driver Seat Heat | Off / Level 1 / Level 2 (most models) or Off / Level 1 / Level 2 / Level 3 (select models) |
| Driver Seat Ventilation | Off / Level 1 / Level 2 (most models) or Off / Level 1 / Level 2 / Level 3 (select models) |
| Passenger Seat Heat | Off / Level 1 / Level 2 (most models) or Off / Level 1 / Level 2 / Level 3 (select models) |
| Passenger Seat Ventilation | Off / Level 1 / Level 2 (most models) or Off / Level 1 / Level 2 / Level 3 (select models) |

> [!NOTE]
> Seat heat and ventilation are mutually exclusive per seat. Activating heat on a seat automatically turns off ventilation for that seat, and vice versa.

---

## Write Cooldown

After you change a climate setting, the app briefly ignores the old value coming back from the vehicle (for up to 30 seconds). This prevents the control from flickering between the old and new value while the car processes the change.

---

## See Also

- [Quick Actions Overlay](09-quick-actions.md)
- [Dashboard](03-dashboard.md)
- [Settings](10-settings.md)

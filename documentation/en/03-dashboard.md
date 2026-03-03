# Dashboard

The Dashboard is the default screen when BYD EV Pro opens. It presents real-time battery, power, range, and drivetrain telemetry from the vehicle.

---

## Layout

The Dashboard adapts to the available screen width.

| Screen width | Layout |
|---|---|
| Wide (head unit) | Two-column: left panel (SOC gauge, power flow, range card) + right panel (four sub-tabs) |
| Narrow | Single scrollable column with a tab bar at the top |

---

## SOC Gauge

The state-of-charge gauge is the visual centrepiece of the left panel.

- **Scale**: 0 to 100%
- **Color zones**:

| Range | Color |
|---|---|
| 0 -- 20% | Red |
| 20 -- 40% | Amber |
| 40 -- 100% | Green |

The numeric percentage is displayed in large text at the centre. When disconnected, the centre shows `--`.

**State of Health (SoH) badge** is displayed below the gauge. It indicates the overall health of the high-voltage battery.

| SoH value | Badge color |
|---|---|
| >= 80% | Green |
| 60 -- 79% | Amber |
| < 60% | Red |

> [!NOTE]
> On a new vehicle the SoH reading is 100%. The value changes gradually over the lifetime of the battery.

---

## Power Flow Indicator

The power flow indicator sits below the SOC gauge. It shows the direction and magnitude of battery power using animated directional chevrons.

- **Left-pointing (green, pulsing)**: Battery is charging (power flowing in).
- **Right-pointing**: Battery is discharging (power flowing out to the motor).
- **"Idle"**: Shown when the power value is near zero.

**Discharge color thresholds:**

| Power | Color |
|---|---|
| < 20 kW | Blue |
| 20 -- 50 kW | Amber |
| > 50 kW | Red |

---

## Range Panel

The range panel shows three complementary range estimates side by side.

| Label | Description |
|---|---|
| EV Range | The vehicle's own range estimate |
| Prognosed Range | Calculated from SOC, battery capacity, and your average efficiency over the last 20 charge cycles |
| Actual Range | Calculated from SOC and your current trip's efficiency (falls back to Prognosed if less than 2 km driven) |

All three values are shown in kilometres. When the vehicle is off or disconnected, each shows `--`.

> [!NOTE]
> Prognosed Range becomes more accurate as more charge cycles are recorded. With fewer than 3 cycles on record, the vehicle's own EV Range may be more reliable.

---

## Sub-Tabs

The right panel contains four tabs, each grouping related metrics.

### Cycle

Metrics accumulated since the last completed charge session.

| Metric | Unit |
|---|---|
| Cycle Distance | km |
| Cycle Energy | kWh |
| Cycle Efficiency | kWh/100 km |
| Est. Distance | km |
| Cycle Time | h:mm |

**Efficiency color coding:**

| Efficiency | Color |
|---|---|
| < 23 kWh/100 km | Green |
| 23 -- 30 kWh/100 km | Amber |
| > 30 kWh/100 km | Red |

### Trip

Metrics for the current driving session (since the car was turned on).

| Metric | Unit |
|---|---|
| Trip Distance | km |
| Trip Energy | kWh |
| Avg Speed | km/h |
| Trip Efficiency | kWh/100 km |
| Est. Distance | km |
| Trip Time | h:mm |

> [!NOTE]
> Average speed is calculated by the app from total trip distance and total elapsed time. It is independent of the vehicle's built-in trip computer.

### All Time

Cumulative lifetime statistics, stored locally.

| Metric | Unit |
|---|---|
| Total Distance | km |
| Total Energy | kWh |
| Avg Speed | km/h |
| Efficiency | kWh/100 km |
| Est. Distance | km |
| Drive Time | h:mm |

A **Reset All Time** button appears at the bottom of this tab with a confirmation dialog.

### Battery

Live high-voltage battery and drivetrain telemetry. This tab loads detailed cell-level data on demand.

**Electrical:**

| Metric | Unit |
|---|---|
| Voltage | V |
| Current | A |
| Power | kW |

**Temperatures:**

| Metric | Unit |
|---|---|
| Max Battery Temp | C |
| Min Battery Temp | C |
| Avg Temp | C |
| Motor Temp | C |

**Cell voltages:**

| Metric | Unit |
|---|---|
| Max Cell Voltage | V |
| Min Cell Voltage | V |
| Cell Delta | mV |

**Cell delta color coding:**

| Delta | Color |
|---|---|
| <= 30 mV | Green |
| 31 -- 80 mV | Amber |
| > 80 mV | Red |

> [!NOTE]
> Any value showing `--` means the sensor is unavailable, the vehicle is off, or the reading is invalid. On some models, motor temperature may show `--` when the vehicle has just powered on.

---

## See Also

- [Climate Control](04-climate.md)
- [Charging](05-charging.md)

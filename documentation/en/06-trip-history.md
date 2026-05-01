# Trip History

BYD EV Pro records one trip per ignition cycle. A trip begins when the vehicle enters the READY state and ends when it powers off or enters ACC mode. All trip records are stored locally and displayed in the History tab.

---

## How Trips Are Recorded

A trip corresponds to a single ignition cycle. Two detection methods handle different shutdown scenarios:

**Normal shutdown**: The vehicle transitions from READY to OFF or ACC. The trip is finalized immediately.

**Sleep/gap detection**: If the head unit enters deep sleep during shutdown and misses the explicit state change, the app detects a polling gap of more than 60 seconds and closes the current trip retroactively.

> [!NOTE]
> Only trips with actual distance driven are saved. Brief ignition cycles with no movement (e.g., turning the car on briefly without driving) are discarded.

---

## Trip Data

Each trip records:

| Field | Description |
|---|---|
| Start Time | When the ignition cycle started |
| End Time | When the cycle ended |
| Distance | Kilometres driven |
| Energy Consumed | kWh used during the trip |
| Efficiency | kWh/100 km |
| Avg Speed | km/h |
| Duration | Total driving time |

---

## Duration Tracking

The trip timer only counts time while the vehicle is in the READY state (actively driving). Time spent in ACC mode (e.g., sitting with electronics on but not driving) is excluded. This keeps the average speed calculation accurate.

---

## History Screen

The History tab shows all recorded trips in reverse-chronological order (newest first).

Each trip card displays:

- Date and time
- Distance (km)
- Energy consumed (kWh)
- Efficiency (kWh/100 km)
- Duration (hours and minutes)
- Average speed (km/h)

A **Delete All** button with a confirmation dialog is available. An empty state is shown when no trips have been recorded.

---

## Known Limitations

- If the app is force-stopped mid-trip, the trip may not be finalized. The next launch will attempt to close any open trip automatically.
- The range predictor on the Dashboard uses your average efficiency from the last 20 completed trips.

---

## See Also

- [Dashboard](03-dashboard.md)
- [Charging](05-charging.md)

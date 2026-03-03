# Charging Session Tracking

BYD EV Pro automatically detects charging sessions and records them to a local database. Each session captures start/end state-of-charge, energy added, duration, and average charging speed.

---

## How Charging Is Detected

The app uses multiple methods to detect charging:

| Method | How It Works | Notes |
|---|---|---|
| Primary | Detects the vehicle's charging status signal | May not work on all firmware versions (see below) |
| Fallback | Detects charging gun connected + power flowing into battery | Works on all tested models |
| SOC Jump | Detects SOC increase > 5% between sessions | Catches charging that happened while the app was off |

> [!NOTE]
> On some BYD vehicles with newer firmware (DiLink 5.1), the primary charging status signal is not reported correctly. The app automatically uses the fallback method in this case — no user action is needed. See [Compatibility](12-compatibility.md) for details.

The charging signal must be stable for approximately 15 seconds before a session is confirmed, to prevent brief sensor spikes from creating false sessions.

---

## What Gets Recorded

| Field | Description |
|---|---|
| Start Time | When charging was detected |
| End Time | When charging ended |
| Start SOC | Battery percentage at session start |
| End SOC | Battery percentage at session end |
| Energy Added | Estimated energy in kWh |
| Duration | Total session time |
| Avg Charging Speed | Average power during the session (kW) |

> [!NOTE]
> Energy is estimated from the SOC change and your configured battery capacity (see **Settings > Battery Capacity**). If your vehicle has a different battery pack size than the default 87.4 kWh, adjust this setting for accurate energy figures.

---

## Charging Screen

The Charging tab shows all recorded sessions in reverse-chronological order (newest first).

Each session card displays:

- Date and time
- SOC range (e.g., 45% -> 80%)
- Energy added (kWh)
- Duration (hours and minutes)
- Average charging speed (kW)

A **Delete All** button with a confirmation dialog is available at the top. An empty-state message is shown when no sessions have been recorded yet.

---

## Known Limitations

- The SOC-jump detection fires once on app startup if a charge happened while the app was off. Duration is not recorded in that case.
- Average charging speed shows `--` for sessions with zero duration.

---

## See Also

- [Dashboard](03-dashboard.md)
- [Settings](10-settings.md)

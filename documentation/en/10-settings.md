# Settings

The Settings screen is organized into sections: Vehicle, Connectivity, Default Apps, Voice Assistant, Appearance, and Diagnostics & Data.

---

## Vehicle

| Setting | Default | Description |
|---|---|---|
| Battery Capacity | 87.4 kWh | Usable battery capacity for energy calculations and range estimation. Adjust this if your vehicle has a different pack size. 21 presets available plus custom entry. |

---

## Connectivity

| Setting | Default | Description |
|---|---|---|
| Auto-Start | On | Launch the app automatically on system boot and screen-on events. |
| Quick Actions Overlay | Off | Show or hide the floating quick actions pill. See [Quick Actions](09-quick-actions.md). |
| Bring to Foreground on Wake | Off | When enabled, the app comes to the foreground automatically when the car screen turns on. |
| Keep WiFi on ACC Off | Off | Re-enable WiFi automatically after ignition off. *(Extended version)* |
| Keep Mobile Data on ACC Off | Off | Re-enable mobile data automatically after ignition off. *(Extended version)* |
| Keep Bluetooth on ACC Off | Off | Re-enable Bluetooth automatically after ignition off. *(Extended version)* |
| Run While Parked | Off | Keep the app running and polling sensors while the car is parked (OFF state). |
| Slow Poll Mode | Off | Reduce polling frequency to save resources. Useful when running while parked. |
| Disable Traffic Monitor | Off | Disable the BYD traffic monitor service that can interfere with connectivity. |

---

## Default Apps

| Setting | Default | Description |
|---|---|---|
| Default Navigation | (not set) | Select a navigation app from the list of installed apps. Used by the "launch navigation" voice command. |
| Default Music | (not set) | Select a music app from the list of installed apps. Used by the "launch music" voice command. The selected app will also auto-play when launched. |

---

## Voice Assistant

| Setting | Default | Description |
|---|---|---|
| Voice Assistant | Off | Master enable for all voice functionality. |
| Listen for Wake Phrase | Off | When enabled, continuously listens in the background for the wake phrase. |
| PTT Overlay | Off | Show a dedicated push-to-talk floating button. Tap to activate voice recognition on demand. |
| Configure | — | Opens the voice configuration screen: wake phrases, your name, and per-command enable/disable toggles. |

See [Voice Assistant](08-voice-assistant.md) for the full list of 36 supported commands.

---

## Appearance

| Setting | Default | Description |
|---|---|---|
| Theme | System | **System** — follows Android dark/light mode. **Light** — forces light theme. **Dark** — forces dark theme. Applied immediately. |
| Language | System | **System** — follows Android locale. **English** — forces English. **Ukrainian** — forces Ukrainian. Also changes the overlay pill label and voice recognition language. |

---

## Diagnostics & Data

| Action | Description |
|---|---|
| View Logs | Opens the log viewer with filterable tabs (All / Voice / DiLink / Auto / Polling / App / Debug). |
| Clear Diagnostic Logs | Deletes all log entries from the in-app log viewer. |
| Export Diagnostic Bundle | Saves a comprehensive diagnostic file to the device. |
| Send Brief Report | Sends a text summary of recent activity to the developer via Telegram. |
| Send Detailed Report | Sends the full diagnostic bundle and recent logs to the developer via Telegram. |
| Refresh FID Config | Force re-download of remote sensor compatibility rules. |

> [!NOTE]
> The diagnostic bundle is the primary tool for investigating vehicle-specific issues. Include it when reporting a problem.

---

## Integrations

| Action | Description |
|---|---|
| Telegram Bot | Connect the app to a Telegram bot for remote status, battery details, camera, and log uploads. See [Telegram](14-telegram.md). |
| Home Assistant | Configure webhook sync to push vehicle telemetry to Home Assistant in real time. See [Home Assistant](15-home-assistant.md). |

> [!NOTE]
> Telegram and Home Assistant integrations are available in the **Extended version** only (requires an active subscription or trial).

---

## Vehicle Info

This section is read-only. It displays information about your head unit and vehicle detected at connection time.

| Field | Description |
|---|---|
| Product Model | Head unit model name |
| Detected Vehicle | Vehicle name parsed from firmware |
| Vehicle Software | Vehicle software version |
| MCU Version | MCU firmware version |
| DiLink Version | DiLink generation and UI version |
| Protocol | CAN-FD or CAN 2.0 based on firmware |
| Drive Type | BEV / HEV / DM-i Plug-in Hybrid |
| Hardware Version | Hardware revision |
| Car Series | BYD vehicle series (e.g., Ocean, Dynasty) |

> [!NOTE]
> MCU Version shows "MCU_OFFLINE" when the car is in the OFF state. The real version appears once the vehicle enters ACC or READY state.

---

## About

| Field | Description |
|---|---|
| App version | Current installed version |
| Developer | Anton Kramskyi |
| Installation ID | Unique identifier for your app instance (UUID). Tap to copy. |
| FID Config | Shows the current remote config version, rule count, and last fetch date. |
| Subscription | Subscription or trial status, with activate/extend buttons. |
| Donation QR | Monobank donation link displayed as a QR code. |

---

## See Also

- [Voice Assistant](08-voice-assistant.md)
- [Quick Actions](09-quick-actions.md)
- [Diagnostics](11-diagnostics.md)
- [Telegram](14-telegram.md)
- [Home Assistant](15-home-assistant.md)

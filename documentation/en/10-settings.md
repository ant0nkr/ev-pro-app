# Settings

The Settings screen is the last tab in the navigation bar. It is organized into sections: Vehicle, Voice Assistant, Appearance, Data, Vehicle Info, and About.

---

## Vehicle

| Setting | Default | Description |
|---|---|---|
| Battery Capacity | 87.4 kWh | Usable battery capacity for energy calculations and range estimation. Adjust this if your vehicle has a different pack size. |
| Auto-Start | On | Launch the app automatically on system boot and screen-on events. |
| Legacy Connection | Off | Use an alternative (slower) connection method. Enable this if the default connection fails on your head unit model. |
| Quick Actions Overlay | Off | Show or hide the floating quick actions pill. See [Quick Actions](09-quick-actions.md). |

---

## Voice Assistant

| Setting | Default | Description |
|---|---|---|
| Voice Assistant | Off | Master enable for all voice functionality. Cannot be turned on without an API key. |
| Activation Mode | Wake Phrase | **Always Listening** — continuously listens for the wake phrase. **Push to Talk** — activates only when the overlay pill is tapped. |
| ElevenLabs API Key | (empty) | API key for cloud speech recognition and text-to-speech. Shows "Not set" or "Configured". The key is only sent to ElevenLabs servers. |
| Recognition Language | Both | **Ukrainian**, **English**, or **Both** (auto-detect). Specifying a single language improves recognition accuracy. |
| Wake Phrases | "привiт бiуайдi" / "hello byd" | Custom wake phrases for Ukrainian and English. Punctuation is stripped automatically. |
| Your Name | (empty) | Optional. When set, voice confirmations are personalized (e.g., "Hi Anton, turning on climate"). |
| TTS Voice ID | (empty) | ElevenLabs voice ID for custom TTS output. Leave empty to use the default voice. |

See [Voice Assistant](08-voice-assistant.md) for the full list of 26 supported commands.

---

## Appearance

| Setting | Default | Description |
|---|---|---|
| Theme | System | **System** — follows Android dark/light mode. **Light** — forces light theme. **Dark** — forces dark theme. Applied immediately. |
| Language | System | **System** — follows Android locale. **English** — forces English. **Ukrainian** — forces Ukrainian. Also changes the overlay pill label. |

---

## Data

| Action | Description |
|---|---|
| Clear Diagnostic Logs | Deletes all log entries from the in-app log viewer. A confirmation dialog is shown. |
| Export Diagnostic Bundle | Saves a comprehensive diagnostic JSON file to the device. Useful for reporting issues. |
| Send Brief Report | Sends a text summary of recent activity to the developer via Telegram. |
| Send Detailed Report | Sends the full diagnostic bundle and recent logs to the developer via Telegram. Use this when investigating specific issues. |

> [!NOTE]
> The diagnostic bundle is the primary tool for investigating vehicle-specific issues. Include it when reporting a problem.

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
| DiLink Type | DiLink hardware type identifier |
| Hardware Version | Hardware revision |
| Firmware ID | Full firmware identifier string |
| Car Series | BYD vehicle series (e.g., Ocean, Dynasty) |

> [!NOTE]
> MCU Version shows "MCU_OFFLINE" when the car is in the OFF state. The real version appears once the vehicle enters ACC or READY state.

---

## About

| Field | Description |
|---|---|
| App version | Current installed version |
| Developer | Anton Kramskyi |
| Donation QR | Monobank donation link displayed as a QR code at the bottom of the Settings screen |

---

## See Also

- [Voice Assistant](08-voice-assistant.md)
- [Quick Actions](09-quick-actions.md)
- [Diagnostics](11-diagnostics.md)

# BYD EV Pro — Overview

BYD EV Pro is an Android application designed to run directly on BYD DiLink in-car head units. It provides real-time EV diagnostics, climate control, voice assistant, and programmable automation — without any external hardware. No OBD adapter, no Bluetooth dongle, no paired smartphone required. The app communicates directly with the vehicle's built-in systems.

> [!NOTE]
> ADB (Android Debug Bridge) access is required for the app to function. The app uses ADB to communicate with vehicle systems directly on the head unit.

---

## Features

- **Dashboard** — Real-time battery state-of-charge, power flow, estimated range, voltage, current, motor temperatures, cell voltage spread, and gear position.
- **Climate Control** — Full HVAC control: AC on/off, target temperature, seat heating and ventilation (driver and passenger), steering wheel heat, front and rear window defrost.
- **Charging Session Tracking** — Automatic detection and logging of every charge event with start/end SOC, energy added (kWh), duration, and average charging speed.
- **Trip History** — Per-session trip records: distance, energy consumed, efficiency (kWh/100 km), and session duration.
- **Automation Engine** — IF/THEN rule system triggered on vehicle state transitions (OFF / ACC / READY). Supports optional auto-revert after a configurable duration.
- **Voice Assistant** — 26 bilingual (English/Ukrainian) voice commands using ElevenLabs cloud STT and TTS with wake-word activation or push-to-talk. See [Voice Assistant](08-voice-assistant.md).
- **Quick Actions Floating Overlay** — Always-on-top draggable pill that expands into a button grid for A/C, wheel heat, defrost, and seat controls — accessible from any screen. See [Quick Actions](09-quick-actions.md).
- **Diagnostic Export and Reporting** — One-tap export of a full diagnostic bundle (JSON) and Telegram-based bug reporting.

---

## Languages

The app is fully bilingual: **English** and **Ukrainian**. Language selection is available in Settings and persists across sessions. Voice assistant commands and TTS responses are also bilingual.

---

## What This App Is Not

| This app does NOT... | Why |
|---|---|
| Use an OBD-II / ELM327 adapter | Not needed — the app communicates directly with the vehicle via the head unit |
| Use Bluetooth | No BLE pairing or scanning is involved |
| Run on iOS or desktop | Android-only; designed for BYD DiLink head units |
| Run on a paired phone | The app runs on the head unit itself |
| Require a cloud account | No account, no login, no mandatory internet connection (except for voice assistant) |

---

## Supported Vehicles

The app is developed and tested on the **BYD Song Plus EV 2025** (Ocean series, DiLink 5.0). It is expected to be compatible with other BYD vehicles running DiLink 3.0 through 6.0. See [Compatibility](12-compatibility.md) for the full list of supported models.

| Field | Value |
|---|---|
| Primary test vehicle | BYD Song Plus EV 2025 |
| Series | Ocean |
| Default battery capacity | 87.4 kWh (user-configurable) |

---

## Documentation and Releases

Documentation and APK releases are published on GitHub:

**[github.com/ant0nkr/ev-pro-app](https://github.com/ant0nkr/ev-pro-app)**

- **[Documentation (EN)](https://github.com/ant0nkr/ev-pro-app/tree/main/documentation/en)** | **[Documentation (UA)](https://github.com/ant0nkr/ev-pro-app/tree/main/documentation/ua)**
- **[Releases and Release Notes](https://github.com/ant0nkr/ev-pro-app/releases)**

Documentation is updated alongside new releases to reflect the latest functionality.

---

## See Also

- [Installation](02-installation.md)
- [Compatibility](12-compatibility.md)

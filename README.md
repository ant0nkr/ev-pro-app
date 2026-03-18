# BYD EV Pro

Android application for BYD DiLink head units providing real-time EV diagnostics, climate control, voice assistant, and programmable automation.

Runs directly on the head unit — no OBD adapter, no Bluetooth, no paired phone required. ADB access is required.

## Features

### Free

- **Dashboard** — Real-time SOC, power flow, range, voltage, current, motor temps, cell voltage spread
- **Charging Tracking** — Automatic session detection with SOC, energy, duration, avg speed
- **Trip History** — Per-ignition-cycle records: distance, energy, efficiency, avg speed
- **Automation** — IF/THEN rules triggered on vehicle state transitions; includes predefined winter/summer comfort rules
- **Voice Assistant** — 35 bilingual (EN/UK) commands via VOSK (offline) or ElevenLabs (cloud); per-command enable/disable
- **Quick Actions Overlay** — Floating pill with one-tap climate and seat controls
- **Diagnostic Export** — Full diagnostic bundle for troubleshooting

### Subscription (7-day free trial)

- **Telegram Notifications** — Automatic alerts for charging events, gun connection, trip summaries; bot registration with multi-user support
- **Home Assistant Integration** — Push live vehicle sensors to HA via webhook; voice-triggered HA service calls; HACS custom component included
- **WiFi / 4G Keep-Alive** — Automatically re-enables WiFi and mobile data after ignition off (useful for remote monitoring)
- **Remote Commands** — Execute vehicle commands remotely via Telegram bot

Activate the trial from the **About** tab in the app. No payment required for the first 7 days.

## Supported Vehicles

Developed and tested on **BYD Song Plus EV 2025** (DiLink 5.0). Compatible with BYD vehicles running DiLink 3.0 through 6.0. See the compatibility table ([EN](documentation/en/12-compatibility.md) | [UA](documentation/ua/12-compatibility.md)) for the full list.

## Documentation

Full user documentation is available in two languages:

- **[English](documentation/en/)** | **[Ukrainian / Українська](documentation/ua/)**

| # | Guide (EN) | Guide (UA) | Description |
|---|---|---|---|
| 01 | [Overview](documentation/en/01-overview.md) | [Огляд](documentation/ua/01-overview.md) | App description, features |
| 02 | [Installation](documentation/en/02-installation.md) | [Встановлення](documentation/ua/02-installation.md) | Install, first launch |
| 03 | [Dashboard](documentation/en/03-dashboard.md) | [Панель](documentation/ua/03-dashboard.md) | SOC, power flow, range |
| 04 | [Climate](documentation/en/04-climate.md) | [Клімат](documentation/ua/04-climate.md) | AC, temperature, seats |
| 05 | [Charging](documentation/en/05-charging.md) | [Зарядка](documentation/ua/05-charging.md) | Session tracking |
| 06 | [Trip History](documentation/en/06-trip-history.md) | [Поїздки](documentation/ua/06-trip-history.md) | Trip records |
| 07 | [Automation](documentation/en/07-automation.md) | [Автоматизація](documentation/ua/07-automation.md) | Rules, sensors, actions |
| 08 | [Voice Assistant](documentation/en/08-voice-assistant.md) | [Голосовий асистент](documentation/ua/08-voice-assistant.md) | 35 commands, VOSK/ElevenLabs, PTT |
| 09 | [Quick Actions](documentation/en/09-quick-actions.md) | [Швидкі дії](documentation/ua/09-quick-actions.md) | Floating overlay |
| 10 | [Settings](documentation/en/10-settings.md) | [Налаштування](documentation/ua/10-settings.md) | All settings |
| 11 | [Diagnostics](documentation/en/11-diagnostics.md) | [Діагностика](documentation/ua/11-diagnostics.md) | Log viewer, export |
| 12 | [Compatibility](documentation/en/12-compatibility.md) | [Сумісність](documentation/ua/12-compatibility.md) | Supported models |
| 13 | [Troubleshooting](documentation/en/13-troubleshooting.md) | [Вирішення проблем](documentation/ua/13-troubleshooting.md) | Common issues |

## Home Assistant (HACS)

A custom component is included in this repository for Home Assistant integration. To install:

1. Open HACS in Home Assistant
2. Go to Integrations → Custom repositories
3. Add `ant0nkr/ev-pro-app` with category **Integration**
4. Install **BYD EV Pro** and restart Home Assistant
5. Configure the webhook URL and access token in the integration settings

Requires an active subscription in the app.

## Releases

APK releases with release notes are published on the [GitHub Releases](https://github.com/ant0nkr/ev-pro-app/releases) page. Documentation is updated alongside each release to reflect new functionality.

## Languages

English and Ukrainian. Language can be changed in Settings.

## Author

Anton Kramskyi

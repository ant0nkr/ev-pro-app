# Home Assistant Integration

BYD EV Pro can push real-time vehicle telemetry to Home Assistant via a webhook. A HACS custom component is provided that creates sensor entities and a GPS device tracker automatically.

> [!NOTE]
> Home Assistant integration is available in the **Extended version** only (requires an active subscription or trial).

---

## Overview

| | |
|---|---|
| Integration type | Webhook (cloud_push) |
| Data direction | Car → Home Assistant (one-way push) |
| HACS component | `byd_ev_pro` |
| Platforms | Sensor, Device Tracker |
| Sensors | 25 |

The car pushes sensor data to your Home Assistant instance at regular intervals. No polling from HA is needed — the integration receives data passively via webhook.

---

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance.
2. Go to **Integrations > Custom Repositories**.
3. Add the repository URL: `https://github.com/ant0nkr/ev-pro-app` (category: Integration). The HACS component is located in the `homeassistant/` directory.
4. Search for **BYD EV Pro** and install.
5. Restart Home Assistant.

### Manual

1. Download the `homeassistant/custom_components/byd_ev_pro/` directory from this repository.
2. Copy it to your Home Assistant `config/custom_components/` folder.
3. Restart Home Assistant.

---

## Configuration

1. In Home Assistant, go to **Settings > Devices & Services > Add Integration**.
2. Search for **BYD EV Pro**.
3. Enter a name for your vehicle (e.g., "Song Plus EV").
4. The integration will display a **webhook URL** — copy it.
5. In the BYD EV Pro app on your car, go to **Settings > Home Assistant** and paste the webhook URL.

The car will begin pushing data to Home Assistant.

---

## Options

After setup, go to the integration's options to configure:

| Option | Description |
|---|---|
| Long-lived access token | HA access token for authenticated webhook calls |
| Webhook secret | HMAC signing key for webhook payload verification |
| Voice actions | Map HA scripts to voice commands in the car (see below) |

---

## Sensors

The integration creates 25 sensor entities:

### Battery

| Sensor | Unit | Description |
|---|---|---|
| Battery Level | % | Current state of charge (SOC) |
| Battery Health | % | State of health (SoH) |
| HV Battery Voltage | V | High-voltage battery pack voltage |
| HV Battery Current | A | Battery current (positive = discharge, negative = charge) |
| Battery Power | kW | Instantaneous battery power |
| 12V Battery | V | Auxiliary 12V battery voltage |
| Cell Max Voltage | V | Highest individual cell voltage |
| Cell Min Voltage | V | Lowest individual cell voltage |

### Temperature

| Sensor | Unit | Description |
|---|---|---|
| Cabin Temperature | °C | Interior cabin temperature |
| Outside Temperature | °C | Exterior ambient temperature |
| Battery Max Temperature | °C | Highest battery module temperature |
| Battery Min Temperature | °C | Lowest battery module temperature |
| Front Motor Temperature | °C | Front electric motor temperature |

### Driving

| Sensor | Unit | Description |
|---|---|---|
| EV Range | km | Estimated remaining range |
| Odometer | km | Total distance (monotonically increasing) |
| Speed | km/h | Current vehicle speed |
| Vehicle State | — | OFF / ACC / READY |
| Front Motor Speed | RPM | Front motor rotation speed |

### Charging

| Sensor | Unit | Description |
|---|---|---|
| Charging State | — | Not Charging / Charging / Charge Complete |
| Charging Gun | — | Disconnected / AC / DC |

### Climate

| Sensor | Unit | Description |
|---|---|---|
| Climate | — | Off / On |
| Driver Temperature Setting | °C | Target temperature for driver zone |
| Fan Speed | — | Current fan speed level |
| Steering Wheel Heat | — | Off / On |
| Driver Seat Heat | — | Off / Level 1 / Level 2 |

---

## Device Tracker (GPS)

The integration creates a GPS device tracker entity (`device_tracker.{vehicle_name}_location`) with:

- Latitude and longitude
- Heading and altitude (when available)
- Battery SOC displayed on the map card

Location updates are pushed alongside sensor data when the car has a GPS fix.

---

## Voice Actions

You can map Home Assistant scripts to voice commands in the car. This lets you say things like "open the gate" and have the car trigger an HA script.

To add a voice action:

1. Go to the integration options in HA.
2. Select **Add voice action**.
3. Pick a script from the dropdown.
4. Set voice phrases in Ukrainian and/or English.
5. Optionally set confirmation phrases the car will speak back.

The car picks up these actions via the webhook response and adds them to the voice assistant.

---

## See Also

- [Settings](10-settings.md)
- [Voice Assistant](08-voice-assistant.md)
- [Telegram](14-telegram.md)

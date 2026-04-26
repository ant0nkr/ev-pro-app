# BYD EV Pro — Light vs Pro

The BYD EV Pro ecosystem is available in two configurations:

- **Light** — head unit app on BYD DiLink + companion app on the phone. No additional hardware.
- **Pro** — Light + the T-Box hardware module installed in the car. The module adds an always-on remote channel, GPS tracking, proximity-based keyless access, and reliable push notifications even when the car is fully off.

> [!NOTE]
> In the Light edition, remote features work only while the head unit has stable internet. The built-in DiLink 4G modem currently does not work reliably, so the only stable channel is **Wi-Fi**. If you want 24/7 connectivity without a T-Box, the recommended setup is a **USB Wi-Fi dongle** in the car (for example, connected to a portable 4G router or your phone's hotspot) — the head unit stays online even after the car is shut off. With the Pro edition the T-Box provides its own independent connection, so a Wi-Fi dongle is not needed.

---

## Security

Both editions use the same high security standards. There are no compromises in Light.

- **End-to-end AES-256-GCM encryption** of every command and telemetry payload between phone, car, and cloud.
- **HMAC-SHA256** authentication on every message.
- **Biometric gate** for sensitive commands: door unlock, trunk, and remote start. Confirmed via Face ID / Touch ID / Android Biometric.
- **One-time QR pairing** — the secret is never transmitted in plaintext.
- **Per-vehicle and per-phone keys.** Compromising one device does not affect the others.
- **RTT anti-relay protection** *(Pro)* — proximity unlock uses instant ping-pong challenges between phone and car. This blocks "relay attacks" where an attacker amplifies the BLE signal between your phone at home and the car parked outside.
- **Local secret storage** in OS-protected vaults: Android Keystore and iOS Keychain.
- **No server-held passwords** — all keys are generated on user devices.

---

## Feature comparison

### Vehicle monitoring

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 1 | Car on/off monitoring | No / Yes\* | Yes |
| 2 | Door open/close monitoring | No / Yes\* | Yes |
| 3 | Window and sunroof open/close monitoring | No / Yes\* | Yes |
| 4 | Lock state monitoring | No / Yes\* | Yes |
| 5 | Trunk and hood state monitoring | No / Yes\* | Yes |
| 6 | Battery state of charge (SOC) | Yes | Yes |
| 7 | Remaining range (km) | Yes | Yes |
| 8 | Battery temperature | Yes | Yes |
| 9 | Tire pressure (TPMS) | Yes | Yes |
| 10 | Battery state of health (SOH %) | Yes | Yes |
| 11 | 12V auxiliary battery voltage | Yes | Yes |
| 12 | Odometer | Yes | Yes |
| 13 | Average consumption / efficiency | Yes | Yes |
| 14 | Cell voltages and delta | Yes | Yes |
| 15 | Charging state and live power | Yes | Yes |

### Location

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 16 | Vehicle location (GPS) | No / Yes\* | Yes (24/7) |
| 17 | GPS accuracy and live updates | No | Yes |

### Cameras

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 18 | Cabin camera snapshot | Yes\* | Yes |
| 19 | Dashcam snapshot / video | Yes\* | Yes |
| 20 | Live camera streaming to phone | Yes\* | Yes |
| 21 | Sentry mode (motion detection, clips) | Yes\* | Yes |
| 22 | Sentry push alerts | No / Yes\* | Yes |

### Remote climate control

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 23 | A/C on/off | No / Yes\* | Yes |
| 24 | Climate target temperature | No / Yes\* | Yes |
| 25 | Seat heat / ventilation (driver and passenger) | No / Yes\* | Yes |
| 26 | Steering wheel heat | No / Yes\* | Yes |
| 27 | Front windshield defrost | No / Yes\* | Yes |
| 28 | Rear window defrost | No / Yes\* | Yes |
| 29 | Auto-restore climate on ignition | Yes | Yes |

### Remote vehicle control

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 30 | Lock / unlock doors | No / Yes\* | Yes |
| 31 | Open / close trunk | No / Yes\* | Yes |
| 32 | Close windows | No / Yes\* | Yes |
| 33 | Window ventilation (summer) | No / Yes\* | Yes |
| 34 | Remote start | No | Yes |
| 35 | Biometric command confirmation | Yes | Yes |

### Vehicle security

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 36 | Proximity unlock (keyless access) | No | Yes |
| 37 | RTT anti-relay protection | No | Yes |
| 38 | Alarm (door/hood monitoring) | Yes\* | Yes |
| 39 | Auto-arm alarm when leaving | No | Yes |
| 40 | Encrypted channels (AES-256-GCM) | Yes | Yes |

### Charging

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 41 | Live charging information | Yes | Yes |
| 42 | Charging session history | Yes | Yes |
| 43 | "Charging complete" push alert | No / Yes\* | Yes |
| 44 | Low 12V battery alert | No / Yes\* | Yes |

### History and statistics

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 45 | Trip history | Yes | Yes |
| 46 | Trip history sync to phone | No / Yes\* | Yes |
| 47 | Statistics (mileage, energy, efficiency) | Yes | Yes |
| 48 | Parking history | No | Yes |

### Voice and automation

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 49 | Voice assistant (36 commands) | Yes | Yes |
| 50 | On-vehicle automation rules | Yes | Yes |
| 51 | Quick Actions floating panel | Yes | Yes |

### Integrations

| # | Feature | Light | Pro |
|---|---------|:-----:|:---:|
| 52 | Home Assistant integration (HACS) | Yes | Yes |
| 53 | Telegram bot (alerts and commands) | Yes | Yes |
| 54 | Phone push notifications | No / Yes\* | Yes |
| 55 | OTA app updates | Yes | Yes |

---

**Notes:**

\* Works only while the car's head unit has stable internet. The built-in DiLink 4G modem currently does not work reliably — the only stable channel in Light is **Wi-Fi**. As long as the car is on home Wi-Fi or has a USB Wi-Fi dongle attached, these features work. Without an active Wi-Fi connection, remote access to the car is unavailable.

> [!TIP]
> For 24/7 monitoring on the Light edition, install a **USB Wi-Fi dongle** in the car (for example, paired with a portable 4G router or your phone's hotspot). The head unit stays online even after the car is shut off.

In the **Pro** edition, the T-Box module provides:
- its own independent connection (no Wi-Fi dongle required),
- a dedicated GPS receiver,
- proximity-based keyless access with relay-attack protection (RTT),
- reliable 24/7 push notifications,
- remote start.

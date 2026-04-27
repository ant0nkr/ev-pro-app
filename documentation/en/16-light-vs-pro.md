# BYD EV Pro — Free / TG-HA / Lite / Pro

The BYD EV Pro ecosystem is available in four tiers:

- **Free** — head unit app only, on the BYD DiLink. No cloud features. All data stays in the car.
- **TG/HA** — Free + Telegram bot and Home Assistant (HACS) integrations. Receive alerts and control the car from Telegram or HA.
- **Lite** — TG/HA + companion app on the phone (Android and iOS). Full remote control from the phone.
- **Pro** — Lite + the T-Box hardware module. 24/7 connectivity, GPS, keyless proximity access, and remote start.

> [!NOTE]
> In the **Free** and **TG/HA** tiers all features run on the car or pass through the head unit. The **Lite** and **Pro** tiers add the companion app. In **Lite**, the remote channel uses the head unit's Wi-Fi — for 24/7 monitoring a **USB Wi-Fi dongle** is recommended in the car (paired with a portable 4G router or your phone's hotspot). The **Pro** edition's T-Box module has its own always-on connection, so a Wi-Fi dongle is not required.

---

## Security

All tiers use the same high security standards. There are no compromises.

- **AES-256-GCM encryption** of every payload between devices.
- **HMAC-SHA256** authentication on every message.
- **Biometric confirmation** of sensitive commands in the companion app (Face ID / Touch ID / Android Biometric) — *Lite, Pro*.
- **One-time QR pairing** — the secret is never transmitted in plaintext — *Lite, Pro*.
- **Per-vehicle and per-phone keys.** Compromising one device does not affect the others.
- **RTT anti-relay protection** for proximity unlock — instant ping-pong challenges block attacks where an attacker amplifies the BLE signal between phone and car — *Pro*.
- **Local secret storage** in Android Keystore and iOS Keychain.
- **No server-held passwords** — all keys are generated on user devices.

---

## Feature comparison

Legend:
- **Yes** — feature available
- **TG** — available via the Telegram bot
- **Yes\*** — requires an active Wi-Fi connection on the head unit (dongle)
- **—** — not available

### On-vehicle features

(All of these run locally on the BYD DiLink head unit)

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 1 | Dashboard (SOC, power, range) | Yes | Yes | Yes | Yes |
| 2 | Battery temperature, SOH | Yes | Yes | Yes | Yes |
| 3 | Tire pressure (TPMS) | Yes | Yes | Yes | Yes |
| 4 | 12V auxiliary battery voltage | Yes | Yes | Yes | Yes |
| 5 | Odometer, average consumption | Yes | Yes | Yes | Yes |
| 6 | Cell voltages and delta | Yes | Yes | Yes | Yes |
| 7 | Charging state and live power | Yes | Yes | Yes | Yes |
| 8 | On-vehicle climate control | Yes | Yes | Yes | Yes |
| 9 | Automatic charging session tracking | Yes | Yes | Yes | Yes |
| 10 | Trip history (local) | Yes | Yes | Yes | Yes |
| 11 | Auto-restore climate on ignition | Yes | Yes | Yes | Yes |
| 12 | Voice assistant (36 commands) | Yes | Yes | Yes | Yes |
| 13 | On-vehicle automation rules | Yes | Yes | Yes | Yes |
| 14 | Quick Actions floating panel | Yes | Yes | Yes | Yes |
| 15 | Cameras (local snapshot/video on car) | Yes | Yes | Yes | Yes |
| 16 | Local alarm (door/hood monitoring) | Yes | Yes | Yes | Yes |
| 17 | OTA app updates | Yes | Yes | Yes | Yes |
| 18 | Diagnostic bundle export | Yes | Yes | Yes | Yes |

### Cloud integrations

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 19 | Telegram bot (status, photos, commands) | — | Yes | Yes | Yes |
| 20 | Home Assistant integration (HACS) | — | Yes | Yes | Yes |
| 21 | Wi-Fi / 4G / Bluetooth keep-alive | — | Yes | Yes | Yes |
| 22 | Telegram alerts (charging, trips) | — | Yes | Yes | Yes |
| 23 | Charging-gun connection alert | — | Yes | Yes | Yes |

### Companion app — monitoring

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 24 | Car on/off status | — | TG | Yes\* | Yes |
| 25 | Door open/close status | — | TG | Yes\* | Yes |
| 26 | Window and sunroof status | — | TG | Yes\* | Yes |
| 27 | Lock state | — | TG | Yes\* | Yes |
| 28 | Trunk and hood state | — | TG | Yes\* | Yes |
| 29 | SOC in the app | — | TG | Yes\* | Yes |
| 30 | Range in the app | — | TG | Yes\* | Yes |
| 31 | Tire pressure in the app | — | TG | Yes\* | Yes |
| 32 | Battery voltages / temperatures in the app | — | TG | Yes\* | Yes |
| 33 | Vehicle location (GPS) | — | TG | Yes\* | Yes (24/7) |

### Companion app — control

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 34 | Lock / unlock doors | — | TG | Yes\* | Yes |
| 35 | Open / close trunk | — | TG | Yes\* | Yes |
| 36 | Close windows | — | TG | Yes\* | Yes |
| 37 | Window ventilation | — | TG | Yes\* | Yes |
| 38 | A/C on/off | — | TG | Yes\* | Yes |
| 39 | Climate target temperature | — | TG | Yes\* | Yes |
| 40 | Seat heat / ventilation | — | TG | Yes\* | Yes |
| 41 | Steering wheel heat | — | TG | Yes\* | Yes |
| 42 | Front / rear defrost | — | TG | Yes\* | Yes |
| 43 | Biometric command confirmation | — | — | Yes | Yes |
| 44 | Remote start | — | — | — | Yes |

### Cameras (from phone)

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 45 | Cabin camera snapshot | — | TG | Yes\* | Yes |
| 46 | Dashcam snapshot / video | — | TG | Yes\* | Yes |
| 47 | Live camera streaming to phone | — | — | Yes\* | Yes |
| 48 | Sentry mode (motion detection on car) | Yes | Yes | Yes | Yes |
| 49 | Sentry push alerts | — | TG | Yes\* | Yes |

### Security (Pro exclusive)

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 50 | Proximity keyless unlock | — | — | — | Yes |
| 51 | RTT anti-relay protection | — | — | — | Yes |
| 52 | Auto-arm alarm on leaving | — | — | — | Yes |

### Notifications

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 53 | "Charging complete" | — | TG | Yes\* | Yes |
| 54 | Low 12V battery | — | TG | Yes\* | Yes |
| 55 | Phone push notifications | — | — | Yes\* | Yes |
| 56 | Telegram alerts | — | Yes | Yes | Yes |

### History and statistics

| # | Feature | Free | TG/HA | Lite | Pro |
|---|---------|:----:|:-----:|:----:|:---:|
| 57 | Trip history (local on car) | Yes | Yes | Yes | Yes |
| 58 | Trip history sync to phone | — | — | Yes\* | Yes |
| 59 | Statistics (mileage, energy, efficiency) | Yes | Yes | Yes | Yes |
| 60 | Parking history | — | — | — | Yes |

---

**Notes:**

- **Yes\*** means the feature requires an active Wi-Fi connection on the head unit. In the **Lite** edition a **USB Wi-Fi dongle** is recommended for 24/7 connectivity (paired with a portable 4G router or your phone's hotspot). In the **Pro** edition the T-Box module brings its own connection, so a dongle is not required.
- **TG** means the feature is available via the Telegram bot. The user interacts with the bot in Telegram rather than through a separate app.
- The built-in DiLink 4G modem currently does not work reliably — Wi-Fi is required for remote connectivity in the Lite tier.
- Encryption, biometric checks, and anti-relay mechanisms work with the same level of security in all relevant tiers.

In the **Pro** edition, the T-Box module adds:
- its own independent connection (no Wi-Fi dongle needed),
- a dedicated GPS receiver for accurate positioning,
- proximity-based keyless access with relay-attack protection (RTT),
- reliable 24/7 push notifications,
- remote start.

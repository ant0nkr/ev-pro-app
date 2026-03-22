# Telegram Bot

BYD EV Pro can connect to a Telegram bot that lets you check vehicle status, view battery details, capture camera photos and videos, and upload diagnostic logs — all from your phone via Telegram.

> [!NOTE]
> Telegram integration is available in the **Extended version** only (requires an active subscription or trial).

---

## Bot Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and see the welcome message |
| `/register` | Link the bot to your car using your Installation ID |
| `/unregister` | Unlink your Telegram account from the car |
| `/report` | Get a current vehicle status report (SOC, range, temperatures, doors, TPMS, GPS with map) |
| `/battery` | View battery cell voltage details, SoH, pack voltage, and charging state |
| `/photo` | Capture a photo from the car's camera (panorama, front, or cam0) |
| `/video` | Record a 10-second video from the car's camera |
| `/send_logs` | Upload diagnostic logs to the developer |

---

## Screenshots

### `/report` — Vehicle Status

Full status report with SOC, 12V battery, vehicle state, range, temperatures, door status, TPMS pressures, and GPS location with a map pin.

![Telegram /report command](../images/telegram/telegram_report.png)

### `/battery` — Battery Report

Battery cell details: 12V voltage, SOC, SoH, battery temperature range, cell voltage min/max with delta, and pack voltage.

![Telegram /battery command](../images/telegram/telegram_battery.png)

### `/photo` — Camera Capture

Captures a photo from the car's panorama camera and sends it directly to the chat.

![Telegram /photo command](../images/telegram/telegram_photo.png)

### `/video` — Video Recording

Records a 10-second video from the panorama camera, uploads it, and sends it as a video message.

![Telegram /video command](../images/telegram/telegram_video.png)

---

## Setup

1. Open the app and go to **Settings > Telegram Bot**.
2. Tap **Connect** to link the app to the Telegram relay.
3. Open Telegram on your phone and start a conversation with the bot.
4. Send `/register` and follow the instructions to link your car.

Once registered, you can send any of the commands above to get information from your car.

---

## Notifications

The Telegram configuration screen lets you toggle notifications for various events:

- **Master toggle** — Enable or disable all Telegram notifications
- **Report content** — Choose which fields are included in `/report` responses
- **Event notifications** — Get notified about specific vehicle events

---

## How It Works

The app communicates with the Telegram bot through a relay server. The car pushes data to the relay, and the bot fetches commands from it. No direct connection between Telegram and the car is required — the relay handles all communication securely.

- Commands are queued on the relay and picked up by the app on the next poll cycle
- Photos and videos are captured on the head unit and uploaded via the relay
- Status reports use the latest sensor values from the app

---

## See Also

- [Settings](10-settings.md)
- [Diagnostics](11-diagnostics.md)
- [Troubleshooting](13-troubleshooting.md)

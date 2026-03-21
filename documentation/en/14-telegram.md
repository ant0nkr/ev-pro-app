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
| `/report` | Get a current vehicle status report (SOC, range, temperatures, climate state, etc.) |
| `/battery` | View battery cell voltage details |
| `/photo` | Capture a photo from the car's camera (front, panorama, or cam0) |
| `/video` | Capture a video from the car's camera |
| `/cameras` | List available cameras on your head unit |
| `/send_logs` | Upload diagnostic logs to the developer |

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

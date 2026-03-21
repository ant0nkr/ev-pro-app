# Troubleshooting

This page covers common problems, their causes, and solutions. For issues not listed here, check the [Diagnostics](11-diagnostics.md) tab for error entries and export a diagnostic bundle.

---

## Connection Problems

| Problem | Likely Cause | Solution |
|---|---|---|
| Connection indicator stays grey | ADB not enabled on the head unit | Enable ADB in Developer Options. See [Installation](02-installation.md). |
| Connection indicator stays blue (pulsing) | Connection key not trusted | Accept the "Allow USB debugging?" dialog on the head unit. If no dialog appears, try restarting the app. |
| Connection indicator turns red | Vehicle service is temporarily unavailable | Restart the app. If the problem persists, try rebooting the head unit. |

> [!NOTE]
> Connection indicator colors: grey = not connected, blue/pulsing = connecting, green = fully connected, red = error.

---

## Sensor Values

| Problem | Likely Cause | Solution |
|---|---|---|
| All values show `--` | Vehicle is OFF | Values appear when the vehicle enters ACC or READY state. |
| Motor temp shows `--` | Normal on some models | Motor temperature is only valid while driving. |
| Charging status always shows as not charging | Known firmware issue on DiLink 5.1 | No action needed. The app uses an alternative detection method automatically. See [Compatibility](12-compatibility.md). |
| MCU version shows "MCU_OFFLINE" | Car is powered off | Normal. Real MCU version appears in ACC or READY state. |
| Values seem wrong for your vehicle | Different vehicle model may have differences | Export the diagnostic bundle and share with the developer. See [Compatibility](12-compatibility.md). |
| Energy tracking seems incorrect | Battery capacity not configured | Check **Settings > Battery Capacity** and set it to match your vehicle (default is 87.4 kWh for Song Plus EV 2025). |

---

## Charging Detection

| Problem | Likely Cause | Solution |
|---|---|---|
| Charging session not recorded | Detection not triggered | Check the Logs tab while plugging in — look for charging-related entries. If no charging is detected, export a diagnostic bundle and report the issue. |
| Session energy too high or low | Battery capacity setting incorrect | Adjust **Settings > Battery Capacity** to match your vehicle. |

---

## App Lifecycle

| Problem | Likely Cause | Solution |
|---|---|---|
| App stops running in background | Self-start restriction enabled | Go to head unit **Settings > Apps > Self-Start Management**, find BYD EV Pro, and disable the self-start restriction tick. This must be done after every install/update. Also confirm **Auto-Start** is enabled in the app's Settings. |
| App does not auto-start on boot | Varies by DiLink version | Toggle **Auto-Start** off and on in Settings. Some models require a manual app launch after the first boot following installation. |

---

## Voice Assistant

| Problem | Likely Cause | Solution |
|---|---|---|
| Voice assistant not responding | Voice Assistant toggle is off | Check that **Settings > Voice Assistant** is enabled. Ensure either **Listen for Wake Phrase** or **PTT Overlay** is turned on. |
| Wake phrase not recognized | Speech transcription does not match | Check the Logs tab (Voice category) to see the exact transcript. The app handles common pronunciation variants automatically. Try speaking more clearly or switching to Push-to-Talk mode. |
| PTT beep not audible | Media volume is muted | Increase media volume on the head unit. The beep uses the same audio channel as music playback. |

---

## Overlay

| Problem | Likely Cause | Solution |
|---|---|---|
| Quick Actions overlay not appearing | Overlay permission not granted | Try reconnecting — the permission is requested automatically on each connection. You can also check the head unit's **Settings > Apps > BYD EV Pro > Permissions** and enable "Draw over other apps" manually. |

---

## Automation

| Problem | Likely Cause | Solution |
|---|---|---|
| Rule never triggers | Wrong vehicle state selected | Rules fire on state **transitions**, not continuously. Make sure the rule's "Fire when" state matches the state the vehicle enters (not the state it's currently in). Check the Logs tab for state transition events. |
| Rule triggers but nothing happens | Control not responding | Try the same control manually from the Climate screen. If it works there, check the Logs tab for any error messages when the rule fires. |

---

## Telegram Bot

| Problem | Likely Cause | Solution |
|---|---|---|
| Cannot access Telegram settings | Feature not unlocked | Telegram integration requires the Extended version. Check your subscription status in About. |
| Bot not responding to commands | Bot not connected or relay offline | Open **Settings > Telegram Bot** and check that the bot is connected. Try disconnecting and reconnecting. |
| `/report` shows stale data | Vehicle is OFF | Status reports use the last known sensor values. Start the car to get fresh data. |

---

## Home Assistant

| Problem | Likely Cause | Solution |
|---|---|---|
| Cannot access HA settings | Feature not unlocked | Home Assistant integration requires the Extended version. Check your subscription status in About. |
| Sensors show "unavailable" | Webhook not configured or car is OFF | Verify the webhook URL in both the app and HA. Sensors update only when the car pushes data. |
| Location not updating | GPS not available | GPS data is pushed alongside sensor data. Location updates when the car is ON and has a GPS fix. |

---

## Debug Control Panel

| Problem | Likely Cause | Solution |
|---|---|---|
| All actions show "No Readback" | Vehicle is OFF | The Debug Panel requires the car to be in ACC or READY state. |
| Action shows "Mismatch" | Feature ID not correct for your model | Export a diagnostic bundle and report to the developer. A remote FID config update may be needed. |
| Action shows "Failed" | Connection lost or service unavailable | Check the connection indicator. Try reconnecting the app. |

> [!TIP]
> Use the Debug Control Panel (**Settings > View Logs > bug icon**) to see what your car actually reports before sending a bug report. This helps the developer diagnose issues faster.

---

## Collecting Debug Information

When a problem cannot be resolved using the steps above:

1. Open the **Logs** tab and look for red (Error) or dark-red (Critical) entries.
2. Use the **Debug Control Panel** (Settings > View Logs > bug icon) to check if specific controls work and what the car reports.
3. Go to **Settings > Export Diagnostic Bundle** — this saves a comprehensive snapshot to the device.
4. Use **Settings > Send Detailed Report** to send the bundle to the developer via Telegram.

The diagnostic bundle contains sensor data, configuration, and recent log entries — everything needed to diagnose the issue remotely.

---

## See Also

- [Installation](02-installation.md)
- [Diagnostics](11-diagnostics.md)
- [Compatibility](12-compatibility.md)

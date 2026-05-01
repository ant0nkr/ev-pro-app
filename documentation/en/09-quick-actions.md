# Quick Actions Overlay

The Quick Actions Overlay is a floating pill button that stays on top of all applications on the head unit. It provides one-tap access to the most common vehicle controls without opening the main app.

---

## Enabling the Overlay

Navigate to **Settings > Quick Actions Overlay** and turn on the toggle.

The overlay requires the "draw over other apps" permission, which is normally granted automatically when the app first connects. If the overlay does not appear after enabling the setting, try reconnecting via the app's connection button.

---

## The Pill

The overlay appears as a small pill-shaped button floating on the screen.

| Property | Detail |
|---|---|
| Label | "Quick" (English) or "Швидко" (Ukrainian), based on the app language |
| Color | Electric Blue |
| Position | Draggable — tap and hold to reposition anywhere on screen. Position is saved between sessions. |

---

## Tap Behavior

The behavior of a short tap depends on the voice assistant configuration.

| Voice assistant status | Short tap | Long press (> 400 ms) |
|---|---|---|
| Voice enabled + Push-to-Talk mode | Activates voice command (pill turns green, plays beep) | Expands quick actions card |
| Voice enabled + Wake Phrase mode | Expands quick actions card | Expands quick actions card |
| Voice disabled | Expands quick actions card | Expands quick actions card |

---

## Quick Actions Card

Expanding the pill opens a card with two rows of circular control buttons.

### Row 1 — Toggle Controls (On / Off)

| Button | Function | Active Color |
|---|---|---|
| Climate | A/C on (Auto mode) / off | Blue |
| Wheel Heat | Steering wheel heat on / off | Orange |
| Front Defrost | Front windscreen defrost on / off | Blue |
| Rear Defrost | Rear window defrost on / off | Blue |

### Row 2 — Seat Controls (3-State Cycle)

Seat buttons cycle through three states on each tap: **Off > Level 1 > Level 2**.

| Button | Function | Active Color |
|---|---|---|
| Driver Heat | Driver seat heat | Orange |
| Driver Vent | Driver seat ventilation | Light Blue |
| Pass. Heat | Passenger seat heat | Orange |
| Pass. Vent | Passenger seat ventilation | Light Blue |

> [!NOTE]
> Seat heat and ventilation are mutually exclusive per seat. Activating heat automatically turns off ventilation for that seat, and vice versa.

---

## Collapse

Tap anywhere on the expanded card background, or tap the X button in the card header, to collapse back to the pill.

---

## Push-to-Talk Feedback

When voice command is triggered via the pill:

1. Pill background changes to green.
2. A beep plays.
3. The pill stays green until voice recognition completes or the 10-second timeout expires.
4. Pill returns to Electric Blue when the session ends.

See [Voice Assistant](08-voice-assistant.md) for the full list of voice commands.

---

## See Also

- [Voice Assistant](08-voice-assistant.md)
- [Climate](04-climate.md)
- [Settings](10-settings.md)

# Vehicle Compatibility

BYD EV Pro targets BYD vehicles running DiLink 3.0 through 6.0. The app reads the firmware version automatically at connection time and uses it to identify the DiLink generation and vehicle model.

> [!NOTE]
> All features are confirmed on **BYD Song Plus EV 2025** (DiLink 5.0). Other models should work but may have minor differences. See [Reporting Issues](#reporting-compatibility-issues) if values appear incorrect on your vehicle.

---

## How to Check Your Version

1. Open the app and go to **About**.
2. The **Vehicle Info** section shows your firmware details, DiLink version, and detected model.

---

## Supported DiLink Generations

### DiLink 3.0 (Android 10)

| Vehicle Models |
|---|
| Qin Plus DM-i/EV, Song Pro, Yuan Plus, Song Max, Destroyer 05, Dolphins, Tang DM-i |
| Song Plus DM-i, Chazor, King, Atto3, Seagull, Dolphin, E2, M6 |
| Song Plus Champion DM-i/EV, Song Pro, Han, Tang, Seal |
| Song Plus EV 2021-2022, Tang, Yuan Pro |
| Song Plus 520, YuanUp, Song Pro |

### DiLink 4.0 (Android 10)

| Vehicle Models |
|---|
| Han, Tang |
| Song+, Frigate, Seal |

### DiLink 5.0 (Android 12L)

| Vehicle Models |
|---|
| Denza N7/N8/D9 |
| Leopard 3/5 |
| Dynasty |
| Ocean |
| **Sea Lion 05 EV/DM-i, Seal 05/06 GT, Dolphin 25, Seagull 25** *(sensor compatibility improved in 1.0.2)* |
| Yuan Plus 25, Yuan Up 25, Song Pro 25, Qin Plus 25 |
| E7, Han, Tang, Song L, Seal, Sea Lion 07 |
| **Song Plus** (primary test vehicle) |

### DiLink 5.1 (Android 14)

| Vehicle Models |
|---|
| Leopard 5 |
| Denza D9/N9/Z9/Z9 GT |
| Xia |
| Han L, Tang L |
| Leopard 5, Titanium 7, Leopard 8 |
| Qin L, N8L, N9 |

### DiLink 6.0 (Android 12L)

| Vehicle Models |
|---|
| U8, U7, U9 |

---

## Known Platform-Specific Issues

| Issue | Affected Vehicles | Impact |
|---|---|---|
| Charging status not reported correctly | DiLink 5.1 vehicles | No impact — the app automatically uses an alternative detection method |
| MCU version shows "MCU_OFFLINE" | All models when car is OFF | Normal — real values appear when the vehicle is in ACC or READY state |

---

## Compatibility Notes by Version

### 1.0.2
- **Sea Lion 05 / Seagull 25 / Seal 05 / Dolphin 25** (firmware chipset 23, variant 1.22): Fixed firmware detection timing that could show "DiLink unknown" on first connect. Corrected battery voltage, battery current, and motor temperature sensor readings. These models are rear-wheel drive single-motor; the motor temperature display now reads the correct (rear) motor.

---

## Reporting Compatibility Issues

If features display incorrect values or dashes on your vehicle:

1. Open the app and go to **Settings**.
2. Tap **Export Diagnostic Bundle**.
3. Use **Send Detailed Report** to share the bundle with the developer via Telegram.

The diagnostic bundle contains all the information needed to investigate model-specific differences without needing direct access to your vehicle.

---

## See Also

- [Installation](02-installation.md)
- [Troubleshooting](13-troubleshooting.md)

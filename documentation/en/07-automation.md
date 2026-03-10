# Automation Engine

The automation engine lets you define IF/THEN rules that execute vehicle commands automatically when the car changes state. For example: "When the car starts and the outside temperature is below 5 C, turn on the A/C."

---

## How It Works

Rules are **state-transition-triggered**. A rule fires when:

1. The vehicle transitions **into** the rule's required state (e.g., becomes READY).
2. The rule's sensor condition is true at that moment.

Because rules only fire on state transitions, they cannot trigger repeatedly in a loop — each rule fires at most once per transition event.

---

## Vehicle States

| State | Description |
|---|---|
| ON | ACC or READY — fires on either transition (recommended for most rules) |
| OFF | Car powered off |
| ACC | Accessory mode only |
| READY | Ready to drive only |

---

## Rule Structure

Each automation rule contains:

| Component | Description |
|---|---|
| **Name** | Your label for the rule (e.g., "Cold morning comfort") |
| **Enabled** | Toggle on/off — disabled rules are skipped |
| **Condition** | A sensor, an operator, and a threshold value |
| **Fire when** | The vehicle state that must be entered for the rule to trigger. Choose **ON** to fire on ACC or READY (handles vehicles that stay in ACC) |
| **Action** | The vehicle command to execute |
| **Duration** | Optional auto-revert timer (0 = permanent) |

---

## Available Sensors

| Sensor | Unit | Category |
|---|---|---|
| Outside temperature | C | Climate |
| Inside temperature | C | Climate |
| Battery SOC | % | Battery |
| EV range | km | Battery |
| Battery power | kW | Battery |
| Battery max temp | C | Battery |
| Battery min temp | C | Battery |
| Vehicle state | — | Vehicle |
| Speed | km/h | Vehicle |
| Charging gun | — | Charging |

---

## Operators

| Operator | Meaning |
|---|---|
| < | Less than |
| <= | Less than or equal |
| > | Greater than |
| >= | Greater than or equal |
| == | Equal |

---

## Available Actions

### Climate

| Action | Description | Can Auto-Revert |
|---|---|---|
| Turn on A/C (Auto) | Sets AC to auto mode | Yes (reverts to A/C off) |
| Turn off A/C | Powers off climate system | No |
| Steering wheel heat ON | Turns on steering heat | Yes |
| Steering wheel heat OFF | Turns off steering heat | No |
| Front defrost ON | Enables front defrost | Yes |
| Front defrost OFF | Disables front defrost | No |
| Rear defrost ON | Enables rear defrost | Yes |
| Rear defrost OFF | Disables rear defrost | No |

### Seats

| Action | Description | Can Auto-Revert |
|---|---|---|
| Driver seat heat Level 1 | Seat heat low | Yes |
| Driver seat heat Level 2 | Seat heat medium | Yes |
| Driver seat heat Level 3 | Seat heat high (select models) | Yes |
| Driver seat heat Off | Turn off seat heat | No |
| Driver seat vent Level 1 | Seat ventilation low | Yes |
| Driver seat vent Level 2 | Seat ventilation medium | Yes |
| Driver seat vent Level 3 | Seat ventilation high (select models) | Yes |
| Driver seat vent Off | Turn off seat ventilation | No |
| Passenger seat heat Level 1–3 / Off | Same as driver, passenger side | Yes/No |
| Passenger seat vent Level 1–3 / Off | Same as driver, passenger side | Yes/No |
| Steering wheel heat Level 1 | Steering heat on | Yes |
| Steering wheel heat Level 2 | Steering heat high (select models) | Yes |
| Steering wheel heat Off | Turn off steering heat | No |

### Doors

| Action | Description | Can Auto-Revert |
|---|---|---|
| Lock doors | Locks all doors | Yes (reverts to unlock) |
| Unlock doors | Unlocks all doors | Yes (reverts to lock) |

### Windows

| Action | Description | Can Auto-Revert |
|---|---|---|
| Close all windows | Closes all 4 windows | Yes (reverts to open) |
| Open all windows | Opens all 4 windows | Yes (reverts to close) |

### Sunroof

| Action | Description | Can Auto-Revert |
|---|---|---|
| Open sunroof | Opens sunroof fully | Yes (reverts to close) |
| Close sunroof | Closes sunroof | No |
| Tilt sunroof | Tilts to vent position | Yes (reverts to close) |

### Sunshade

| Action | Description | Can Auto-Revert |
|---|---|---|
| Open sunshade | Opens sunshade | Yes (reverts to close) |
| Close sunshade | Closes sunshade | No |

### Trunk

| Action | Description | Can Auto-Revert |
|---|---|---|
| Open trunk | Opens trunk | Yes (reverts to close) |
| Close trunk | Closes trunk | No |

---

## Duration and Auto-Revert

When you set a duration on a rule, the action is automatically reversed after the specified time.

| Duration | Behavior |
|---|---|
| Permanent | Action stays active indefinitely |
| 1 min | Reverts after 1 minute |
| 5 min | Reverts after 5 minutes |
| 15 min | Reverts after 15 minutes |

> [!NOTE]
> The duration picker is only shown for actions that support auto-revert (see the "Can Auto-Revert" column in the action tables above).

---

## Predefined Rules

The app includes several ready-to-use rules that are pre-installed in disabled state. Enable them in the Automation screen with a single tap.

| Name | Condition | Fire When | Action | Duration |
|---|---|---|---|---|
| Winter: Steering wheel heat | Outside temp < 0 °C | ON | Steering wheel heat on | Permanent |
| Winter: Driver seat heat Lvl 2 | Outside temp < 0 °C | ON | Driver seat heat Level 2 | 10 min |
| Winter: Passenger seat heat Lvl 2 | Outside temp < 0 °C | ON | Passenger seat heat Level 2 | 10 min |
| Summer: Driver seat vent Lvl 2 | Inside temp > 15 °C | ON | Driver seat vent Level 2 | Permanent |
| Summer: Passenger seat vent Lvl 2 | Inside temp > 15 °C | ON | Passenger seat vent Level 2 | Permanent |
| Open sunshade on start | Outside temp > 0 °C | ON | Open sunshade | Permanent |

> [!NOTE]
> Predefined rules are seeded once when first installed. They start **disabled** — enable the ones you want.

---

## Creating a Rule

1. Tap the **+** button on the Automation screen.
2. Enter a rule name (e.g., "Cold morning comfort").
3. Select a sensor (e.g., "Outside temperature").
4. Choose an operator (e.g., `<`).
5. Enter a threshold value (e.g., `5`).
6. Select the **Fire when** state. Choose **ON** for most rules — it fires when the car becomes active (ACC or READY).
7. Choose an action (e.g., "Turn on A/C (Auto)").
8. Optionally set a duration (e.g., 10 min).
9. Tap **Save**.

The rule takes effect immediately on the next qualifying state transition.

---

## Example Rules

| Name | Condition | Fire When | Action | Duration |
|---|---|---|---|---|
| Cold morning comfort | Outside temp < 5 °C | ON | Turn on A/C (Auto) | 10 min |
| Night lock | Vehicle state == 0 | OFF | Lock doors | Permanent |
| Summer ventilation | Inside temp > 35 °C | ON | Open all windows | 5 min |
| Charge alert | SOC >= 80 | OFF | Unlock doors | Permanent |

---

## Managing Rules

- **Enable / disable**: Toggle the switch on each rule card. Disabled rules are stored but never evaluated.
- **Edit**: Tap the rule card to open the editor with existing values pre-filled.
- **Delete**: Long-press a rule card and confirm deletion.

All changes are saved immediately and survive app restarts and vehicle power cycles.

---

## See Also

- [Climate](04-climate.md)
- [Voice Assistant](08-voice-assistant.md)

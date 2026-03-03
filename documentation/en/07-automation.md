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
| OFF | Car powered off |
| ACC | Accessory mode (electronics on, not driving) |
| READY | Ready to drive / actively driving |

---

## Rule Structure

Each automation rule contains:

| Component | Description |
|---|---|
| **Name** | Your label for the rule (e.g., "Cold morning comfort") |
| **Enabled** | Toggle on/off — disabled rules are skipped |
| **Condition** | A sensor, an operator, and a threshold value |
| **Fire when** | The vehicle state that must be entered for the rule to trigger |
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

## Creating a Rule

1. Tap the **+** button on the Automation screen.
2. Enter a rule name (e.g., "Cold morning comfort").
3. Select a sensor (e.g., "Outside temperature").
4. Choose an operator (e.g., `<`).
5. Enter a threshold value (e.g., `5`).
6. Select the **Fire when** vehicle state (e.g., READY).
7. Choose an action (e.g., "Turn on A/C (Auto)").
8. Optionally set a duration (e.g., 10 min).
9. Tap **Save**.

The rule takes effect immediately on the next qualifying state transition.

---

## Example Rules

| Name | Condition | Fire When | Action | Duration |
|---|---|---|---|---|
| Cold morning comfort | Outside temp < 5 C | READY | Turn on A/C (Auto) | 10 min |
| Night lock | Vehicle state == 0 | OFF | Lock doors | Permanent |
| Summer ventilation | Inside temp > 35 C | READY | Open all windows | 5 min |
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

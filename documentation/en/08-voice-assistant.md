# Voice Assistant

BYD EV Pro includes a bilingual voice assistant for vehicle control with spoken commands in English or Ukrainian. Two speech recognition backends are available: **VOSK** (offline, default) and **ElevenLabs** (cloud, optional).

---

## Backends

### VOSK — Offline (Default)

| | |
|---|---|
| Internet required | No |
| API key required | No |
| Speech recognition | On-device (VOSK engine) |
| Spoken responses (TTS) | No — confirmation shown as text in the UI |
| Languages | One language at a time (matches app display language) |

VOSK runs entirely on the device. No data is sent anywhere. The recognition model (~80 MB for Ukrainian, ~40 MB for English) must be downloaded once — or use the **Full Edition** which includes models pre-bundled.

### ElevenLabs — Cloud (Optional)

| | |
|---|---|
| Internet required | Yes |
| API key required | Yes ([elevenlabs.io](https://elevenlabs.io)) |
| Speech recognition | ElevenLabs Scribe v2 |
| Spoken responses (TTS) | Yes (`eleven_multilingual_v2`, configurable voice) |
| Languages | Ukrainian, English, or both simultaneously |
| Free tier | ~2.5 hours/month STT + ~10,000 chars/month TTS |

---

## Setup

### VOSK (offline)

1. Open the app and go to **Settings → Voice Assistant**.
2. Make sure **Backend** is set to **VOSK (Offline)**.
3. Enable the **Voice Assistant** toggle.
4. If using the **Lite Edition**: tap **Download Model** to download the recognition model for your app language. The download is ~80 MB (Ukrainian) or ~40 MB (English). Wi-Fi recommended.
5. Select an activation mode: **Always Listening** or **Push to Talk**.

> [!NOTE]
> The **Full Edition** includes models pre-bundled — no download needed.

### ElevenLabs (cloud)

1. Obtain an ElevenLabs API key at [https://elevenlabs.io](https://elevenlabs.io).
2. Open the app and go to **Settings → Voice Assistant**.
3. Set **Backend** to **ElevenLabs (Cloud)**.
4. Enter your key in the **ElevenLabs API Key** field.
5. Enable the **Voice Assistant** toggle.
6. Select an activation mode.

---

## Activation Modes

| Mode | How to Activate | Behavior |
|---|---|---|
| Wake Phrase (Always Listening) | Say the wake phrase, then say a command | Listens continuously in the background. On detecting the wake phrase, signals readiness, then waits up to 7 seconds for a command. |
| Push to Talk (Button) | Tap the floating overlay pill | Activates immediately on tap. The pill turns green and plays a beep. Listens for a command and auto-stops after execution or a 10-second timeout. |

Push-to-Talk is recommended for VOSK — it avoids continuous background recording.

---

## Wake Phrases

| Language | Default Phrase |
|---|---|
| Ukrainian | "Привiт BYD" |
| English | "Hello BYD" |

Wake phrases are configurable in **Settings > Wake Phrases**. Punctuation is stripped automatically, so "Привiт, BYD" works the same as "Привiт BYD".

---

## 7-Second Command Window

After the wake phrase is recognized, you have 7 seconds to say a command. If the assistant responds (e.g., "unrecognized command"), the window is extended automatically. In Push-to-Talk mode, the timeout is 10 seconds.

---

## Voice Commands

36 commands across eight categories. Each works in both English and Ukrainian.

### Climate

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "turn on climate", "ac on", "climate on" | "ввiмкни клiмат", "включи клiмат", "увiмкни кондицiонер" | A/C on (Auto mode) |
| "turn off climate", "ac off", "climate off" | "вимкни клiмат", "виключи клiмат" | A/C off |
| "heat steering wheel", "steering heat on", "warm steering wheel" | "ввiмкни пiдiгрiв керма", "нагрiй кермо" | Steering wheel heat on |
| "steering heat off", "stop heating steering wheel" | "вимкни пiдiгрiв керма" | Steering wheel heat off |
| "set temperature [16–32]", "set driver temperature [16–32]" | "встанови температуру [16–32]", "постав [16–32] градусiв" | Set driver temperature (°C) |
| "set passenger temperature [16–32]" | "встанови температуру пасажира [16–32]" | Set passenger temperature (°C) |
| "heat driver seat", "warm my seat" | "нагрiй моє сидiння", "пiдiгрiв водiйського сидiння" | Driver seat heat on |
| "stop heating driver seat" | "вимкни пiдiгрiв водiйського сидiння" | Driver seat heat off |
| "heat passenger seat" | "нагрiй пасажирське сидiння" | Passenger seat heat on |
| "stop heating passenger seat" | "вимкни пiдiгрiв пасажирського сидiння" | Passenger seat heat off |
| "vent driver seat", "cool my seat" | "провiтри моє сидiння", "вентиляцiя водiйського сидiння" | Driver seat vent on |
| "stop venting driver seat" | "вимкни вентиляцiю водiйського сидiння" | Driver seat vent off |
| "vent passenger seat" | "провiтри пасажирське сидiння" | Passenger seat vent on |
| "stop venting passenger seat" | "вимкни вентиляцiю пасажирського сидiння" | Passenger seat vent off |

### Windows (All)

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "open windows", "open all windows", "windows down" | "вiдкрий вiкна", "опусти вiкна" | Open all 4 windows |
| "close windows", "close all windows", "windows up" | "закрий вiкна", "пiднiми вiкна" | Close all 4 windows |

### Windows (Individual)

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "open driver window", "open my window" | "вiдкрий водiйське вiкно", "вiдкрий моє вiкно" | Open driver window |
| "close driver window", "close my window" | "закрий водiйське вiкно", "закрий моє вiкно" | Close driver window |
| "open passenger window" | "вiдкрий пасажирське вiкно" | Open passenger window |
| "close passenger window" | "закрий пасажирське вiкно" | Close passenger window |
| "open rear left window" | "вiдкрий заднє лiве вiкно" | Open rear-left window |
| "close rear left window" | "закрий заднє лiве вiкно" | Close rear-left window |
| "open rear right window" | "вiдкрий заднє праве вiкно" | Open rear-right window |
| "close rear right window" | "закрий заднє праве вiкно" | Close rear-right window |

### Sunroof

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "open sunroof", "open panorama" | "вiдкрий люк", "вiдкрий панораму" | Open sunroof |
| "close sunroof", "close panorama" | "закрий люк", "закрий панораму" | Close sunroof |
| "tilt sunroof", "vent sunroof", "crack sunroof" | "нахили люк", "провiтри", "вiдкрий люк трiшки" | Tilt to vent position |

### Sunshade

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "open sunshade", "open shade", "open curtain" | "вiдкрий шторку", "вiдкрий штору" | Open sunshade |
| "close sunshade", "close shade", "close curtain" | "закрий шторку", "закрий штору" | Close sunshade |

### Door Locks

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "lock doors", "lock car" | "закрий дверi", "замкни машину", "заблокуй дверi" | Lock all doors |
| "unlock doors", "unlock car" | "вiдкрий дверi", "вiдiмкни машину", "розблокуй дверi" | Unlock all doors |

### Trunk

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "open trunk", "open boot" | "вiдкрий багажник" | Open trunk |
| "close trunk", "close boot" | "закрий багажник" | Close trunk |

### App Launch *(since 1.0.2)*

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "launch navigation", "open navigation", "navigate", "open maps" | "вiдкрий навiгацiю", "запусти навiгацiю", "навiгацiя" | Launch the default navigation app |
| "launch music", "open music", "play music" | "вiдкрий музику", "запусти музику", "грай музику" | Launch the default music app and start playback |

> [!NOTE]
> App launch commands require a default navigation or music app to be configured in **Settings > Default Navigation** / **Default Music**.

---

## Disabling Commands

Individual voice commands can be disabled from **Settings → Voice Assistant → Commands**. Each command has a toggle switch — switching it off removes the command from recognition entirely. Disabled commands are shown grayed out and are not matched even if the phrase is spoken.

This is useful for commands you never use (e.g., "launch music" if no music app is configured) to reduce accidental matches.

Changes take effect immediately — no need to restart the voice assistant.

---

## Confirmation Response

After each recognized command, the assistant shows (and speaks, if ElevenLabs is active) a confirmation.

| Name configured? | English example | Ukrainian example |
|---|---|---|
| Yes (e.g., "Anton") | "Hi Anton, turning on climate" | "Привiт, Anton, вмикаю клiмат" |
| No | "Turning on climate" | "Вмикаю клiмат" |

> [!NOTE]
> With the **VOSK** backend, confirmations are shown as text only — there is no spoken response.

The name is configurable in **Settings > Your Name**.

---

## Unrecognized Command

If the assistant is listening but does not recognize a command:

- Shows (and speaks if ElevenLabs): "Command not recognized, please repeat" / "Не зрозумiв команду, повторiть"
- In wake mode: extends the 7-second window
- In PTT mode: resets the 10-second timeout

---

## Recognition Language

| Setting | VOSK | ElevenLabs |
|---|---|---|
| Ukrainian only | Supported | Supported |
| English only | Supported | Supported |
| Both (auto-detect) | Not supported — falls back to app language | Supported |

Configure in **Settings > Recognition Language**.

---

## ElevenLabs TTS Voice

When using ElevenLabs, you can set a custom voice ID in **Settings > TTS Voice ID**. Default: George (`JBFqnCBsd6RMkjVDRZzb`).

---

## See Also

- [Quick Actions Overlay](09-quick-actions.md)
- [Climate](04-climate.md)
- [Settings](10-settings.md)
- [Home Assistant](15-home-assistant.md)

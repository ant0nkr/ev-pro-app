# Voice Assistant

BYD EV Pro includes a bilingual voice assistant that lets you control the vehicle with spoken commands in English or Ukrainian. Speech recognition and text-to-speech are powered by ElevenLabs cloud services.

---

## Requirements

| Requirement | Notes |
|---|---|
| Internet connection | Cloud API calls are required. No offline mode. |
| ElevenLabs API key | Free tier provides approximately 10 minutes/month of speech recognition. Get one at [elevenlabs.io](https://elevenlabs.io). |
| Microphone permission | Granted automatically on first app connection |

> [!NOTE]
> The voice assistant does not work without a valid ElevenLabs API key. Android system TTS is used as a fallback for spoken responses, but speech recognition always requires ElevenLabs.

---

## Setup

1. Obtain an ElevenLabs API key at [https://elevenlabs.io](https://elevenlabs.io). The free tier is sufficient for basic use.
2. Open the app and go to **Settings**.
3. Scroll to the **Voice Assistant** section.
4. Enter your key in the **ElevenLabs API Key** field.
5. Enable the **Voice Assistant** toggle.
6. Select an activation mode: **Always Listening** (wake phrase) or **Push to Talk** (button).

---

## Activation Modes

| Mode | How to Activate | Behavior |
|---|---|---|
| Wake Phrase (Always Listening) | Say the wake phrase, then say a command | Listens continuously in the background. On detecting the wake phrase, signals readiness with audio feedback, then waits up to 7 seconds for a command. |
| Push to Talk (Button) | Tap the floating overlay pill | Activates immediately on tap. The pill turns green and plays a beep. Listens for a command and auto-stops after execution or a 10-second timeout. |

Push-to-Talk mode is recommended when internet bandwidth is limited, as it avoids continuously processing background audio.

---

## Wake Phrases

| Language | Default Phrase | Also Recognized |
|---|---|---|
| Ukrainian | "Привiт BYD" | Various pronunciation variants are handled automatically |
| English | "Hello BYD" | "Hey BYD" |

Wake phrases are configurable in **Settings > Wake Phrases**. Punctuation (commas, periods, etc.) is stripped automatically before matching, so "Привiт, BYD" works the same as "Привiт BYD".

---

## 7-Second Command Window

After the wake phrase is recognized, you have 7 seconds to say your command. If the assistant speaks a response during this window (e.g., an "unrecognized command" message), the window is automatically extended so you don't have to re-trigger the wake phrase.

In Push-to-Talk mode, the timeout is 10 seconds.

---

## Voice Commands

26 commands are supported across six categories. Each command works in both English and Ukrainian.

### Climate

| English Phrases | Ukrainian Phrases | Action |
|---|---|---|
| "turn on climate", "ac on", "climate on" | "ввiмкни клiмат", "включи клiмат", "увiмкни кондицiонер" | A/C on (Auto mode) |
| "turn off climate", "ac off", "climate off" | "вимкни клiмат", "виключи клiмат" | A/C off |
| "heat steering wheel", "steering heat on", "warm steering wheel" | "ввiмкни пiдiгрiв керма", "нагрiй кермо" | Steering wheel heat on |
| "steering heat off", "stop heating steering wheel" | "вимкни пiдiгрiв керма" | Steering wheel heat off |

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

---

## TTS Confirmation

After each recognized command, the assistant speaks a confirmation in the detected language.

| Name configured? | English example | Ukrainian example |
|---|---|---|
| Yes (e.g., "Anton") | "Hi Anton, turning on climate" | "Привiт, Anton, вмикаю клiмат" |
| No | "Turning on climate" | "Вмикаю клiмат" |

The name is configurable in **Settings > Your Name**.

---

## Unrecognized Command

If the assistant is listening but does not recognize a command:

- Speaks: "Command not recognized, please repeat" / "Не зрозумiв команду, повторiть"
- In wake mode: extends the 7-second window
- In PTT mode: resets the 10-second timeout

---

## Recognition Language Setting

You can hint the speech recognition engine to expect a specific language, which improves accuracy.

| Setting | Behavior |
|---|---|
| Ukrainian only | Optimized for Ukrainian speech |
| English only | Optimized for English speech |
| Both (default) | Auto-detects language (slightly lower accuracy) |

Configure this in **Settings > Recognition Language**. Use "Both" only when you genuinely mix languages.

---

## Custom TTS Voice

By default, the assistant uses the "George" voice from ElevenLabs. You can enter any valid ElevenLabs voice ID in **Settings > TTS Voice ID** to use a different voice.

If ElevenLabs TTS fails (network error, quota exceeded), the assistant automatically falls back to Android system TTS.

---

## See Also

- [Quick Actions Overlay](09-quick-actions.md)
- [Climate](04-climate.md)
- [Settings](10-settings.md)

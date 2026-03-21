# BYD EV Pro

Android application for BYD DiLink head units providing real-time EV diagnostics, climate control, voice assistant, and programmable automation.

Runs directly on the head unit — no OBD adapter, no Bluetooth, no paired phone required. ADB access is required.

---

Android-додаток для головних пристроїв BYD DiLink з діагностикою електромобіля в реальному часі, клімат-контролем, голосовим помічником та програмованою автоматизацією.

Працює безпосередньо на головному пристрої — без OBD-адаптера, без Bluetooth, без підключеного телефону. Потрібен ADB-доступ.

## Features / Функції

### Free / Безкоштовно

- **Dashboard / Панель** — Real-time SOC, power flow, range, voltage, current, motor temps, cell voltage spread / SOC, потік енергії, запас ходу, напруга, струм, температури моторів, розкид комірок
- **Charging Tracking / Зарядка** — Automatic session detection with SOC, energy, duration, avg speed / Автоматичне відстеження сесій з SOC, енергією, тривалістю, середньою швидкістю
- **Trip History / Історія поїздок** — Per-ignition-cycle records: distance, energy, efficiency, avg speed / Записи по циклах запалення: відстань, енергія, ефективність, середня швидкість
- **Automation / Автоматизація** — IF/THEN rules triggered on vehicle state transitions; includes predefined winter/summer comfort rules / Правила ЯКЩО/ТОДІ при зміні стану авто; включає зимові/літні правила комфорту
- **Voice Assistant / Голосовий помічник** — 36 bilingual (EN/UK) offline voice commands via VOSK / 36 двомовних офлайн голосових команд через VOSK
- **Bluetooth** — *(Feature in development / Функція у розробці)*
- **Quick Actions Overlay / Швидкі дії** — Floating pill with one-tap climate and seat controls / Плаваюча кнопка з керуванням кліматом та сидіннями
- **Debug Control Panel / Панель налагодження** — Verify that vehicle commands reach the car and read back actual CAN values / Перевірка, що команди доходять до авто, зчитування фактичних значень CAN
- **Diagnostic Export / Діагностика** — Full diagnostic bundle for troubleshooting / Повний діагностичний пакет для аналізу

### Subscription (7-day free trial) / Підписка (7 днів безкоштовно)

- **Telegram Notifications / Telegram-сповіщення** — Automatic alerts for charging events, gun connection, trip summaries; bot registration with multi-user support / Автоматичні сповіщення про зарядку, підключення пістолета, підсумки поїздок; реєстрація бота з підтримкою кількох користувачів
- **Home Assistant Integration / Інтеграція з Home Assistant** — Push live vehicle sensors to HA via webhook; voice-triggered HA service calls; HACS custom component included / Передача датчиків авто в HA через webhook; голосові команди для сервісів HA; HACS-компонент включено
- **WiFi / 4G / Bluetooth Keep-Alive / Утримання WiFi / 4G / Bluetooth** — Automatically re-enables WiFi, mobile data, and Bluetooth after ignition off / Автоматично відновлює WiFi, мобільний інтернет та Bluetooth після вимкнення запалення
- **Remote Commands / Віддалене керування** — Execute vehicle commands remotely via Telegram bot / Виконання команд авто віддалено через Telegram-бот

Activate the trial from the **About** tab in the app. No payment required for the first 7 days.

Активуйте пробний період у вкладці **Про додаток**. Оплата не потрібна перші 7 днів.

## Supported Vehicles / Підтримувані автомобілі

Developed and tested on **BYD Song Plus EV 2025** (DiLink 5.0). Compatible with BYD vehicles running DiLink 3.0 through 6.0. See the compatibility table ([EN](documentation/en/12-compatibility.md) | [UA](documentation/ua/12-compatibility.md)) for the full list.

Розроблено та протестовано на **BYD Song Plus EV 2025** (DiLink 5.0). Сумісний з автомобілями BYD на DiLink 3.0–6.0. Повний список — у таблиці сумісності ([EN](documentation/en/12-compatibility.md) | [UA](documentation/ua/12-compatibility.md)).

## Documentation / Документація

- **[English](documentation/en/)** | **[Українська](documentation/ua/)**

| # | Guide (EN) | Guide (UA) | Description / Опис |
|---|---|---|---|
| 01 | [Overview](documentation/en/01-overview.md) | [Огляд](documentation/ua/01-overview.md) | App description, features / Опис додатку, функції |
| 02 | [Installation](documentation/en/02-installation.md) | [Встановлення](documentation/ua/02-installation.md) | Install, first launch / Встановлення, перший запуск |
| 03 | [Dashboard](documentation/en/03-dashboard.md) | [Панель](documentation/ua/03-dashboard.md) | SOC, power flow, range / SOC, потік енергії, запас ходу |
| 04 | [Climate](documentation/en/04-climate.md) | [Клімат](documentation/ua/04-climate.md) | AC, temperature, seats / Кондиціонер, температура, сидіння |
| 05 | [Charging](documentation/en/05-charging.md) | [Зарядка](documentation/ua/05-charging.md) | Session tracking / Відстеження сесій |
| 06 | [Trip History](documentation/en/06-trip-history.md) | [Поїздки](documentation/ua/06-trip-history.md) | Trip records / Записи поїздок |
| 07 | [Automation](documentation/en/07-automation.md) | [Автоматизація](documentation/ua/07-automation.md) | Rules, sensors, actions / Правила, датчики, дії |
| 08 | [Voice Assistant](documentation/en/08-voice-assistant.md) | [Голосовий асистент](documentation/ua/08-voice-assistant.md) | 36 commands, VOSK offline, PTT / 36 команд |
| 09 | [Quick Actions](documentation/en/09-quick-actions.md) | [Швидкі дії](documentation/ua/09-quick-actions.md) | Floating overlay / Плаваюча панель |
| 10 | [Settings](documentation/en/10-settings.md) | [Налаштування](documentation/ua/10-settings.md) | All settings / Усі налаштування |
| 11 | [Diagnostics](documentation/en/11-diagnostics.md) | [Діагностика](documentation/ua/11-diagnostics.md) | Log viewer, debug panel, export / Перегляд логів, панель налагодження, експорт |
| 12 | [Compatibility](documentation/en/12-compatibility.md) | [Сумісність](documentation/ua/12-compatibility.md) | Supported models / Підтримувані моделі |
| 13 | [Troubleshooting](documentation/en/13-troubleshooting.md) | [Вирішення проблем](documentation/ua/13-troubleshooting.md) | Common issues / Поширені проблеми |
| 14 | [Telegram](documentation/en/14-telegram.md) | [Telegram](documentation/ua/14-telegram.md) | Telegram bot integration / Інтеграція з Telegram-ботом |
| 15 | [Home Assistant](documentation/en/15-home-assistant.md) | [Home Assistant](documentation/ua/15-home-assistant.md) | HA webhook integration / Інтеграція з HA через webhook |

## Home Assistant (HACS)

A custom component is included in this repository for Home Assistant integration. To install:

1. Open HACS in Home Assistant
2. Go to Integrations → Custom repositories
3. Add `ant0nkr/ev-pro-app` with category **Integration**
4. Install **BYD EV Pro** and restart Home Assistant
5. Configure the webhook URL and access token in the integration settings

Requires an active subscription in the app.

---

Користувацький компонент для Home Assistant включено в цей репозиторій. Для встановлення:

1. Відкрийте HACS в Home Assistant
2. Перейдіть до Інтеграції → Користувацькі репозиторії
3. Додайте `ant0nkr/ev-pro-app` з категорією **Integration**
4. Встановіть **BYD EV Pro** та перезапустіть Home Assistant
5. Налаштуйте webhook URL та токен доступу в налаштуваннях інтеграції

Потребує активну підписку в додатку.

## Releases / Релізи

APK releases with release notes are published on the [GitHub Releases](https://github.com/ant0nkr/ev-pro-app/releases) page.

APK-релізи з нотатками публікуються на сторінці [GitHub Releases](https://github.com/ant0nkr/ev-pro-app/releases).

## Languages / Мови

English and Ukrainian. Language can be changed in Settings.

Англійська та українська. Мову можна змінити в Налаштуваннях.

## Author / Автор

Anton Kramskyi / Антон Крамський

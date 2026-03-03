# Installation

This guide covers installing BYD EV Pro on a BYD DiLink head unit.

---

## Prerequisites

- A BYD vehicle with DiLink 3.0, 4.0, 5.0, 5.1, or 6.0. See [Compatibility](12-compatibility.md) for confirmed models.
- ADB access enabled on the head unit.
- The APK file: `byd_ev_pro.apk` (approximately 19 MB).

---

## Step 1 — Enable ADB on the Head Unit

1. On the head unit, open **Settings > About**.
2. Tap **Build Number** seven times in quick succession. A toast message will confirm that Developer Options are unlocked.
3. Go to **Settings > Developer Options**.
4. Enable **USB debugging**.
5. Enable **ADB over network** (the exact label varies by firmware; it may also appear as "Wireless debugging" or "ADB via Wi-Fi").

> [!NOTE]
> On most BYD DiLink units, ADB is already available over TCP once the toggle is enabled. If the option is not visible, you may need to connect the head unit to a PC via USB first to enable TCP mode.

---

## Step 2 — Install the APK

**Option A — via ADB from a computer:**

Connect to the head unit from a computer with Android platform tools installed, then install the APK using `adb install`.

**Option B — via USB stick:**

1. Copy `byd_ev_pro.apk` to the root of a FAT32-formatted USB stick.
2. Insert the stick into the head unit's USB port.
3. Open the head unit's **File Manager**, navigate to the USB drive, and tap the APK to install it.
4. If prompted, allow installation from unknown sources.

---

## Step 3 — First Launch

1. Launch **BYD EV Pro** from the app drawer.
2. The app will attempt to connect automatically.
3. On the very first connection, the head unit may display an **"Allow USB debugging?"** dialog. Tap **Always allow from this computer**, then tap **OK**.

> [!NOTE]
> Trusting the app's connection key on the head unit is a one-time step. After this, the app will connect automatically on every launch.

Once the key is trusted, the connection status indicator in the app should turn green.

---

## Step 4 — Disable Self-Start Restriction (Important)

> [!WARNING]
> After every installation or update, BYD's system may add the app to the self-start restriction list. If this is not disabled, the head unit will kill the app in the background, causing it to disconnect mid-drive.

1. On the head unit, go to **Settings > Apps > Self-Start Management** (or similar, depending on your firmware).
2. Find **BYD EV Pro** in the list.
3. Make sure the **self-start restriction tick is disabled** (unchecked) — this allows the app to run in the background.

> [!NOTE]
> You must repeat this step after every app installation or update. BYD resets this setting automatically when an app is installed or updated.

---

## Step 5 — Permissions

After the first successful connection, the app automatically requests the necessary permissions:

| Permission | Purpose |
|---|---|
| Overlay (draw over other apps) | Required for the floating quick actions overlay |
| Microphone | Required for the voice assistant |

No manual action is normally required. If the overlay or voice assistant does not work after first launch, try reconnecting via the app's connection button.

---

## Verifying the Installation

Once installed and connected:

1. The status indicator at the top of the app should be **green**.
2. The Dashboard tab should show live SOC, voltage, and power values.
3. Swipe to the Climate tab and confirm controls respond to taps.

If any step fails, consult [Troubleshooting](13-troubleshooting.md).

---

## Uninstall

To uninstall, go to **Settings > Apps** on the head unit, find **BYD EV Pro**, and tap **Uninstall**. This removes the app and all its data.

---

## See Also

- [Compatibility](12-compatibility.md)
- [Troubleshooting](13-troubleshooting.md)

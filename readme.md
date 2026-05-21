<div align="center">

<img width="500" alt="Rovio Activation Script banner" src="banner.png" />
<br><br>
A collection of scripts that allow you to fully unlock Bad Piggies on your PC.

[![](https://img.shields.io/badge/python-3.2+-blue.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/fork%20of-PRO100KatYT%2FRovioActivationScript-orange)](https://github.com/PRO100KatYT/RovioActivationScript)

⚙️ [How does it work?](#%EF%B8%8F-how-does-it-work) •
🚀 [How to use it?](#-how-to-use-it) •
🐛 [Found a bug?](#-found-a-bug)

</div>

---

> **📌 Fork Notice**
> This is a fork of [PRO100KatYT/RovioActivationScript](https://github.com/PRO100KatYT/RovioActivationScript) by [@frostcalibr](https://github.com/frostcalibr).
> The original Python script was written for Windows only. This fork adds a **Linux/Wine** compatible version of the script as Option 2, allowing Linux users running Bad Piggies through Wine to activate the game without needing Windows or Fiddler.
> All credit for the original concept, research, and scripts goes to [PRO100KatYT](https://github.com/PRO100KatYT).

---

### ⚙️ How does it work?

In February 2024, the activation servers for full versions of several Rovio PC games, including Bad Piggies, were permanently shut down. When you attempt to enter an activation code in the game's activation window, the game still sends a request to the servers. However, due to the lack of response from the servers, the activation process fails.

This is where this script comes into play. The script intercepts requests to `cloud.rovio.com/drm/consumeKey/` URL, simulating a server response. It then forwards this simulated response to the game client. As a result, the game believes that the Rovio servers are operational, and the activation code you input is considered valid. Consequently, the game gets activated, allowing you to enjoy the full experience!

#### Without the script:
![bp-activated-no](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/ab114f8e-f49e-4092-9dc5-1ec2092ca8d5)

#### With the script:
![bp-activated-yes](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/31f55c2d-a198-4c51-9cef-0f6297788955)

> **Note:** The gifs above demonstrate the **Fiddler Script** method which runs in the background and allows you to activate the game directly through the in-game menu. If you choose the **Python Script** method, it's recommended to run it while the game is closed. The Python script generates the necessary activation file contents and the game will be activated the next time you launch it!

---

### 🚀 How to use it?

<details>
<summary><b>Click to expand the step-by-step activation guide</b></summary>
<br>

#### Option 1: Python Script — Windows (Recommended, works for all versions)
This script automatically generates the necessary configuration `Settings.xml` file with the activation data and saves it in the game data folder in AppData. This method works for all Bad Piggies versions on Windows.

1. Download and extract the `RovioActivationScript.py` file to any location on your Windows PC from this repository. [(Direct download link)](https://github.com/PRO100KatYT/RovioActivationScript/archive/refs/heads/main.zip)
2. Make sure you have [Python](https://www.python.org/downloads/) installed (tested on version 3.9 but should work on 3.2 or newer).
3. Close the game if it's open.
4. Run the downloaded script (e.g., by double-clicking it).
5. Once the script is finished with no errors, Bad Piggies should be activated!

<br>

#### Option 2: Python Script — Linux / Wine *(Added in this fork)*
This version of the script works on Linux for users running Bad Piggies through [Wine](https://www.winehq.org/). It generates the same `Settings.xml` file but writes it to the correct location inside your Wine prefix, using Linux-native commands to detect your MAC address.

**Requirements:**
- Python 3.2 or newer
- Wine with Bad Piggies installed (game executable should be at `~/.wine/drive_c/Program Files (x86)/Rovio Entertainment Ltd/Bad Piggies/BadPiggies.exe` or similar)
- `ip` command available (standard on most Linux distros)

**Steps:**

1. Download `RovioActivationScript_Wine.py` from this repository.
2. Close the game if it's running.
3. Open a terminal and run:
   ```bash
   python3 RovioActivationScript_Wine.py
   ```
4. If your Wine prefix is **not** the default `~/.wine` (e.g. you use Bottles or Lutris), set `WINEPREFIX` first:
   ```bash
   WINEPREFIX=~/.local/share/bottles/BadPiggies python3 RovioActivationScript_Wine.py
   ```
5. The script will print the detected MAC address and the path it wrote `Settings.xml` to. If there are no errors, launch Bad Piggies through Wine — it should be activated!

> **What's different from the Windows version?**
> - Uses `ip link show` instead of `getmac` to read MAC addresses.
> - Derives the `AppData/LocalLow` path from `$WINEPREFIX` (or `~/.wine` as default) instead of `%APPDATA%`.
> - Auto-scans `drive_c/users/` if your Wine username differs from your Linux username.

<br>

#### Option 3: Fiddler Script — Windows only (Alternative, works for v1.3.0+)
1. Download and Install [Fiddler Classic](https://www.telerik.com/download/fiddler) and open it.
2. If you get an `AppContainer Configuration` popup, click cancel.
3. Head to the `FiddlerScript` section.
4. If there is an `Introduction` script, remove it.
5. Paste the following script there and click on `Save Script`:

```javascript
import Fiddler;
// Script by PRO100KatYT
 
class Handlers
{
    static function OnBeforeRequest(oSession: Session) {
        if (oSession.fullUrl.Contains("cloud.rovio.com/drm/consumeKey/"))
        {
            oSession.utilCreateResponseAndBypassServer();
            oSession.responseCode = 200;
            oSession.oResponse.headers.HTTPResponseCode = 200;
            oSession.oResponse.headers.HTTPResponseStatus = "200 OK";
            oSession.utilSetResponseBody("status=1&msg=valid");
        }
    }
}
```

6. Go to Bad Piggies, input any code into the activation window, and confirm it.
7. Your Bad Piggies PC copy should be activated. You can now close Fiddler and play the game!

</details>

---

### 🐛 Found a bug?
Feel free to [open an issue](../../issues/new/choose) if you encounter any bugs or just have a question.

---

### 📜 Credits
- Original script and research: [PRO100KatYT](https://github.com/PRO100KatYT)
- Linux/Wine adaptation: [@frostcalibr](https://github.com/frostcalibr)
- Earlier Linux/Wine research: [j-romchain](https://github.com/PRO100KatYT/RovioActivationScript/issues/1)

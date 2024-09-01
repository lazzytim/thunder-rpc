<img src="https://raw.githubusercontent.com/timothydeletrez/thunder-rpc/main/banner.png" align="right" width="180px">

![GitHub License](https://img.shields.io/github/license/timothydeletrez/thunder-rpc?style=for-the-badge&color=blue)
![Version](https://img.shields.io/github/v/release/timothydeletrez/thunder-rpc?style=for-the-badge&color=yellow&label=LAST%20VERSION)
![Python](https://img.shields.io/badge/PYTHON-3.12.1-4584b6.svg?style=for-the-badge)

ThunderRPC is a portable software made in Python using PyPresence Lib. that allow you to send RichPresence using a `Client ID`.
To make it work you'll need to fill all the field!, if a field is not filled, it won't work (maybe a error popup for later, I'll see!).

Have an amazing day, and have fun!

---

### 📑 Python Libraries

ThunderRPC use <a href="https://pypi.org/project/pypresence/">PyPresence</a> to make the RPC work and <a href="https://pypi.org/project/customtkinter/0.3/">CTk</a> to make the app window.
From v1.3, ThunderRPC also use [pystray](https://pypi.org/project/pystray/) to make a system tray icon and minimize window instead of closing it!

---

### 🦠 Found a bug ?

You found a bug or an issues with the code and you want to help ?, go to the issues section and create an new issues!

---

### ✏️ Last change log

Version: v2.0

- Added buttons feature
- Added tabs to GUI
- Completly reworked interface

---

### 🔎 Frequantly asked question

#### ⚡ ***ThunderRPC doesn't launch ?***

Sometimes the windows security anti-virus detect ThunderRPC as a `Trojan`.
No worry, it is a false positive.

To fix it, go into the Windows Security Panel and go into `Protection History`, click on the last one (check if it is ThunderRPC!) and select on `ALLOW`.

#### ⚡ ***My custom rpc doesn't disappear when I closed the app ?***

Sometimes it happen, to repair it, open your task manager (<kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Esc</kbd>) and search for `ThunderRPC Reworked vx.x`, right-click on it and choose `End Task`. It should repair your problem.
If not you may forgot to close it into your system tray icon.

#### ⚡ ***The RPC isn't showing on my Discord profile, why ?***

It may be multiple reason but here's the 2 most popular:

1. You Client ID isn't correct. To rectify that, go to your discord app on the developer portal and copy the `Application ID`, (NOT THE BOT TOKEN!), then paste it into the `Client ID` field and make sure all the other field are filled!

2. You send too much request to the Discord API, to rectify this, just create a new application and use this one instead!

---

### ❔ How to use

1. First, you'll need to download the latest version of ThunderRPC. For this, go into the release page.
2. Launch the executable, windows will maybe detect it as a threat, if so, go into the Windows Security Panel and create an exception for ThunderRPC.
3. After launch, select the feature that you want and click on `CONNECT`. Your custom rich presence is now available!

---

### 🏓 Icons

From the v2.0 update, ThunderRPC started using [Google Fonts' Icons](https://fonts.google.com/icons?icon.set=Material+Icons)!

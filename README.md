# ⌨️ KeySprint

**KeySprint** is a sleek and lightweight Python-based typing speed tester designed to challenge your accuracy and speed under pressure. Whether you're a casual typist or someone brushing up on professional typing skills, KeySprint makes practice both fun and productive.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/gui-tkinter-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- ⚡ Two difficulty levels: **Easy** (short phrases) & **Hard** (punctuated paragraphs)
- 🟥 Real-time **mistake highlighting** in red
- ⏳ Timed test sessions:
  - Easy: 40 seconds
  - Hard: 60 seconds
- ✅ Submit early with a simple click
- 📊 Live WPM (Words Per Minute) and Accuracy calculations
- 🌙 Dark mode UI for comfortable typing


---

## 🚀 Getting Started

### 📦 Requirements

- Python 3.6+
- No additional modules required (only built-in `tkinter`, `time`, `random`)

### 🧰 Installation

Clone the repository and navigate to the folder:

```bash
git clone https://github.com/pvk-96/KeySprint.git
cd keysprint
```

### Run the Application
```bash
python KeySprint.py
```
---

### 🧠 How It Works
- Choose your difficulty level.
- Read the displayed prompt and start typing!
- Your timer will begin once you start.
- Submit anytime or let the timer end.
- Get instant feedback on speed and accuracy.

--- 

### ✍️ Customization
You can easily update or expand the typing passages in the code. Look for this block:
```bash
passages = {
    "Easy": [(For easy)]
    "Hard": [(For Hard)]
```
Feel free to add your own phrases or even connect to APIs like Wikipedia for random paragraphs!
---

### 🛑 Exit the App
Simply close the window or press Ctrl + C in the terminal if running manually.
---
### 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

---

### 💬 Feedback
Enjoying KeySprint or want new features?
Drop a star ⭐ and leave your thoughts in the Issues tab.
---

Let me know if you want:
- A version with badges from GitHub Actions
- Setup as a `.exe` or `.deb` app
- Translations or themes (e.g. light/dark toggle)

Ready to ship 🚀

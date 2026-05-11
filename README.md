# 🎯 RandomPick: The Smart Selector

**RandomPick** is a Python-powered utility designed to help you make decisions quickly. Whether you're picking a lucky winner from a list of names or choosing a random number for a game, RandomPick handles the logic so you don't have to.

---

## 🚀 The Vision

This project is part of our **Graduation Project Prep**. We are transitioning from a simple console-based Python script to a fully functional **Android Application** using the **Flet** framework.

### ✨ Core Features

* 🎲 **Multi-Type Selection:** Input names, numbers, or items.
* 🔢 **Custom Count:** Choose how many results you want to see.
* 📱 **Cross-Platform:** Built in Python, running on Android.
* 🎨 **Clean UI:** Simple Material Design interface.

---

## 🧰 The Developer Toolbox

| Category | Tool | Purpose |
| --- | --- | --- |
| **Language** | 🐍 `Python 3.10+` | Core logic and backend |
| **UI Framework** | 🎨 `Flet` | Building the Android interface |
| **Version Control** | 🐙 `Git / GitHub` | Team collaboration & tracking |
| **Deployment** | 📦 `Buildozer` | Converting code to `.apk` |
| **Environment** | 🐧 `Ubuntu/Linux` | Standard development OS |

---

## 📁 Project Structure

```bash
random-selector-app/
├── console_app.py          # 📟 Terminal version for testing
├── core/                   # 🧠 Core logic (The "Brain")
│   └── logic_selector.py
├── data/                   # 📂 History and logs
├── main.py                 # 📱 UI and Android assets
├── Mobile UI Development Phase.pdf
└── README.md

```

---

## 🤝 Team Collaboration Workflow

Welcome to the team! If this is your first time using Git, follow these steps to fix bugs or add features.

### 🛠️ 1. Setup

```bash
# Clone the repository
git clone https://github.com/Ibraheem-Al-hafith/random-selector-app.git

# Install dependencies
uv sync

```

### 1.2. Pull: pull the latest updates to your local machine.

```bash
git pull origin ui

uv sync
```

### 🐛 2. Fixing the "Broken" Code

Look for `# TODO` or `# BUG` tags in `core/selector_logic.py`.

1. Open the file and fix the logic.
2. Test it using `uv run console_app.py`.
3. **Commit your fix:**

```bash
git add .
git commit -m "Fix: selection logic now handles empty inputs"
git push origin main

```

### 🌿 3. Adding New Features (Branching)

Never work directly on the `main` branch for new features!

1. **Create a branch:** `git checkout -b feat-your-feature-name`
2. **Build your feature.**
3. **Push the branch:** `git push origin feat-your-feature-name`
4. **Open a Pull Request (PR)** on GitHub for the team lead to review.

---

### 4. How to run a file? (e.g. `main.py`)
**Simply run: `uv run main.py`**

---

## 🗺️ Roadmap

* ✅ 🏗️ Initial project structure
* ✅ 🛠️ Fix broken selection logic
* [ ] 📱 Build the basic Android UI
* [ ] ⚠️ Add input validation (No empty lists!)
* [ ] 💾 Implement "Save History" feature
* [ ] 🤖 Export final APK for Android

---

## 👥 The Team

* **Khalid Rabea**
* **Ruaa Hassan**
* **Ibrahim Al Hafiz**


### 🛠️ Tasks to Assign on GitHub:

1.  **Khalid Rabea:** Fix the **Button Connection**. Currently, `on_click` is `None`. They need to point it to `pick_clicked`.
2.  **Ruaa Hassan:** Fix the **UI Update Bug**. The `result_text.value` changes in code, but the user doesn't see it because `page.update()` is missing at the end of the function.
3.  **Ibrahim:** Fix the **Logic Flow**. They must call `selector.add_options(options_input.value)` before calling `select_items`, otherwise the list will be empty!

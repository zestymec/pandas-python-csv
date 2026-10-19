<div align="center">

# 🐼 Pandas, CSV & Tkinter — Python Learning Journey

**Working with data files, comprehensions, and building desktop GUIs in Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6F00?style=for-the-badge)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-2E7D32?style=for-the-badge)

![Progress](https://img.shields.io/badge/Current-Day%2027-e7305b?style=flat-square)
![Lessons](https://img.shields.io/badge/Lessons%20done-215-9bdeac?style=flat-square)

</div>

---

## 📖 Table of Contents

- [What I Learned](#-what-i-learned)
- [Projects](#-projects)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)

---

## 🧠 What I Learned

### 📅 Day 25 — Working with CSV Data & Pandas

- Reading data files with Python's built-in `csv` library
- Getting started with **pandas**: `read_csv()`
- **Series** vs **DataFrame**, and converting between them
- Statistics: mean, **median**, **mode** and more
- Selecting and filtering **rows**, **columns** and series
- Building a DataFrame from scratch and saving it to CSV
- Handling large files (e.g. the 2018 Central Park Squirrel Census)

### 📅 Day 26 — List & Dictionary Comprehensions

- Python sequences (lists, strings, ranges, tuples)
- **List comprehension**: `[new_item for item in list if condition]`
- **Dictionary comprehension**: `{key: value for (key, value) in dict.items()}`
- Looping over DataFrames with `iterrows()`
- Intro to the **NATO phonetic alphabet** and building the NATO project

### 📅 Day 27 — Tkinter, `*args` & `**kwargs`

- **Tkinter**, Python's built-in GUI library
- Widgets: `Label`, `Button`, `Entry`, `Text`, `Spinbox`, `Scale`, `Checkbutton`, `Radiobutton`, `Listbox`
- Advanced function arguments:
  - Default arguments
  - `*args`: any number of positional arguments
  - `**kwargs`: any number of keyword arguments
- Layout managers: `pack()`, `place()` and `grid()`
- Building a **Miles → Km converter**

### 📅 Day 28 — Pomodoro App *(in progress)* 🍅

- Putting an image into a program with `PhotoImage`
- The **Canvas** widget: layering images and text
- Event-driven programming

---

## 🚀 Projects

| Project | Description | Concepts |
|:--|:--|:--|
| 🇺🇸 [**U.S. States Game**](us_states_game/) | Guess all 50 states on a map; missing states are saved to CSV when you exit | `turtle`, `pandas`, CSV |
| 📻 [**NATO Alphabet**](NATO_Alphabet_project/) | Type a word and get its NATO phonetic spelling | dict comprehension, `iterrows()` |
| 📏 [**Miles → Km Converter**](day_27/miles_to_km_converter.py) | A small GUI unit converter | `tkinter`, `grid()` |
| 🍅 [**Pomodoro Timer**](pomodoro_app/) | A focus timer with a tomato UI *(work in progress)* | `tkinter`, `Canvas`, `PhotoImage` |

---

## 🗂 Repository Structure

```
pandas-python-csv/
├── 📂 day_26/                  # List & dictionary comprehension practice
├── 📂 day_27/                  # Tkinter widgets, *args/**kwargs, converter
├── 📂 NATO_Alphabet_project/   # NATO phonetic alphabet project
├── 📂 pomodoro_app/            # Pomodoro timer (Tkinter + Canvas)
├── 📂 us_states_game/          # U.S. States guessing game (Turtle)
├── 📄 main.py                  # Pandas & CSV experiments
├── 📊 weather_data.csv         # Sample weather dataset
├── 📊 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
└── 📄 requirements.txt
```

---

## ⚙️ Getting Started

```bash
# Clone the repo
git clone https://github.com/zestymec/pandas-python-csv.git
cd pandas-python-csv

# Install dependencies
pip install -r requirements.txt   # or: pip install pandas

# Run a project
python NATO_Alphabet_project/main.py
python us_states_game/main.py
python pomodoro_app/main.py
```

> 💡 `tkinter` and `turtle` ship with Python. On Linux you may need `sudo apt install python3-tk`.

---

<div align="center">

⭐ **Learning in public, one day at a time.** ⭐

Made with ❤️ by **Umer**

</div>




216 5.46
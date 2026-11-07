<div align="center">

# 🐼 Pandas, CSV & Tkinter — Python Learning Journey

**Working with data files, comprehensions, and building desktop GUIs in Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6F00?style=for-the-badge)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-2E7D32?style=for-the-badge)

![Progress](https://img.shields.io/badge/Current-Day%2030-e7305b?style=flat-square)
![Lessons](https://img.shields.io/badge/Videos%20completed-226-9bdeac?style=flat-square)

</div>

---

## 📖 Table of Contents

- [What I Learned](#-what-i-learned)
- [Projects](#-projects)
- [Password Manager](#-password-manager)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Learning Progress](#-learning-progress)

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

### 📅 Day 28 — Pomodoro App 🍅

- Putting an image into a program with `PhotoImage`
- The **Canvas** widget: layering images and text
- Event-driven programming

### 📅 Day 29 — Password Manager Foundations 🔐

- Building a multi-field Tkinter form
- Using callbacks with buttons
- Validating user input with `messagebox`
- Generating 16-character passwords with Python's `secrets` module
- Copying generated passwords to the clipboard
- Designing a polished dark-mode desktop interface

### 📅 Day 30 — Errors, Exceptions & JSON *(in progress)* 🧩

- Understanding errors and exception handling
- Saving structured application data as JSON
- Improving the Password Manager experience and reliability

---

## 🚀 Projects

| Project | Description | Concepts |
|:--|:--|:--|
| 🇺🇸 [**U.S. States Game**](us_states_game/) | Guess all 50 states on a map; missing states are saved to CSV when you exit | `turtle`, `pandas`, CSV |
| 📻 [**NATO Alphabet**](NATO_Alphabet_project/) | Type a word and get its NATO phonetic spelling | dict comprehension, `iterrows()` |
| 📏 [**Miles → Km Converter**](day_27/miles_to_km_converter.py) | A small GUI unit converter | `tkinter`, `grid()` |
| 🍅 [**Pomodoro Timer**](pomodoro_app/) | A focus timer with a tomato UI | `tkinter`, `Canvas`, `PhotoImage` |
| 🔐 [**Vault Password Manager**](password-manager/) | A focused desktop vault for generating, copying and saving credentials | `tkinter`, `ttk`, `secrets`, file handling |

---

## 🔐 Password Manager

The Password Manager is a compact desktop vault built with Python and Tkinter. Its redesigned interface uses a dark, card-based layout to keep credential entry focused and easy to scan.

### Features

- Secure 16-character password generation using `secrets`
- Show and hide password visibility on demand
- One-click clipboard copying
- Website, username and password validation
- Confirmation before credentials are saved
- Clear success and error feedback inside the app
- Credentials stored in the project's local `password-manager/data.txt` file
- File paths resolved relative to the application, so it can be launched from any directory

### Run it

```bash
python password-manager/main.py
```

The first launch creates `password-manager/data.txt` when the first credential is saved. The local data file contains credentials in plain text, so keep it private and do not commit it to a public repository.

---

## 🗂 Repository Structure

```
pandas-python-csv/
├── 📂 day_26/                  # List & dictionary comprehension practice
├── 📂 day_27/                  # Tkinter widgets, *args/**kwargs, converter
├── 📂 NATO_Alphabet_project/   # NATO phonetic alphabet project
├── 📂 pomodoro_app/            # Pomodoro timer (Tkinter + Canvas)
├── 📂 password-manager/        # Vault password manager, logo and local data
├── 📂 us_states_game/          # U.S. States guessing game (Turtle)
├── 📄 main.py                  # Pandas & CSV experiments
├── 📊 weather_data.csv         # Sample weather dataset
├── 📊 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
└── 📄 requirements.txt
```

---

## ⚙️ Getting Started

```bash
git clone https://github.com/zestymec/pandas-python-csv.git
cd pandas-python-csv

pip install -r requirements.txt

python NATO_Alphabet_project/main.py
python us_states_game/main.py
python pomodoro_app/main.py
python password-manager/main.py
```

> 💡 `tkinter` and `turtle` ship with Python. On Linux you may need `sudo apt install python3-tk`.

---

## 📈 Learning Progress

- **Current milestone:** Day 30
- **Completed lessons:** Day 28 and Day 29
- **Course videos completed:** 226
- **Current focus:** Error handling, exceptions and JSON data storage
- **Learning style:** Building practical projects while learning Python fundamentals

---

<div align="center">

⭐ **Learning in public, one day at a time.** ⭐

Made with ❤️ by **Umer**
</div>



key err
index err
catching expection

try 
excpet
else
finally
raise err

video 230 done 
write read and update json(javascript object notation) data 
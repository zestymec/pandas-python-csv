<div align="center">

# Python Portfolio: Data, APIs, Automation and Desktop Apps

### A hands-on collection of Python projects covering pandas, CSV processing, REST APIs, Tkinter GUIs, automation, JSON storage and third-party integrations.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-Desktop%20GUI-FF6F00?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![REST APIs](https://img.shields.io/badge/REST-API%20Integration-009688?style=for-the-badge)](https://restfulapi.net/)
[![Learning](https://img.shields.io/badge/Status-Active%20Learning-e7305b?style=for-the-badge)](https://github.com/zestymec/pandas-python-csv)

[Projects](#featured-projects) • [Skills](#skills-demonstrated) • [Getting Started](#getting-started) • [Repository Structure](#repository-structure) • [Security](#security-notes)

</div>

---

## About This Repository

This repository is a practical Python learning portfolio built while progressing through applied programming projects. It demonstrates how Python can be used for data analysis, desktop application development, file management, API integration, email automation, cloud-style scheduled workflows and secure configuration handling.

The project collection emphasizes:

- Writing clear, reusable Python functions
- Reading and filtering CSV data with Pandas
- Building desktop interfaces with Tkinter and Turtle
- Handling exceptions and invalid input
- Working with JSON, TXT and CSV files
- Consuming REST APIs and processing HTTP responses
- Managing API keys and credentials with environment variables
- Sending automated email notifications
- Applying authentication, POST, PUT and DELETE concepts
- Building terminal and GUI applications from requirements

---

## Featured Projects

### Password Manager

[![Project](https://img.shields.io/badge/Project-Password%20Manager-305291?style=flat-square)](password-manager/)

A desktop credential manager built with Python, Tkinter and JSON. It includes password generation, clipboard support, credential search, visibility controls, input validation and a custom dark-themed interface.

- Generates strong 16-character passwords using Python's `secrets` module
- Saves and searches website credentials in a local JSON file
- Uses Tkinter/ttk widgets and native confirmation dialogs
- Resolves file paths relative to the application
- Handles missing files and malformed JSON gracefully

**Technologies:** Python, Tkinter, ttk, JSON, `secrets`, exception handling

### U.S. States Quiz

[![Project](https://img.shields.io/badge/Project-U.S.%20States%20Game-3776AB?style=flat-square)](us_states_game/)

A Turtle-based geography game that places correctly guessed states on a map and exports missed states to a CSV file.

**Technologies:** Python, Turtle, Pandas, CSV

### Stock News Monitoring

[![Project](https://img.shields.io/badge/Project-Stock%20News%20Monitoring-009688?style=flat-square)](stock-News-Monitoring-Project/)

Monitors stock-price changes through Alpha Vantage, retrieves relevant articles from NewsAPI and sends an email summary when the configured market-change threshold is met.

**Technologies:** Python, REST APIs, HTTP requests, SMTP, environment variables

### Automated Birthday Wisher

[![Project](https://img.shields.io/badge/Project-Birthday%20Wisher-e7305b?style=flat-square)](Auto-bd-wisher/)

Compares birthday records with the current date and sends a personalized email using locally stored templates and CSV data.

**Technologies:** Python, Pandas, SMTP, datetime, CSV, email templates

### Quizzler App

[![Project](https://img.shields.io/badge/Project-Quizzler-375362?style=flat-square)](quizzler-app/)

A class-based Tkinter trivia application that retrieves questions from an API and presents a scored, interactive quiz.

**Technologies:** Python, Tkinter, REST API, OOP, type hints, HTML entity handling

---

## Project Index

| Project | Description | Core Concepts |
|:--|:--|:--|
| [Password Manager](password-manager/) | Generate, copy, save and search credentials in a desktop interface | Tkinter, JSON, `secrets`, validation |
| [U.S. States Game](us_states_game/) | Guess U.S. states and place them on a Turtle map | Turtle, Pandas, CSV |
| [NATO Alphabet](NATO_Alphabet_project/) | Convert words into their NATO phonetic alphabet | Pandas, dictionary comprehension |
| [Pomodoro Timer](pomodoro_app/) | Desktop focus timer with an image-based interface | Tkinter, Canvas, event-driven UI |
| [Miles to Kilometers](day_27/miles_to_km_converter.py) | Convert miles to kilometers in a Tkinter GUI | Tkinter, widgets, `grid()` |
| [Kanye Quote App](kanye-quotes-end/) | Display random quotes returned by a public API | REST API, Tkinter |
| [Trivia Quiz](quizzler-app/) | Quiz application using the Open Trivia API | Tkinter, OOP, API requests |
| [Weather Alert](sms-sender/) | Check forecast conditions and send an email alert | OpenWeather API, SMTP, dotenv |
| [Stock News Monitor](stock-News-Monitoring-Project/) | Monitor stock movement and email relevant news | Alpha Vantage, NewsAPI, SMTP |
| [Birthday Wisher](Auto-bd-wisher/) | Automate date-based birthday emails | datetime, CSV, Pandas, SMTP |
| [Habit Tracker](Habit-tracker/) | Practice creating and updating pixels through Pixela | HTTP POST, REST authentication |
| [Japanese Flash Cards](capstone_projet/) | Learn vocabulary using a Tkinter flash-card interface | Tkinter, Pandas, CSV |
| [ISS Overhead](Solution+-+issoverhead-end/) | Detect ISS visibility and nighttime conditions | REST APIs, SMTP, scheduling |
| [Sunrise/Sunset API](day-33/) | Retrieve and process sunrise and sunset data | API parameters, JSON, datetime |
| [Pandas Practice](main_foolder/) | Explore weather and squirrel census datasets | Pandas, filtering, statistics |

---

## Skills Demonstrated

### Python Fundamentals

- Variables, control flow and functions
- List and dictionary comprehensions
- Object-oriented programming
- File and exception handling
- Type hints and class-based application structure
- Unit conversion and date/time calculations

### Data and File Processing

- CSV reading, filtering and exporting with Pandas
- DataFrame and Series operations
- Working with JSON using `json.load()` and `json.dump()`
- Building datasets and saving processed results
- Managing application data with relative file paths

### Desktop and GUI Development

- Tkinter widgets and layout managers
- Turtle graphics
- Canvas-based interfaces
- Event-driven programming
- Input validation and native dialogs
- Reusable UI components

### APIs and Integrations

- REST API requests with `requests`
- API query parameters and response status codes
- HTTP GET and POST operations
- API authentication concepts
- Alpha Vantage and NewsAPI integrations
- OpenWeather and Open Trivia API integrations
- SMTP email delivery

### Automation and Operations

- Scheduled scripts and repeated monitoring
- Environment variable configuration
- GitHub Actions concepts
- PythonAnywhere deployment concepts
- Secure handling of API keys and app passwords

---

## Getting Started

### Prerequisites

- Python 3.9 or later
- `pip`
- Tkinter support for GUI applications
- Internet access for projects that use external APIs

### Installation

```bash
git clone https://github.com/zestymec/pandas-python-csv.git
cd pandas-python-csv

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install pandas requests python-dotenv
```

On Linux, Tkinter may need to be installed through your system package manager:

```bash
sudo apt install python3-tk
```

---

## Run the Applications

```bash
# Password Manager
python password-manager/main.py

# U.S. States Game
python us_states_game/main.py

# NATO Alphabet
python NATO_Alphabet_project/main.py

# Pomodoro Timer
python pomodoro_app/main.py

# Trivia Quiz
python quizzler-app/main.py

# Miles to Kilometers
python day_27/miles_to_km_converter.py
```

Projects containing API or email integrations may require their own environment variables and dependencies.

For example:

```bash
python -m pip install -r stock-News-Monitoring-Project/requirements.txt
python -m pip install -r Auto-bd-wisher/requirements.txt
```

---

## Environment Configuration

Never commit real API keys, passwords or personal credentials.

Create a `.env` file based on the provided examples. For example:

```bash
cp stock-News-Monitoring-Project/.env.example \
   stock-News-Monitoring-Project/.env
```

The stock news project uses:

```env
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
MAIL_SENDER=your_email_address
MAIL_PASSWORD=your_app_password
MAIL_RECIPIENT=your_recipient_email
```

Additional projects may use `API_KEY`, `MAIL_SENDER`, `MAIL_PASSWORD` or `MAIL_RECIPIENT`. Review each project entry before running it.

---

## Repository Structure

```text
pandas-python-csv/
├── password-manager/                 # Tkinter credential manager
├── us_states_game/                   # Turtle map guessing game
├── NATO_Alphabet_project/            # NATO phonetic alphabet converter
├── pomodoro_app/                     # Pomodoro timer
├── quizzler-app/                     # API-powered trivia GUI
├── kanye-quotes-end/                 # Random quote API application
├── stock-News-Monitoring-Project/    # Stock and news email alerts
├── Auto-bd-wisher/                   # Automated birthday emails
├── Habit-tracker/                    # Pixela HTTP API practice
├── sms-sender/                       # Weather email alerts
├── capstone_projet/                  # Japanese flash-card application
├── Solution+-+issoverhead-end/       # ISS notification automation
├── day_26/                           # Comprehensions and Pandas practice
├── day_27/                           # Tkinter widgets and GUI practice
├── day_30/                           # Exceptions and file handling practice
├── day-33/                           # Sunrise/sunset API practice
├── main_foolder/                     # Pandas datasets and examples
└── readme.md
```

---

## Security Notes

- API keys and email passwords must be loaded from environment variables or local secret configuration.
- The password manager stores credentials locally in `password-manager/data.json` and is an educational project, not a replacement for a professional password vault.
- `data.json` does not encrypt stored credentials. Do not commit real usernames or passwords.
- A Gmail or Google Workspace account may require an app password instead of a normal account password.
- External API rate limits and service availability can affect project behavior.

---

## Learning Outcomes

This portfolio demonstrates progression across:

1. Python syntax and core programming concepts
2. Data analysis and CSV processing with Pandas
3. Tkinter and Turtle desktop application development
4. JSON persistence and exception handling
5. REST API consumption and authentication
6. SMTP email automation
7. Environment variable management
8. Scheduled and cloud-based script execution

---

## Future Improvements

- Add automated tests for core application logic
- Introduce a root-level dependency manifest
- Replace absolute image paths with project-relative paths
- Add encrypted storage to the password manager
- Improve API error handling and retry logic
- Add CI workflows for syntax and dependency checks
- Standardize project naming and folder structure
- Separate course exercises from production-style examples

---

## Author

**Umer Aziz**

Python learner and developer building practical projects in data analysis, desktop applications, API integration and automation.

- GitHub: [@zestymec](https://github.com/zestymec)

---

<div align="center">

⭐ If this repository helped you learn Python, consider giving it a star.

</div>


habits travcker use pixela 
285 done 
286 learned strftime and date and time usage advance
287 how to update and delet pixels , https requests 

day 37 done 
day 38 challenge project 
workout tracking using google sheet 
289 done apikey from https://app.100daysofpython.dev/
290 done figure out how to print the exercise stats for plain text input.
291 done and did this "Setup Your Google Sheet with Sheety"
292 done Saving Data into Google Sheets
293 Authenticate Your Sheety API to add barer token or authetication so no one other then me have tio access my sheet 
294 Environment Variables
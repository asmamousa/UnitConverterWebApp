# UnitConverterWebApp

A simple web application to convert values between different units of measurement — built as a solution to the **Unit Converter** project from [roadmap.sh](https://roadmap.sh/projects/unit-converter).

## 🚀 Project Overview

**UnitConverterWebApp** allows users to input a numerical value, select the unit to convert from and the unit to convert to, and instantly see the converted result in the browser.

Supported conversion categories include:
- 📏 Length (e.g., meters → miles)
- ⚖️ Weight (e.g., kilograms → pounds)
- 🌡️ Temperature (e.g., Celsius ↔ Fahrenheit)

This project focuses on practicing backend fundamentals with Django while building a simple, functional web interface.

---

## 📦 Features

- Convert values between multiple units
- Simple and clean user interface
- Django-based backend logic
- HTML forms for user input

---

## 🔧 Technologies Used

- **Python**
- **Django**
- **HTML / CSS**
- **pip & virtual environments**

---

## 📁 Getting Started

### Requirements

- Python 3.x
- pip

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/asmamousa/UnitConverterWebApp.git
cd UnitConverterWebApp
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://localhost:8000/
```

---

## 🧪 Usage

1. Enter the value you want to convert
2. Select the source unit
3. Select the target unit
4. Click **Convert** to see the result

---

## 📂 Project Structure

```
UnitConverterWebApp/
├── django_project/
├── unit_converter/
├── manage.py
├── requirements.txt
└── README.md
```

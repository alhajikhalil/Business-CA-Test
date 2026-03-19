# BizSpot — Local Business & Startup Directory

A Flask web application that allows users to view, add, and manage local businesses and startups in their community. Built for CSC 202 Continuous Assessment.

---

## What the App Does

BizSpot is a **Local Business Directory** that lets you:

- **Browse** all registered local businesses on the homepage
- **Filter** businesses by category (Food, Tech, Agriculture, etc.)
- **Add** a new business using a clean submission form
- **Remove** a business listing with one click
- **Undo** an accidental deletion using a Stack-powered undo feature
- **See** the 3 most recently added businesses in a sidebar ("Recently Added")
- **View** how long ago each business was added (e.g. "5 minutes ago")

---

## Technologies Used

- **Python 3** — backend logic and OOP models
- **Flask** — lightweight web framework for routing and templating
- **Jinja2** — HTML templating (built into Flask)
- **HTML/CSS** — frontend UI (no extra frameworks needed)
- **Python `datetime` module** — timestamping each business entry

---

## Project Structure

```
business_directory/
│
├── app.py          # Flask app — all routes and logic
├── models.py       # OOP classes: Business, BusinessDirectory
├── templates/
│   ├── index.html  # Home page (list + filter + sidebar)
│   └── add.html    # Add business form
└── README.md
```

---

## How to Run the App Locally

Follow these steps, even if you are new to Python:

### 1. Make sure Python is installed

Open your terminal and type:

```bash
python --version
```

You should see something like `Python 3.10.x`. If not, download Python from [python.org](https://www.python.org/downloads/).

### 2. Install Flask

In your terminal, run:

```bash
pip install flask
```

### 3. Navigate to the project folder

```bash
cd path/to/business_directory
```

### 4. Run the app

```bash
python app.py
```

You will see output like:

```
 * Running on http://127.0.0.1:5000
```

### 5. Open in your browser

Go to: **http://127.0.0.1:5000**

The app will be running! You can now browse, add, and delete businesses.

---

## Core Concepts Used (CSC 202)

| Concept | Where Used |
|---|---|
| OOP (Classes) | `models.py` — `Business` and `BusinessDirectory` classes with `__init__` and custom methods |
| Stack (LIFO) | `BusinessDirectory._undo_stack` — stores deleted businesses for undo |
| `datetime` API | `Business.timestamp` — records when each business is added |
| Flask Routes | `app.py` — `/`, `/add`, `/delete/<id>`, `/undo` |
| HTML Forms | `add.html` — submits data via POST to Flask backend |

---

## Author

CSC 202 Student — Built with Flask, Python OOP, and ❤️

# FitLog CLI

**FitLog** is a Python Command-Line Interface (CLI) application designed to help users stay motivated and consistent in their fitness journey. Users can sign up, log their daily activities, and track their progress through interactive challenges.

---

## **Features**
FitLog helps users stay consistent in their fitness journey through these key features:

- **User Login / Signup**: Users can create a new profile or log in with their name. Profiles are stored in the database for persistence.
- **Challenges**: Users can view existing challenges and add their own custom challenges.
- **Logs**: Users can record progress by adding notes to a specific challenge (e.g., “Day 5 – Completed 20 pushups”). Logs are tied to both the user and the challenge.
- **Progress Tracking**: Users can view their own logs, showing which challenge they attempted and any notes they added. This keeps each user’s data private while still allowing them to track their fitness journey over time.
- **Data Persistence**: All users, challenges, and logs are stored in a **SQLite** database using **SQLAlchemy ORM**, so data isn’t lost between sessions.
- **Interactive CLI Menu**: A simple text-based menu guides the user through all available actions (e.g., view challenges, add logs, exit the program).

---

## **Project Structure**

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py
```

---

## **Installation**

1. Clone the repository:

```
git clone https://github.com/your-username/Phase3-FitLog.git
cd Phase3-FitLog
```
2.  Create a virtual environment and install dependencies using Pipenv:
```
pipenv install
pipenv shell
```
3. Seed the database:
```
python -m lib.db.seed
```

---

## **Usage**
Run the CLI application:
```
python -m lib.cli
```
1. Login / Sign Up – Enter your name.
2. Main Menu – Choose options by typing the number:

- 1 – Add Challenges
- 2 – Delete Challenge
- 3 – Add Log
- 4 – View Logs
- 0 – Exit

All interactions are done in the terminal.
Users can only manage challenges if they’re logged in.

---

## **Technologies Used**
- Python 3
- SQLite for database
- SQLAlchemy ORM for object-relational mapping
- Pipenv for virtual environment and dependency management

---

## **Author**
Ashley Mararo
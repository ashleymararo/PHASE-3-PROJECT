# FitLog CLI

**FitLog** is a Python Command-Line Interface (CLI) application designed to help users stay motivated and consistent in their fitness journey. Users can sign up, log their daily activities, and track their progress through interactive challenges.

---

## **Features**

- User login and sign up
- View all users in the system
- View available fitness challenges
- Add logs for challenges with notes
- View all logs with user and challenge details
- Persistent data storage using **SQLite** with **SQLAlchemy ORM**

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

- 1 – View Users
- 2 – View Challenges
- 3 – Add Log
- 4 – View Logs
- 0 – Exit

All interactions are done in the terminal.

---

## **Technologies Used**
- Python 3
- SQLite for database
- SQLAlchemy ORM for object-relational mapping
- Pipenv for virtual environment and dependency management

---

## **Author**
Ashley Mararo
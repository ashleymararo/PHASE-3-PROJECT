# FitLog CLI

**FitLog** is a Python Command-Line Interface (CLI) application designed to help users stay motivated and consistent in their fitness journey. Users can sign up, log their daily activities, and track their progress through interactive challenges.

---

## **Features**
FitLog helps users stay consistent in their fitness journey through these key features:

- User login & auto sign-up
- View available fitness challenges
- Create new challenges
- Delete challenges (only if no logs exist)
- Log daily challenge activity
- View personal logs
- Edit existing logs
- Delete logs
- Persistent SQLite database
- Database migrations with Alembic
- Seeded starter data

---

## **Project Structure**

```
├── cli.py
├── fitlog.db
├── alembic.ini
├── migrations/
├── lib/
│ ├── db/
│ │ ├── models.py
│ │ └── seed.py
│ ├── helpers.py
│ └── init.py
├── Pipfile
├── Pipfile.lock
└── README.md
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
3. Run database migrations
```
alembic upgrade head
```
4. Seed the database
```
python lib/db/seed.py
```
5. Run the application
```
python cli.py
```

---

## **Usage**
1. Launch the app
2. Enter your name to log in or create user
3. View available challenges
4. Add logs to track your progress
5. Edit or delete logs anytime
6. Create or delete custom fitness challenges
7. Exit when done

All interactions are done in the terminal.
Users can only manage challenges if they’re logged in.

---

## **Database Models**
**User**
- id
- name
- has many logs

**Challenge**
- id
- title
- description
- has many logs

**Log**
- id
- user_id
- challenge_id
- notes

---

## **Technologies Used**
- Python 3
- SQLite for database
- SQLAlchemy ORM for object-relational mapping
- Pipenv for virtual environment and dependency management
- Alembic for database migrations

---

## **Author**
Ashley Mararo
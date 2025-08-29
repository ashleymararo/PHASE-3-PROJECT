from lib.helpers import print_header
from lib.db.models import session, User, Challenge, Log

from sqlalchemy import func

current_user = None

def login():
    global current_user
    print_header("Login / Sign Up")
    name = input("Enter your name: ").strip()

    user = session.query(User).filter(func.lower(User.name) == name.lower()).first()
    if user:
        print(f"✅ Welcome back, {user.name}!")
    else:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"✅ User '{name}' created and logged in!")

    current_user = user

def view_users():
    print_header("Users")
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    for u in users:
        print(f"{u.id}. {u.name}")

def view_challenges():
    print_header("Challenges")
    challenges = session.query(Challenge).all()
    if not challenges:
        print("No challenges yet.")
        return
    for c in challenges:
        print(f"{c.id}. {c.title} - {c.description}")

def add_log_cli():
    if not current_user:
        print("⚠️ You must log in first.")
        return

    print_header("Add Log")
    challenges = session.query(Challenge).all()
    if not challenges:
        print("No challenges to log.")
        return

    for c in challenges:
        print(f"{c.id}. {c.title}")
    choice = input("Enter challenge ID: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    choice = int(choice)

    challenge = session.query(Challenge).filter_by(id=choice).first()
    if not challenge:
        print("Challenge not found.")
        return

    notes = input("Enter notes for this log: ")
    log = Log(user_id=current_user.id, challenge_id=challenge.id, notes=notes)
    session.add(log)
    session.commit()
    print(f"✅ Log added for {current_user.name} on '{challenge.title}'")

def view_logs():
    print_header("Logs")
    logs = session.query(Log).all()
    if not logs:
        print("No logs yet.")
        return

    for log in logs:
        user = session.query(User).filter_by(id=log.user_id).first()
        challenge = session.query(Challenge).filter_by(id=log.challenge_id).first()
        print(f"{user.name} - {challenge.title}: {log.notes}")

def exit_program():
    print("👋 Goodbye!")
    exit()

menu_options = {
    "1": view_users,
    "2": view_challenges,
    "3": add_log_cli,
    "4": view_logs,
    "0": exit_program
}

def main_menu():
    login()

    while True:
        print_header("FitLog CLI Main Menu")
        print("""
1. View Users
2. View Challenges
3. Add Log
4. View Logs
0. Exit
""")
        choice = input("Choose an option: ").strip()
        action = menu_options.get(choice)
        if action:
            action()
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()

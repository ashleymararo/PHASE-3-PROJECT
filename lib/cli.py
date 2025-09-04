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
    print(f"👤 Current User: {current_user.name}")

def view_challenges():
    print_header("Challenges")
    challenges = session.query(Challenge).all()
    if not challenges:
        print("No challenges yet.")
        return
    for c in challenges:
        print(f"{c.id}. {c.title} - {c.description}")

def add_challenge():
    print_header("Add Challenge")
    title = input("Enter challenge title: ").strip()
    description = input("Enter challenge description: ").strip()
    if not title:
        print("⚠️ Title cannot be empty.")
        return

    exists = session.query(Challenge).filter(func.lower(Challenge.title) == title.lower()).first()
    if exists:
        print("⚠️ A challenge with this title already exists.")
        return

    challenge = Challenge(title=title, description=description)
    session.add(challenge)
    session.commit()
    print(f"✅ Challenge '{title}' added successfully!")

def delete_challenge():
    print_header("Delete Challenge")
    challenges = session.query(Challenge).all()
    if not challenges:
        print("No challenges available to delete.")
        return

    for c in challenges:
        print(f"{c.id}. {c.title}")

    choice = input("Enter challenge ID to delete: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    choice = int(choice)

    challenge = session.query(Challenge).filter_by(id=choice).first()
    if not challenge:
        print("Challenge not found.")
        return

    logs_exist = session.query(Log).filter_by(challenge_id=challenge.id).first()
    if logs_exist:
        print("⚠️ Cannot delete this challenge. Logs exist for it.")
        return

    session.delete(challenge)
    session.commit()
    print(f"✅ Challenge '{challenge.title}' deleted successfully!")

def add_log_cli():
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

    notes = input("Enter notes for this log: ").strip()
    log = Log(user_id=current_user.id, challenge_id=challenge.id, notes=notes)
    session.add(log)
    session.commit()
    print(f"✅ Log added for {current_user.name} on '{challenge.title}'")

def view_logs():
    print_header("Logs")
    logs = session.query(Log).filter_by(user_id=current_user.id).all()
    if not logs:
        print("No logs yet.")
        return

    for log in logs:
        challenge = session.query(Challenge).filter_by(id=log.challenge_id).first()
        print(f"{challenge.title}: {log.notes}")

def exit_program():
    print("👋 Goodbye!")
    exit()

menu_options = {
    "1": view_users,
    "2": view_challenges,
    "3": add_log_cli,
    "4": view_logs,
    "5": add_challenge,
    "6": delete_challenge,
    "0": exit_program
}

def main_menu():
    login()

    while True:
        print_header("FitLog CLI Main Menu")
        print("""
1. View Current User
2. View Challenges
3. Add Log
4. View My Logs
5. Add Challenge
6. Delete Challenge
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

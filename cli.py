from lib.db.models import session, User, Challenge, Log
from lib.helpers import print_header

from sqlalchemy import func

current_user = None

def login():
    global current_user
    print_header("Login / Sign Up")

    name = input("Enter your name: ").strip()

    if not name:
        print("⚠️ Name cannot be empty. Please enter a valid name.")
        return login()

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
    for u in users:
        print(f"{u.id}. {u.name}")

    print(f"\n👤 Current User: {current_user.name}")

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
    print_header("My Logs")
    logs = session.query(Log).filter_by(user_id=current_user.id).all()

    if not logs:
        print("No logs yet.")
        return

    for log in logs:
        print(f"{log.id}. {log.challenge.title} → {log.notes}")

def edit_log():
    print_header("Edit Log")

    logs = session.query(Log).filter_by(user_id=current_user.id).all()
    if not logs:
        print("No logs to edit.")
        return

    for log in logs:
        print(f"{log.id}. {log.challenge.title} → {log.notes}")

    choice = input("Enter Log ID to edit: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    log = session.query(Log).filter_by(id=int(choice), user_id=current_user.id).first()
    if not log:
        print("Log not found.")
        return

    new_notes = input("Enter new notes: ").strip()
    if not new_notes:
        print("⚠️ Notes cannot be empty.")
        return

    log.notes = new_notes
    session.commit()
    print("✅ Log updated successfully!")

def delete_log():
    print_header("Delete Log")

    logs = session.query(Log).filter_by(user_id=current_user.id).all()
    if not logs:
        print("No logs to delete.")
        return

    for log in logs:
        print(f"{log.id}. {log.challenge.title} → {log.notes}")

    choice = input("Enter Log ID to delete: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    log = session.query(Log).filter_by(id=int(choice), user_id=current_user.id).first()
    if not log:
        print("Log not found.")
        return

    session.delete(log)
    session.commit()
    print("✅ Log deleted successfully!")


def exit_program():
    print("👋 Goodbye!")
    exit()

menu_options = {
    "1": view_users,
    "2": view_challenges,
    "3": add_log_cli,
    "4": view_logs,
    "5": edit_log,
    "6": delete_log,
    "7": add_challenge,
    "8": delete_challenge,
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
5. Edit Log
6. Delete Log
7. Add Challenge
8. Delete Challenge
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

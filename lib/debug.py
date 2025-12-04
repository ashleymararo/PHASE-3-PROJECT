from lib.db.models import session, User, Challenge, Log

if __name__ == "__main__":
    users = session.query(User).all()
    print("Users:", users)

    challenges = session.query(Challenge).all()
    print("Challenges:", challenges)

    logs = session.query(Log).all()
    print("Logs:", logs)

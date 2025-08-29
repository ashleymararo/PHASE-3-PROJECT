from lib.db.models import session, User, Challenge

users = ["Ashley", "Michelle", "Carol"]
for name in users:
    if not session.query(User).filter(User.name == name).first():
        user = User(name=name)
        session.add(user)

challenges = [
    ("30-day Pushup Challenge", "Do pushups every day for 30 days"),
    ("5K Run", "Run 5 kilometers"),
    ("Yoga Month", "Do yoga every day for a month")
]
for title, desc in challenges:
    if not session.query(Challenge).filter(Challenge.title == title).first():
        challenge = Challenge(title=title, description=desc)
        session.add(challenge)

session.commit()
print("✅ Database seeded successfully!")

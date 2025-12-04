from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///fitlog.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    logs = relationship("Log", back_populates="user")

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    logs = relationship("Log", back_populates="challenge")

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    notes = Column(String)
    user = relationship("User", back_populates="logs")
    challenge = relationship("Challenge", back_populates="logs")


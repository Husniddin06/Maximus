from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    xp = Column(Integer, default=0)
    level = Column(String, default="Beginner") # Beginner, Advanced, Beast
    is_pro = Column(Boolean, default=False)
    
    # Relationship to progress
    progress = relationship("Progress", back_populates="user")

class Progress(Base):
    __tablename__ = 'progress'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(String)
    workout_completed = Column(Boolean, default=False)
    xp_gained = Column(Integer, default=0)
    
    user = relationship("User", back_populates="progress")

class Music(Base):
    __tablename__ = 'music'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String) # HARD, CHILL, FOCUS
    url = Column(String) # YouTube link or File ID
    is_premium = Column(Boolean, default=False)

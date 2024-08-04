from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  
    
    creators = relationship("Creator", back_populates="user")

class Creator(Base):
    __tablename__ = "creators"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    job_description = Column(String)
    genre = Column(String)
    sub_genre = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="creators")
    pricings = relationship("Pricing", back_populates="creator")

class Pricing(Base):
    __tablename__ = "pricing"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    delivery_time = Column(Integer)
    time_limit = Column(Float)
    content_form = Column(String)
    price = Column(Float)
    type = Column(String)  # New column
    creator_id = Column(Integer, ForeignKey("creators.id"))
    
    creator = relationship("Creator", back_populates="pricings")

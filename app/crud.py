from sqlalchemy.orm import Session
from . import models, schemas, auth

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not auth.verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)  # Hash the password
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_creator(db: Session, creator: schemas.CreatorCreate, user_id: int):
    db_creator = models.Creator(**creator.dict(), user_id=user_id)
    db.add(db_creator)
    db.commit()
    db.refresh(db_creator)
    return db_creator

def create_pricing(db: Session, pricing: schemas.PricingCreate, creator_id: int):
    db_pricing = models.Pricing(**pricing.dict(), creator_id=creator_id)
    db.add(db_pricing)
    db.commit()
    db.refresh(db_pricing)
    return db_pricing

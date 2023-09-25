from sqlalchemy.orm import Session
from app.db.schema import User
from datetime import datetime

def create_user(db: Session, username: str, data: datetime, role: str):
    user = User(username=username, data=data, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users_by_role(db: Session, role: str):
    return db.query(User).filter(User.role == role).all()

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, new_data: dict):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in new_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

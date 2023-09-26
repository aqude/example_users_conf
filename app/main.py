from fastapi import FastAPI, Depends, HTTPException
from app.db.crud import *
from sqlalchemy.orm import Session
from app.db.datebase import SessionLocal, engine, get_db
from datetime import datetime
app = FastAPI()
valid_roles = ["admin", "user", "moderator"]
@app.get("/users/get_users")
def __get_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users

@app.post("/users/create_user")
async def __create_user(username: str, role: str = "user", db: Session = Depends(get_db)):
    if role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Invalid role: {role}. Valid roles are {', '.join(valid_roles)}")

    addUser = create_user(db, username=username, data=datetime.now(), role=role)
    return addUser

@app.get("/users/{user_id}")
async def __get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/")
async def __get_users_by_role(role: str = "user", db: Session = Depends(get_db)):
    if role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Invalid role: {role}. Valid roles are {', '.join(valid_roles)}")
    
    users = get_users_by_role(db, role=role)
    return users
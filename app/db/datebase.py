from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from .schema import Base
DATABASE_URL = "sqlite:///./app/db/users.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базы данных и таблицы при первой инициализации
def init_db():
    if os.path.isfile(DATABASE_URL):
        pass
    else:
        Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
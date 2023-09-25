import app.main
from app.db.datebase import init_db

import uvicorn

if __name__ == "__main__":
    # Создание базы данных
    init_db()
    # Запуск проекта
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
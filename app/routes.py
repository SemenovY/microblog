"""
Маршрут на главную страницу
"""
from app import app
@app.route("/") # главная страница - / (без пути)
@app.route("/index") # главная страница - /index (по умолчанию)
def index(): return "Hello World! - это главная страница"

"""
модулю routes необходимо импортировать переменную app, определенную в этом файле,
поэтому размещение одного из взаимных импортов внизу позволяет избежать ошибки,
возникающей в результате взаимных ссылок между этими двумя файлами.
"""

from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # type: Flask
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Нижний импорт - это хорошо известное решение,
# позволяющее избежать циклического импорта, распространенной проблемы с приложениями Flask.
from app import routes, models  # type: ignore


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

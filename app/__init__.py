from flask import Flask
app = Flask(__name__)  # type: Flask
# Нижний импорт - это хорошо известное решение,
# позволяющее избежать циклического импорта, распространенной проблемы с приложениями Flask.
from app import routes  # type: ignore

"""
Точка входа в блог
Для завершения работы приложения у вас должен быть код на Python верхнего уровня,
который определяет экземпляр приложения Flask.
"""

from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}

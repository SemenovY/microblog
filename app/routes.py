"""
Маршрут на главную страницу
"""

from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User

@app.route("/")  # главная страница - / (без пути)
@app.route("/index")  # главная страница - /index (по умолчанию)
def index():
    """
    This function is a view function that handles the main page of the application. It is decorated with @app.route("/") and @app.route("/index") to specify the URLs that this function will handle.

    :return: A rendered HTML template 'index.html' with title 'MainPage', user information, and a list of posts.
    """
    user = {"username": "Yuriy"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", title="MainPage", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = db.session.scalar(
      sa.select(User).where(User.username == form.username.data))
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

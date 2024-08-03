"""
Маршрут на главную страницу
"""

from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm


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


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function handles the login route and renders the login.html template.

    It creates an instance of the LoginForm class and passes it to the login.html template.
    The template is rendered with the title "Sign In".

    Returns:
        The rendered login.html template.
    """
    # Create an instance of the LoginForm class
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    # Render the login.html template with the form and title
    return render_template("login.html", title="Sign In", form=form)

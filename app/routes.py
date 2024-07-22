"""
Маршрут на главную страницу
"""
from flask import render_template

from app import app
@app.route("/")  # главная страница - / (без пути)
@app.route("/index")  # главная страница - /index (по умолчанию)
def index():
    user = {'username': 'Yuriy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        'index.html', title='MainPage', user=user, posts=posts
                           )

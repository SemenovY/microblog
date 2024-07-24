"""
Атрибут method определяет метод HTTP-запроса, который следует использовать при отправке формы на сервер. По умолчанию он отправляется с запросом GET, но почти во всех случаях использование запроса POST улучшает взаимодействие с пользователем, поскольку запросы этого типа могут отправлять данные формы в теле запроса, в то время как запросы GET добавляют поля формы к URL-адресу, загромождая адресную строку браузера.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

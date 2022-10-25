from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
with app.app_context():
    labelDB = SQLAlchemy(app)
    labelDB.create_all()
    mail = Mail(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "/login"


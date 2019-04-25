from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("msglist")
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from msglist import views

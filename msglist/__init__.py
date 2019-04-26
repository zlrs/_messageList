from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask("msglist")
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
bs = Bootstrap(app)
# 删除定界符前后的空行 (whitespace-control)
# http://jinja.pocoo.org/docs/dev/templates/#whitespace-control
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from msglist import views, commands
# 当使用 flask 命令时，会自动 load .env文件中的配置
# 用来代替，更方便使用了
#    > set FLASK_APP=hello.py
#    > set FLASK_ENV=development
#    > flask run

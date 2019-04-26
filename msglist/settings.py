import os
import sys
if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
dev_db = prefix + os.path.join(PROJECT_ROOT, 'msgbase')

# app.config
# 遵循环境变量优先原则。如果未指定环境变量，则使用备选值
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


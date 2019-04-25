import os
import sys
if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 环境变量配置优先。os.getenv 的第二个参数是未配置环境变量时的备选

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
dev_db = prefix + os.path.join(PROJECT_ROOT, 'msgbase')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


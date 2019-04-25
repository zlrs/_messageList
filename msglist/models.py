from msglist import db
import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    note = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)  # 取的是本地时间
    # timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True) # 取的是utc时间，在前端转为客户端所在时区的时间


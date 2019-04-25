from flask import redirect, url_for, render_template, request, flash

from msglist import app, db
from msglist.forms import MessageForm
from msglist.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    # messages = Message.query.order_by(Message.timestamp.desc()).all()
    messages = Message.query.all()
    form = MessageForm

    if form.validate_on_submit():  # 当为非GET 请求, 且表单通过验证时
        name = form.name.data
        note = form.note.data
        a_msg = Message(name=name, note=note)
        db.session.add(a_msg)
        db.session.commit()
        # flash('你成功发送了一条消息!')
        return redirect(url_for('index'))

    return render_template('index.html', form=form, messages=messages)  # 当 GET 请求时


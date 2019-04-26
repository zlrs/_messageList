from flask import redirect, url_for, render_template, request, flash, jsonify

from msglist import app, db
from msglist.forms import MessageForm
from msglist.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    # messages = Message.query.order_by(Message.timestamp.desc()).all()
    messages = Message.query.order_by(Message.timestamp.desc()).all()  # 令较新的留言保存在数组较前部
    # Flask-WTF 自动传入 request.form; 通过 request.form 中的数据实例化表单类
    form = MessageForm()
    print('form.errors', form.errors)

    # Note that you don't have to pass request.form to Flask-WTF; it will load automatically.
    # And the convenience validate_on_submit will check if it is a POST request and if it is valid.
    # ``validate_on_submit`` is a shortcut for ``form.is_submitted() and form.validate()``
    if form.validate_on_submit():  # 当为非GET 请求, 且表单通过验证时
        name = form.name.data
        note = form.note.data
        a_msg = Message(name=name, note=note)
        db.session.add(a_msg)
        db.session.commit()
        print("INSERT SUCCESS")
        # flash('你成功发送了一条消息!')
        return redirect(url_for('index'))

    return render_template('index.html', form=form, messages=messages)  # 当 GET 请求时
    # http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates


@app.route('/api/messages', methods=['POST'])
def api_messages():
    form = request.form
    if form.op == 'get':
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        return jsonify(messages)
    elif form.op == 'insert':
        db.session.add(name=form.name, note=form.note)
        db.session.commit()
        print("INSERT SUCCESS BY API")
        # 刷新页面
    else:
        pass

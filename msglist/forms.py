from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    note = TextAreaField('留言', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CreatePost(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    text = TextAreaField('Текст записи', validators=[DataRequired()])
    submit = SubmitField('Создать')


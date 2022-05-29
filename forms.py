from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')

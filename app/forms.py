from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class AddUserForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    name = ""
    slack = StringField('Slack Username', validators=[DataRequired()])
    submit = SubmitField('Add me to the list!')


class AddRequestForm(FlaskForm):
    email = StringField('Work Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Alright, lets go!')

class RemoveRequestForm(FlaskForm):
    email = StringField('Work Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
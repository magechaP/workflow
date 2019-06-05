from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PostForm(FlaskForm):

    title = StringField('Channel title')
    category = SelectField('Channel category', choices=[('select a channel', 'select a channel'),('Management','Management'),('H.R','H.R'),('Finance','Finance'),('Maintenance','Maintainance'),('The Hall','The Hall')])
    content = TextAreaField('Work Flow...')
    submit = SubmitField('post')
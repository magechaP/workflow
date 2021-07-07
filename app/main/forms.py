from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ManagementForm(FlaskForm):
    title = StringField('Post Topic', validators=[Required()])
    department= SelectField('Department', choices=[('Select a department', 'Select a department'),('Finance', 'Finance'),('Maintance', 'Maintainace'),('Management', 'Management'),('Human Resource', 'Human Resource')])
    description = TextAreaField('Post Description',validators=[Required()])
    submit = SubmitField('Submit')
class FinanceForm(FlaskForm):
    title = StringField('Post Topic', validators=[Required()])    
    description = TextAreaField('Post Description',validators=[Required()])
    submit = SubmitField('Submit')
class HrForm(FlaskForm):
    title = StringField('Post Topic', validators=[Required()])    
    description = TextAreaField('Post Description',validators=[Required()])
    submit = SubmitField('Submit')
class MaintenanceForm(FlaskForm):
    title = StringField('Post Topic', validators=[Required()])    
    description = TextAreaField('Post Description',validators=[Required()])
    submit = SubmitField('Submit')
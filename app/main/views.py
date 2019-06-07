from flask import render_template,redirect,url_for
from ..models import Management,Finance,Hr,Maintenance
from .import main
from .forms import ManagementForm,FinanceForm,HrForm,MaintenanceForm
# from flask_login import login_required
# Management=description.Management
# Views 
@main.route("/")
def index():
    '''
    Function that renders the main page of our app
    '''
    title = 'Workflow-Management'
    return render_template ('index.html', title=title)
    # Unsure about the this dynamic root. Confirm
@main.route('/management/new', methods =['GET','POST'])
# @login_required
def new_management():
    form = ManagementForm()
    comments= Management.get_comments()
    if form.validate_on_submit():
        title = form.title.data
        department=form.department.data
        description = form.description.data
        new_description = Management(title,department,description)
        new_description.save_description()
        
        
        # Just for testing. Change
        return redirect (url_for('.new_management'))
    return render_template  ('management.html',comments=comments, management_form=form)
@main.route('/finance/new', methods =['GET','POST'])
# @login_required
def new_finance():
    form = FinanceForm()
    comments= Finance.get_comments()
    if form.validate_on_submit():
        title = form.title.data    
        description = form.description.data
        new_description = Finance(title,description)
        new_description.save_description()
        
        
        # Just for testing. Change
        return redirect (url_for('.new_finance'))
    return render_template  ('finance.html',comments=comments, finance_form=form)
@main.route('/hr/new', methods =['GET','POST'])
# @login_required
def new_hr():
    form = HrForm()
    comments= Hr.get_comments()
    if form.validate_on_submit():
        title = form.title.data    
        description = form.description.data
        new_description = Hr(title,description)
        new_description.save_description()
        
        
        # Just for testing. Change
        return redirect (url_for('.new_hr'))
    return render_template  ('hr.html',comments=comments, hr_form=form) 
@main.route('/maintenance/new', methods =['GET','POST'])
# @login_required
def new_maintenance():
    form = MaintenanceForm()
    comments= Maintenance.get_comments()
    if form.validate_on_submit():
        title = form.title.data    
        description = form.description.data
        new_description = Maintenance(title,description)
        new_description.save_description()
        
        
        # Just for testing. Change
        return redirect (url_for('.new_maintenance'))
    return render_template  ('maintenance.html',comments=comments, maintenance_form=form)       
from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos
app = Flask(__name__)

# views
@main.route("/")
def index():
   '''
   title = "Work Flow"
   '''
   title = 'Work Flow'
   posts = Post.query.all()

   return render_template('index.html', title= title, posts = posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        post = Post(title=title, content=content,category=category)
        # post.save_post(post)
        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index', id=post.id))

    return render_template('new_post.html', title='New Post', post_form=form, post ='New Post')

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content, post_id=id)

        # post.save_post(post)
        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(post_id=id).all()
    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/management/new<int:id>', methods=['GET','POST'])
@login_required
def management(category = "Management"):

    management = Post.query.filter_by(category = "Management")
    
    title = "Management"
    return render_template('management.html', management= management, title=title, post ='New Post')

@main.route('/hr/new<int:id>', methods=['GET','POST'])
@login_required
def hr(category = "hr"):

    hr = Post.query.filter_by(category = "HR")
    
    title = "HR"
    return render_template('hr.html', hr= hr, title=title, post ='New Post')

@main.route('/finance/new<int:id>', methods=['GET','POST'])
@login_required
def finance(category = "Finance"):

    finance = Post.query.filter_by(category = "Finance")
    
    title = "Finance"
    return render_template('finance.html', finance= finance, title=title, post ='New Post')

@main.route('/maintenance/new<int:id>', methods=['GET','POST'])
@login_required
def maintenance(category = "Maintenance"):

    maintenance = Post.query.filter_by(category = "Maintenance")
    
    title = "Maintenance"
    return render_template('maintenance.html', maintenance= maintenance, title=title, post ='New Post')

@main.route('/thehall/new<int:id>', methods=['GET','POST'])
@login_required
def thehall(category = "Thehall"):

    management = Post.query.filter_by(category = "Management")
    
    title = "The Hall"
    return render_template('index.html', management= management, title=title, post ='New Post')

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
   del_post = Post.query.filter_by(id=id).first()
   db.session.delete(del_post)
   db.session.commit()
   
   return redirect(url_for('main.index'))    
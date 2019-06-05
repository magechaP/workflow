from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos
app = Flask(__name__)
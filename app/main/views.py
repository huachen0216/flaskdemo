from os import abort
from flask import render_template
from . import main
from app.models import User


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usr/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

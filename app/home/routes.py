from flask import request, render_template, session, url_for, request, redirect
from . import home

@home.route('/', methods=['GET'])
def index():
    return render_template('home/index.html')
    
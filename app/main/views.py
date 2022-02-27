from email import message
from turtle import title
from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home- Welcome to The Best News Preview Articles Website'
    return render_template('..index.html', title = title)
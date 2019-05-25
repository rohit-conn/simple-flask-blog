from flask import Blueprint, render_template, request

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return "Hello World"

@core.route('/info')
def info():
    return "Info Page"

from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/map')
def map():
    return render_template('map.html')

@main_blueprint.route('/create')
def create():
    return render_template('create.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')
from flask import Blueprint, render_template

home_blueprint = Blueprint(
    'home_bp', __name__
)


@home_blueprint.route('/')
def home():
    pagetitle = "HomePage"
    return render_template('layout.html', mytitle=pagetitle)

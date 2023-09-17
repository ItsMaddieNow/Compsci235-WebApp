from flask import Blueprint, session, request, render_template, jsonify, flash, url_for, redirect
import math
import games.wishlist.services as services
import games.adapters.datareader.repository as repo
from games.auth.authentication import login_required

wishlist_blueprint = Blueprint(
    'wishlist_bp', __name__
)


@wishlist_blueprint.route('/wishlist/add', methods=["POST"])
@login_required
def wishlist_add():
    pass


@wishlist_blueprint.route('/wishlist/remove', methods=["POST"])
@login_required
def wishlist_remove():
    pass


@wishlist_blueprint.route('/wishlist/', methods=["GET"])
@login_required
def wishlist():
    return render_template("wishlist.html")

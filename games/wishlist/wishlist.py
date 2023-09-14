from flask import Blueprint, session, request, render_template, jsonify, flash, url_for, redirect
import math
import games.wishlist.services as services
import games.adapters.datareader.repository as repo

wishlist_blueprint = Blueprint(
    'wishlist_bp', __name__
)


@wishlist_blueprint.route('/wishlist/add', methods=["POST"])
def wishlist_add():
    pass


@wishlist_blueprint.route('/wishlist/remove', methods=["POST"])
def wishlist_remove():
    pass


@wishlist_blueprint.route('/wishlist/', methods=["GET"])
def wishlist():
    return render_template("wishlist.html")

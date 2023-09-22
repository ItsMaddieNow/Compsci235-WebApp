from flask import Blueprint, render_template, flash
import games.adapters.datareader.repository as repo
from games.description.services import get_game
from flask import Blueprint, session, request, render_template, jsonify, flash, url_for, redirect
import math
import games.wishlist.services as services
import games.adapters.datareader.repository as repo
from games.auth.authentication import login_required

from games.domainmodel.model import Game, Genre

description_blueprint = Blueprint(
    'description_bp', __name__
)


@description_blueprint.route("/description/<game_id>")
def description(game_id):
    game = get_game(int(game_id), repo.repo_instance)
    # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
    user_id = session["username"]
    wishlist_games = services.get_user_wishlist(user_id, repo.repo_instance)
    wishlist_game_ids = [game.game_id for game in wishlist_games]
    return render_template('gameDescription.html', game=game,wishlist_game_ids=wishlist_game_ids)

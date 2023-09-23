from flask import Blueprint, render_template, redirect, url_for
import games.adapters.datareader.repository as repo
from games.description.services import get_game
from games.reviews.reviews import ReviewForm
from games.reviews import services as review_services
from games.domainmodel.model import Game, Genre
from games.auth.authentication import login_required
from flask import Blueprint, session, request, render_template, jsonify, flash, url_for, redirect
import math
import games.wishlist.services as services

description_blueprint = Blueprint(
    'description_bp', __name__
)


@description_blueprint.route("/description/<game_id>", methods=['GET', 'POST'])
@login_required
def description(game_id):
    game = get_game(int(game_id), repo.repo_instance)
    form = ReviewForm()

    if form.validate_on_submit():
        return redirect(url_for('description_bp.description'))  # Redirect after handling form submission
    user_id = session["username"]
    wishlist_games = services.get_user_wishlist(user_id, repo.repo_instance)
    wishlist_game_ids = [game.game_id for game in wishlist_games]
    return render_template('gameDescription.html', game=game, form=form,
                           wishlist_game_ids=wishlist_game_ids)


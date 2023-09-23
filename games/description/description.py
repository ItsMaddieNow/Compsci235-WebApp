from flask import Blueprint, render_template, redirect, url_for
import games.adapters.datareader.repository as repo
from games.description.services import get_game
from games.reviews.reviews import ReviewForm
from games.reviews import services as review_services
from games.domainmodel.model import Game, Genre

description_blueprint = Blueprint(
    'description_bp', __name__
)


@description_blueprint.route("/description/<game_id>", methods=['GET', 'POST'])
def description(game_id):
    game = get_game(int(game_id), repo.repo_instance)
    form = ReviewForm()

    if form.validate_on_submit():
        return redirect(url_for('description_bp.description'))  # Redirect after handling form submission

    return render_template('gameDescription.html', game=game, form=form)


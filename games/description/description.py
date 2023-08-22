from flask import Blueprint, render_template
import games.adapters.datareader.repository as repo
from games.description.services import get_game

from games.domainmodel.model import Game, Genre

from games.utilities.copyright import copyright_rand

description_blueprint = Blueprint(
    'description_bp', __name__
)


@description_blueprint.route("/description/<game_id>")
def description(game_id):
    game = get_game(int(game_id), repo.repo_instance)
    # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
    return render_template('gameDescription.html', game=game, copyright=copyright_rand())

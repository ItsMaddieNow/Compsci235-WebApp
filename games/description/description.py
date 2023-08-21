from flask import Blueprint, render_template
import random

description_blueprint = Blueprint(
    'description_bp', __name__
)
# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from games.domainmodel.model import Game
from games.domainmodel.model import Genre


# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
def create_some_game():
    some_game = Game(1, "Call of Duty® 4: Modern Warfare®")
    some_game.release_date = "Nov 12, 2007"
    some_game.price = 9.99
    some_game.description = "The new action-thriller from the award-winning team at Infinity Ward, the creators of " \
                            "the Call of Duty® series, delivers the most intense and cinematic action experience ever. "
    some_game.image_url = "https://cdn.akamai.steamstatic.com/steam/apps/7940/header.jpg?t=1646762118"
    some_game.add_genre(Genre("Fantasy"))
    some_game.add_genre(Genre("I know nothing about this game"))
    return some_game


@description_blueprint.route("/description/<game>")
def description(game):
    some_game = create_some_game()
    team_members = ["Ubayd Abdul Majit", "Bilal Sarwar", "Madeline Whitmore"]
    random.shuffle(team_members)
    # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
    return render_template('gameDescription.html', game=some_game,
                           copyright=f"&copy {team_members[0]}, {team_members[1]} and {team_members[2]} 2023")

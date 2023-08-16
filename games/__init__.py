"""Initialize Flask app."""
import math
import random

from flask import Flask, render_template, request

# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from games.domainmodel.model import Game

GAMES_PER_PAGE = 12 # 12 is a nice number divisible by 1, 2, 3 and 4, so it works nicely with Flexbox

# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
def create_some_game():
    some_game = Game(1, "Call of Duty® 4: Modern Warfare®")
    some_game.release_date = "Nov 12, 2007"
    some_game.price = 9.99
    some_game.description = "The new action-thriller from the award-winning team at Infinity Ward, the creators of " \
                            "the Call of Duty® series, delivers the most intense and cinematic action experience ever. "
    some_game.image_url = "https://cdn.akamai.steamstatic.com/steam/apps/7940/header.jpg?t=1646762118"
    return some_game


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    @app.route('/')
    def home():
        some_game = create_some_game()
        team_members = ["Ubayd Abdul Majit", "Bilal Sarwar", "Madeline Whitmore"]
        random.shuffle(team_members)
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
        return render_template('gameDescription.html', game=some_game, copyright=f"&copy {team_members[0]}, {team_members[1]} and {team_members[2]} 2023")

    @app.route('/games')
    def games():
        page = request.args.get('page', 1, type=int)
        team_members = ["Ubayd Abdul Majit", "Bilal Sarwar", "Madeline Whitmore"]
        random.shuffle(team_members)
        games_list = [
            {
                'name': "Celeste",
                'price': '4.99',
                "headerImage": "../static/headers/celeste.jpg"
            },
            {
                'name': "Dredge",
                'price': '5.99',
                "headerImage": "../static/headers/dredge.jpg"
            },
            {
                'name': "Towerfall",
                'price': '5.99',
                "headerImage": "../static/headers/towerfall.jpg"
            },
        ]
        pages = math.ceil(len(games_list)/GAMES_PER_PAGE)
        page_selection = games_list[max((page-1)*GAMES_PER_PAGE, 0):min(page*GAMES_PER_PAGE, len(games_list))]
        return render_template('games.html', gamesList=page_selection, copyright=f"&copy {team_members[0]}, {team_members[1]} and {team_members[2]} 2023")
    return app

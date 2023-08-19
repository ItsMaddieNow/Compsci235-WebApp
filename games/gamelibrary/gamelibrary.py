from flask import Blueprint, request, render_template
import math
import random
import games.gamelibrary.services as services

GAMES_PER_PAGE = 12  # 12 is a nice number divisible by 1, 2, 3 and 4, so it works nicely with Flexbox

library_blueprint = Blueprint(
    'library_bp', __name__
)


@library_blueprint.route('/games')
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
    pages = math.ceil(len(games_list) / GAMES_PER_PAGE)
    page_selection = services.get_games(max((page - 1) * GAMES_PER_PAGE, 0), min(page * GAMES_PER_PAGE, len(games_list)))
    return render_template('games.html', gamesList=page_selection, current_page=page, total_pages=pages,
                           copyright=f"&copy {team_members[0]}, {team_members[1]} and {team_members[2]} 2023")

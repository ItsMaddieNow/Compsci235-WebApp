from flask import Blueprint, request, render_template, url_for
import math
import random
import games.gamelibrary.services as services
import games.adapters.datareader.repository as repo

REPO = repo.repo_instance
GAMES_PER_PAGE = 12  # 12 is a nice number divisible by 1, 2, 3 and 4, so it works nicely with Flexbox

library_blueprint = Blueprint(
    'library_bp', __name__
)


@library_blueprint.route('/games')
def games(library_bp=None):
    page = request.args.get('page', 1, type=int)
    sort_by = request.args.get('sortBy', "Newest", type=str)
    team_members = ["Ubayd Abdul Majit", "Bilal Sarwar", "Madeline Whitmore"]
    random.shuffle(team_members)
    page_selection = services.get_games(page, GAMES_PER_PAGE, sort_by, REPO)
    pages = math.ceil(services.get_game_amount(REPO) / GAMES_PER_PAGE)
    return render_template('games.html',
                           gamesList=page_selection,
                           current_page=page,
                           total_pages=pages,
                           sort_by=sort_by,
                           copyright=f"&copy {team_members[0]}, {team_members[1]} and {team_members[2]} 2023"
                           )

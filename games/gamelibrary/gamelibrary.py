from flask import Blueprint, request, render_template
import math
import games.gamelibrary.services as services
import games.adapters.datareader.repository as repo
REPO = repo.repo_instance
GAMES_PER_PAGE = 12  # 12 is a nice number divisible by 1, 2, 3 and 4, so it works nicely with Flexbox

library_blueprint = Blueprint(
    'library_bp', __name__
)


@library_blueprint.route('/games')
def games():
    page = request.args.get('page', 1, type=int)
    sort_by = request.args.get('sortBy', "Newest", type=str)
    page_selection = services.get_games(page, GAMES_PER_PAGE, sort_by, REPO)
    pages = math.ceil(services.get_game_amount(REPO) / GAMES_PER_PAGE)
    return render_template('games.html',
                           gamesList=page_selection,
                           current_page=page,
                           total_pages=pages,
                           sort_by=sort_by,
                           )

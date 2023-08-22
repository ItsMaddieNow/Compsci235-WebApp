from flask import Blueprint, request, render_template, redirect
import games.adapters.datareader.repository as repo
from games.search.services import search_games
from games.utilities.copyright import copyright_rand

REPO = repo.repo_instance
GAMES_PER_PAGE = 12  # 12 is a nice number divisible by 1, 2, 3 and 4, so it works nicely with Flexbox

search_blueprint = Blueprint(
    'search_bp', __name__
)


@search_blueprint.route('/search', methods=["GET"])
def search():
    args = request.args
    if "term" not in args:
        return render_template("search/queryLodge.html", copyright=copyright_rand())
    else:
        term = request.args.get("term", type=str)
        key = request.args.get("key", type=str)
        games = search_games(term, key, repo.repo_instance)
        return render_template("search/results.html", gamesList=games, copyright=copyright_rand())





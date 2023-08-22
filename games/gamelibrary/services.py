from games.domainmodel.model import Game
from games.adapters.datareader.repository import AbstractRepository


def get_games(page, per_page, key, repo: AbstractRepository):
    return repo.get_games_by_key((page-1)*per_page, page*per_page, key)


def get_game_amount(repo: AbstractRepository):
    return repo.game_amount()

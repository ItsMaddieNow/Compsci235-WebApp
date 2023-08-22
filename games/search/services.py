from games.adapters.datareader.repository import AbstractRepository


def search_games(term, key, repo: AbstractRepository):
    return repo.search_games_by_key(term, key)

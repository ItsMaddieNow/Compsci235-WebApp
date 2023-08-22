from games.adapters.datareader.repository import AbstractRepository


def get_game(game_id, repo: AbstractRepository):
    return repo.get_game(game_id)

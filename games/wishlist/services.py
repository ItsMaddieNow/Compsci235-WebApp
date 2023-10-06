from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Wishlist


def remove_game_from_wishlist(user_id, game_id, repo: AbstractRepository):
    user = repo.get_user(user_id)
    game = repo.get_game(int(game_id))
    repo.remove_game_from_wishlist(user, game)


def get_user_wishlist(user_id, repo: AbstractRepository):
    user = repo.get_user(user_id)
    wishlist = repo.get_wishlist(user)
    return wishlist.list_of_games() if wishlist else []


def add_game_to_wishlist(user_id, game_id, repo: AbstractRepository):
    user = repo.get_user(user_id)
    game = repo.get_game(int(game_id))
    wishlist = repo.get_wishlist(user)
    if not wishlist:
        wishlist = Wishlist(user)
        repo.add_wishlist(wishlist)
    if game not in wishlist.list_of_games():
        wishlist.list_of_games().append(game)
    else:
        raise ValueError("Game already in the wishlist!")

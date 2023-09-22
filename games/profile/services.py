from games.adapters.datareader.repository import AbstractRepository
from games.domainmodel.model import Wishlist, Review, User


def get_username(username, repo: AbstractRepository):
    user = repo.get_user(username)
    return user


def get_reviews_by_user(user_id, repo: AbstractRepository):
    reviews = repo.get_review(user_id)
    return reviews

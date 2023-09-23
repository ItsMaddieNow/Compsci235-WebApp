from games.adapters.datareader.repository import RepositoryException, AbstractRepository
from games.domainmodel.model import User, Game, Review


def add_review_for_game(user: User, game: Game, rating: int, comment: str, repo: AbstractRepository) -> bool:
    """Adds a review for a specific game."""
    if isinstance(user, User):
        review = Review(user, game, rating, comment)
        try:
            repo.add_review(review)
            return True
        except RepositoryException:
            return False


def get_reviews_for_gamez(game: Game, repo: AbstractRepository) -> list:
    """Returns all reviews for a specific game."""
    return repo.get_reviews_for_game(game)


def calculate_average_rating(game: Game, repo: AbstractRepository) -> float:
    """Calculate the average rating for a specific game."""
    reviews = get_reviews_for_gamez(game, repo)
    if reviews:
        total_rating = sum([review.rating for review in reviews])
        return total_rating / len(reviews)
    return 0  # Return 0 if no reviews yet

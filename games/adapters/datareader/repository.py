import abc
from typing import List

from games.domainmodel.model import Publisher, Genre, Game, User, Review, Wishlist

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_publisher(self, publisher: Publisher):
        """ Adds a Publisher to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_publisher(self, publisher_name: str) -> Publisher:
        """ Returns the Publisher with the given publisher_name from the repository.

        If there is no Publisher with the given publisher_name, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns all existing Genres from the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_game(self, game: Game):
        """ Adds a Game to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_game(self, game_id: int) -> Game:
        """ Returns Game with the given game_id from the repository.

        If there is no Game with the given game_id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_games_by_key(self, term: str, key) -> List[Game]:
        raise NotImplementedError

    @abc.abstractmethod
    def game_amount(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_games_by_key(self, start_index, end_index, key):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        """ Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str) -> User:
        """ Returns the User with the given username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Review to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_review(self, review_id: int) -> Review:
        """ Returns the Review with the given review_id from the repository.

        If there is no Review with the given review_id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_wishlist(self, wishlist: Wishlist):
        """ Adds a Wishlist to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_wishlist(self, user: User) -> Wishlist:
        """ Returns the Wishlist for the given User from the repository.

        If there is no Wishlist for the given User, this method returns None.
        """
        raise NotImplementedError

from typing import List
from games.domainmodel.model import Publisher, Genre, Game, User, Review, Wishlist
from .repository import AbstractRepository, RepositoryException
from .csvdatareader import GameFileCSVReader


def get_game_title(game):
    return game.title


def get_game_description(game):
    return game.description


def get_game_publisher(game):
    return game.publisher.publisher_name


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__publishers = {}
        self.__genres = {}
        self.__games = {}
        self.__users = {}
        self.__reviews = []
        self.__wishlists = {}

    def populate_data_from_file(self, file_path):
        reader = GameFileCSVReader(file_path)
        reader.read_csv_file()
        for genre in reader.dataset_of_genres:
            self.__genres[genre.genre_name] = genre
        for game in reader.dataset_of_games:
            self.__games[game.game_id] = game
            for genre in game.genres:
                self.__genres[genre.genre_name].add_game(game)
        for publisher in reader.dataset_of_publishers:
            self.__publishers[publisher.publisher_name] = publisher

    # Publisher Methods
    def add_publisher(self, publisher: Publisher) -> bool:
        if publisher.publisher_name not in self.__publishers:
            self.__publishers[publisher.publisher_name] = publisher
            return True
        raise RepositoryException(f'Publisher with name {publisher.publisher_name} already exists.')

    def get_publisher(self, publisher_name: str) -> Publisher:
        return self.__publishers.get(publisher_name)

    # Genre Methods
    def add_genre(self, genre: Genre) -> bool:
        if genre.genre_name not in self.__genres:
            self.__genres[genre.genre_name] = genre
            return True
        raise RepositoryException(f'Genre with name {genre.genre_name} already exists.')

    def get_genre(self, genre_name: str) -> Genre:
        return self.__genres.get(genre_name)

    def get_genres(self) -> List[Genre]:
        return list(self.__genres.values())

    # Game Methods
    def add_game(self, game: Game) -> bool:
        if game.game_id not in self.__games:
            self.__games[game.game_id] = game
            return True
        raise RepositoryException(f'Game with ID {game.game_id} already exists.')

    def get_game(self, game_id: int) -> Game:
        return self.__games.get(game_id)

    def search_games_by_key(self, term: str, key_str: str) -> List[Game]:
        key = get_game_title
        if key_str == "description":
            key = get_game_description
        elif key_str == "publisher":
            key = get_game_publisher
        return [game for game in self.__games.values() if isinstance(key(game), str) and
                term.lower() in key(game).lower()]

    def game_amount(self):
        return len(self.__games)

    def get_games_by_key(self, start_index, end_index, key_str):
        key = None
        reverse = False
        if key_str == "Newest":
            key = Game.date_sort_key
            reverse = True
        elif key_str == "Oldest":
            key = Game.date_sort_key
        # Sorting this list every time a request is made is probably a bad idea but like ¯\_(ツ)_/¯
        games = sorted(self.__games.values(), key=key, reverse=reverse)
        return games[start_index:end_index]

    # User Methods
    def add_user(self, user: User) -> bool:
        if user.username not in self.__users:
            self.__users[user.username] = user
            return True
        raise RepositoryException(f'User with username {user.username} already exists.')

    def get_user(self, username: str) -> User:
        return self.__users.get(username)

    # Review Methods
    def add_review(self, review: Review) -> bool:
        if review not in self.__reviews:
            self.__reviews.append(review)
            return True
        return False

    def get_review(self, review_id: int) -> Review | None:
        if 0 <= review_id < len(self.__reviews):
            return self.__reviews[review_id]
        return None

    # Wishlist Methods
    def add_wishlist(self, wishlist: Wishlist) -> bool:
        if wishlist.user.username not in self.__wishlists:
            self.__wishlists[wishlist.user.username] = wishlist
            return True
        raise RepositoryException(f'Wishlist for user {wishlist.user.username} already exists.')

    def get_wishlist(self, user: User) -> Wishlist:
        return self.__wishlists.get(user.username)

    def remove_game_from_wishlist(self, user: User, game: Game) -> bool:
        wishlist = self.get_wishlist(user)
        if wishlist and game in wishlist.list_of_games():
            wishlist.list_of_games().remove(game)
            return True
        return False


def populate(file_path, repo: MemoryRepository):
    # initialise, read, populate
    repo.populate_data_from_file(file_path)

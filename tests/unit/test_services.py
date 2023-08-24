import pytest

from games.domainmodel.model import Game
from games.gamelibrary import services as library_services
from games.search import services as search_services


def test_get_games_library_newest(in_memory_repo):
    games = library_services.get_games(1, 12, "Newest", in_memory_repo)
    for i in range(0, len(games) - 1):
        assert games[i].date_sort_key() >= games[i + 1].date_sort_key()


def test_get_games_library_oldest(in_memory_repo):
    games = library_services.get_games(1, 12, "Oldest", in_memory_repo)
    for i in range(0, len(games) - 1):
        assert games[i].date_sort_key() <= games[i + 1].date_sort_key()


def test_library_game_amount(in_memory_repo):
    assert 877 == library_services.get_game_amount(in_memory_repo)


def test_search_by_title(in_memory_repo):
    games = search_services.search_games("super meat boy", "title", in_memory_repo)
    assert games[0] == Game(40800, "Super Meat Boy")


def test_search_by_description(in_memory_repo):
    games = search_services.search_games("super meat boy", "description", in_memory_repo)
    assert str(games) == "[<Game 1672700, Tiny Hunter>, <Game 266330, Ethan: Meteor Hunter>, <Game 40800, Super Meat Boy>]"


def test_search_by_publisher(in_memory_repo):
    games = search_services.search_games("Pablo Picazo", "publisher", in_memory_repo)
    assert games[0] == Game(1995240, "Deer Journey")
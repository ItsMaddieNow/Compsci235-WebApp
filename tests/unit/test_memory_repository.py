import pytest

from games.domainmodel.model import Game


def test_repo_get_game(in_memory_repo):
    game = in_memory_repo.get_game(40800)
    assert game == Game(40800, "Super Meat Boy")


def test_repo_get_nonexistent_game(in_memory_repo):
    game = in_memory_repo.get_game(1)
    assert game is None


def test_repo_search_games(in_memory_repo):
    description_game = in_memory_repo.search_games_by_key("MURI is a DOS-style", "description")
    assert description_game == [Game(267360, "MURI")]
    title_game = in_memory_repo.search_games_by_key("super meat boy", "title")
    assert title_game == [Game(40800, "Super Meat Boy")]
    publisher_game = in_memory_repo.search_games_by_key("encore", "publisher")
    assert publisher_game == [Game(243890, "Mavis Beacon Teaches Typing Family Edition")]


def test_repo_get_ordered_games(in_memory_repo):
    oldest_games = in_memory_repo.get_games_by_key(0, 3, "Oldest")
    assert (str(oldest_games) ==
            "[<Game 3010, Xpand Rally>, <Game 7940, Call of Duty® 4: Modern Warfare®>, <Game 16130, Fish Tycoon>]")
    newest_games = in_memory_repo.get_games_by_key(0, 3, "Newest")
    assert (str(newest_games) ==
            "[<Game 2010700, Hunter Survivors>, <Game 1995240, Deer Journey>, <Game 2061060, The Marson Home>]")


def test_repo_can_retrieve_genres(in_memory_repo):
    genres = in_memory_repo.get_genres()
    simulation = None
    for genre in genres:
        if genre.genre_name == "Simulation":
            simulation = genre
    assert simulation.number_of_games == 167


def test_repo_get_genre(in_memory_repo):
    genre = in_memory_repo.get_genre("Racing")
    assert genre.number_of_games == 31


def test_repo_get_genre_not_exist(in_memory_repo):
    # Check None is returned when Non-Existent Genre is Requested
    genre = in_memory_repo.get_genre("NFSW")
    assert genre is None

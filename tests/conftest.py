import pytest

from games import create_app
from games.adapters.datareader import memory_repository


@pytest.fixture
def in_memory_repo():
    repo = memory_repository.MemoryRepository()
    memory_repository.populate("./games/adapters/data/games.csv", repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,  # Set to True during testing.
    })

    return my_app.test_client()

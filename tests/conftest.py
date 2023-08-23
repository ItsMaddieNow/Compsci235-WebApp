import pytest

from games.adapters.datareader import memory_repository


@pytest.fixture
def in_memory_repo():
    repo = memory_repository.MemoryRepository()
    memory_repository.populate("./games/adapters/data/games.csv", repo)
    return repo

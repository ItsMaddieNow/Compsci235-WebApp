import pytest


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200


@pytest.mark.parametrize(("page", "order", "result"), ((0, "Newest", b"No Games found at specified page"),
                                                       (75, "Newest", b"No Games found at specified page"),
                                                       (1, "Newest", b"Deer Journey"), (1, "Oldest", b"Xpand Rally")))
def test_library_pages(client, page, order, result):
    response = client.get("/games", query_string={"page": page, "sortBy": order})
    assert result in response.data


@pytest.mark.parametrize(("term", "key", "result"), (("super meat boy", "title", b"Super Meat Boy"),
                                                     ("a Franco-Spanish painter and a key figure in the pictorial",
                                                      "description", b"Maria Blanchard Virtual Gallery"),
                                                     ("Pablo Picazo", "publisher", b"Deer Journey"),
                                                     ("sdjfjlkgkbhsdjghlj", "title",
                                                      b"No Games Found With The Specified Criteria")))
def test_search(client, term, key, result):
    response = client.get("/search", query_string={"term": term, "key": key})
    assert result in response.data


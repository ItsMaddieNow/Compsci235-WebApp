games_list = [
    {
        'name': "Celeste",
        'price': '4.99',
        "headerImage": "../static/headers/celeste.jpg"
    },
    {
        'name': "Dredge",
        'price': '5.99',
        "headerImage": "../static/headers/dredge.jpg"
    },
    {
        'name': "Towerfall",
        'price': '5.99',
        "headerImage": "../static/headers/towerfall.jpg"
    },
]


def get_games(start, end):
    return games_list[start:end]

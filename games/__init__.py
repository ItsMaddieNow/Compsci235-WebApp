"""Initialize Flask app."""

from flask import Flask, render_template, request

import games.adapters.datareader
import games.adapters.datareader.repository as repo
from games.adapters.datareader.memory_repository import MemoryRepository
from games.utilities.copyright import copyright_rand


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    repo.repo_instance = MemoryRepository()
    repo.repo_instance.populate_data_from_file("./games/adapters/data/games.csv")

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .gamelibrary import gamelibrary
        app.register_blueprint(gamelibrary.library_blueprint)

        from .description import description
        app.register_blueprint(description.description_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

    app.jinja_env.globals.update(copyright_rand=copyright_rand)

    return app

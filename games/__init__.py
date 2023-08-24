"""Initialize Flask app."""

from flask import Flask, render_template, request

import games.adapters.datareader
import games.adapters.datareader.repository as repo
from games.adapters.datareader.memory_repository import MemoryRepository


def create_app():
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

    return app

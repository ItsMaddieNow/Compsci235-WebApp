"""Initialize Flask app."""

from flask import Flask, render_template, request

import games.adapters.datareader
import games.adapters.datareader.repository as repo
from games.adapters.datareader.memory_repository import MemoryRepository


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    repo.repo_instance = MemoryRepository("./games/adapters/data/games.csv")

    with app.app_context():
        from .gamelibrary import gamelibrary
        app.register_blueprint(gamelibrary.library_blueprint)

        from .description import description
        app.register_blueprint(description.description_blueprint)

    return app

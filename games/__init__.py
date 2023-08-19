"""Initialize Flask app."""

from flask import Flask, render_template, request

import games.adapters.datareader

def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    with app.app_context():
        from .gamelibrary import gamelibrary
        app.register_blueprint(gamelibrary.library_blueprint)

        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app

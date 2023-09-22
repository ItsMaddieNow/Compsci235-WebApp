from flask import Blueprint, request, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, SubmitField
import games.reviews.services as services
import games.adapters.datareader.repository as repo
from ..domainmodel.model import Game, Review
from games.auth.authentication import login_required


class AudienceReviewForm(FlaskForm):
    review_txt = TextAreaField('Review', [validators.length(min=1, max=500)])
    submit = SubmitField('Submit Review')


reviews_blueprint = Blueprint('reviews_bp', __name__)


@reviews_blueprint.route('/reviews/view_game_reviews/<int:game_id>', methods=['GET'])
def view_game_reviews(game_id):
    pass



@reviews_blueprint.route('/reviews/add_audience_review/<int:game_id>', methods=['POST'])
@login_required
def add_audience_review(game_id):
    pass

    return redirect(url_for('reviews_bp.view_game_reviews', game_id=game_id))

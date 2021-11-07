"""Cam Hudson Personal Website app's not-found.html view.

URLs handled in this file include anything that results in a 404.
"""
from flask.templating import render_template
from flask import request
import camhudson

@camhudson.app.errorhandler(404)
def get_404(e) -> str:
    """Handle 404 error by returning custom 404 page."""
    context = {
        'url': request.full_path[:-1]  # -1 so we don't include query string
    }
    return render_template('404.html', **context), 404

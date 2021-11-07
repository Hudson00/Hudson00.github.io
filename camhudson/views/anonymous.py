"""Cam Hudson Personal Website app's index.html view.

URLs handled in this file include:
/anonymous
"""
from flask.templating import render_template
import camhudson

@camhudson.app.route('/anonymous-message', methods=['GET'])
def get_anonymous_message() -> str:
    """Handle request for anonymous message form."""
    return render_template('anonymous-message.html')

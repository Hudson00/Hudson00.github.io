"""Cam Hudson Personal Website app's index.html view.

URLs handled in this file include:
/
"""
from flask.templating import render_template
import camhudson

@camhudson.app.route('/', methods=['GET'])
@camhudson.app.route('/index.html', methods=['GET'])
def get_index() -> str:
    """Handle request for homepage."""
    return render_template('index.html')

"""Cam Hudson Personal Website app's index.html view.

URLs handled in this file include:
/contact-info
"""
from flask.templating import render_template
import camhudson

@camhudson.app.route('/contact-info', methods=['GET'])
def get_contact_info() -> str:
    """Handle request for homepage."""
    return render_template('index.html')

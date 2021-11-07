"""Cam Hudson Personal Website app's index.html view.

URLs handled in this file include:
/
"""
from flask import render_template, session
from camhudson.views.utility import create_index_card  # Make linter shut up
import camhudson

@camhudson.app.route('/', methods=['GET'])
@camhudson.app.route('/index.html', methods=['GET'])
def get_index() -> str:
    """Handle request for homepage."""
    context = {
        'cards': [
            create_index_card(
                'Bio',
                'Take a few moments to learn a little about Cam!',
                '/bio',
                '/static/images/cam.png',
                'Cam Hudson selfie'
            ),
            create_index_card(
                'R&eacute;sum&eacute;',
                'Dive into Cam\'s skills, education, and work history!',
                '/hudson-resume.pdf\" target=\"_blank',
                '/static/images/joao-ferrao-resume.png',
                'Resume on desk'
            ),
            create_index_card(
                'Contact',
                'Find out how you can get in touch with Cam!',
                'contact-info',
                '/static/images/elizaveta-kushnirenko-mailbox.png',
                'Mailbox',
            )
        ]
    }
    return render_template('index.html', **context)

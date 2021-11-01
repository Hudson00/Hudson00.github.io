"""Cam Hudson Personal Website app's resume view.

URLs handled in this file include:
/hudson-resume.pdf
"""
from flask import send_from_directory
import camhudson

@camhudson.app.route('/hudson-resume.pdf', methods=['GET'])
def get_resume() -> str:
    """Handle request for resume."""
    return send_from_directory(
        camhudson.app.config['STATIC_FOLDER'],
        'files/hudson-resume.pdf'
    )

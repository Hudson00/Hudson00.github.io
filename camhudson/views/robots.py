"""Cam Hudson Personal Website app's robots.txt view.

URLs handled in this file include:
/robots.txt
"""
from flask import send_from_directory
import camhudson

@camhudson.app.route('/robots.txt', methods=['GET'])
def get_robots() -> str:
    """Handle request for robots.txt."""
    return send_from_directory(
        camhudson.app.config['STATIC_FOLDER'],
        'files/robots.txt'
    )

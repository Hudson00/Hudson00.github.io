"""Cam Hudson Personal Website app's handler for static image content.

URLS handled in this file include:
/cam.png
"""
from flask import send_from_directory
import camhudson

@camhudson.app.route('/static/<path>', methods=['GET'])
def get_static_file(path: str) -> str:
    """Handle request for my picture."""
    print('\there')
    print(path)
    print('\tdone')
    return send_from_directory(
        camhudson.app.config['STATIC_FOLDER'],
        f'{path}'
    )

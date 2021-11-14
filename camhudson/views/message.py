"""Cam Hudson Personal Website app's index.html view.

URLs handled in this file include:
/message
"""
from os import abort
from flask import abort, render_template, request
import camhudson

@camhudson.app.route('/message', methods=['GET', 'POST'])
def handle_message() -> str:
    """Handle requests for the message view.
    
    GET requests return the message page. POST requests upload the
    submitted message to the database and return the tracking number
    associated with the message.
    """
    if request.method == 'GET':
        return get_message()
    elif request.method == 'POST':
        return post_message()
    else:
        abort(500)  # NOTE: Should never happen, as Flask filters traffic


def get_message() -> str:
    """GET handler for /message.
    
    Return the HTML for the message form.
    """
    return render_template('message.html')


def post_message() -> str:
    """POST handler for /message.
    
    Upload the submitted message to the database and return the
    tracking number associated with the message embedded in the
    HTML.
    """
    print(request.form)
    if ('anonymous' not in request.form or 'message' not in request.form or
        'email' not in request.form):

        abort(400)  # Bad request

    # TODO: handle the form

    # Retrieve database connection
    dynamodb = camhudson.model.get_db()

    # item = dynamodb.get_item(
    #     TableName='database-dev',
    #     Key={
    #         'id': {
    #             'N': '0'
    #         }
    #     }
    # )


    db_response = dynamodb.put_item(
        TableName='database-dev',
        Item={
            'id': {
                'N': '0'
            },
            'message': {
                'S': '<MESSAGE>'
            },
            'timestamp': {
                'S': 'YYYY-MM-DD hh:mm:ss:µµµµµµ'
            }
        }
    )

    print(db_response)

    return "<!doctype html><h1>hi</h1>"

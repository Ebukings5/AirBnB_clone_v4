#!/usr/bin/python3
"""
app
"""

from flask import Flask, jsonify
# from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage

# Creating an instance of Flask
app = Flask(__name__)

# Uncomment this if you want to enable CORS
# CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """
    Closes the storage session after each request.
    """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    Handles 404 error.
    :param exception: The exception that was raised.
    :return: A JSON response with an error message.
    """
    data = {
        "error": "Not found"
    }
    resp = jsonify(data)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)

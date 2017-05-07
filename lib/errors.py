# zato-api
# lib/errors.py
# error stuff

from __init__ import returnApp
from flask import make_response, jsonify

app = returnApp()

# error handlers
@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"error": "Not found"}), 404)

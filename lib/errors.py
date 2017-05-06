# zato-api
# lib/errors.py
# error stuff

# error handlers
@app.errorhandler(404)
def not_found(e):
    return make_respone(jsonify({"error": "Not found"}), 404)

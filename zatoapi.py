# zato-api
# zato-api.py
# main file

# get flask stuff
import os
from flask import render_template_string, jsonify, abort, request
# might not be used
#from flask_mail import Mail
# will be used
#from flask_sqlalchemy import SQLAlchemy

# own libraries
from lib.errors import *
from lib.users import *
from lib.databaseTools import *
# flask will be setup through the __init__ inside of lib

# index with a 404
@app.route("/")
def index():
    abort(404)

# run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0')

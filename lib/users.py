# zato-api
# users.py
# core functions for user registration, management and login (relies on db connection)

from __init__ import returnApp
app = returnApp()

# get user data
@app.route("/v1/users/<int:user_id>", methods=["GET"])
def getUserData(user_id):
    print("soon")

# create user
@app.route("/v1/users", methods=["POST"])
def createUser():
    print("soon")

# ADMIN ONLY: list all users
@app.route("/v1/users", methods=["GET"])
def admin_getAllUsers():
    print("soon")

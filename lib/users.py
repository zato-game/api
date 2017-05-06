# zato-api
# users.py
# core functions for user registration, management and login (relies on db connection)

# get user data
@app.route("/v1/users/<int:user_id>", methods=["GET"])
def getUserData(user_id):

# create user
@app.route("/v1/users", methods=["POST"])
def createUser():

# ADMIN ONLY: list all users
@app.route("/v1/users", methods=["GET"])
def admin_getAllUsers():
    

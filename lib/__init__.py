from flask import Flask

app = Flask(__name__)

# to make the lib files have access to app
def returnApp():
    return app

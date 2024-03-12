from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet_welcome():
    return "welcome"

@app.route("/welcome/home")
def greet_welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def greet_back():
    return "welcome back"

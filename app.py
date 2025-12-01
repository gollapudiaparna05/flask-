from flask import Flask
from userdb import user_bp 
app =Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/user")
@app.route("/")
def home():
    return "hello user "
@app.route("/about")
def about():
    return "about"
@app.route("/contact")
def contact():
    return "contact"
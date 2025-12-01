

from flask import Blueprint


user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/profile")
def profile():
    return "This is the user profile"

@user_bp.route("/settings")
def settings():
    return "User settings page"

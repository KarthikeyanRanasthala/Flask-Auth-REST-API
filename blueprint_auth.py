from flask import Blueprint, request, Response

authentication = Blueprint("authentication", __name__)


@authentication.route("/register", methods=["POST"])
def register_user():
    pass


@authentication.route("/login", methods=["POST"])
def login_user():
    pass

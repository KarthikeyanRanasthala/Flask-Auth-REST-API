from flask import Blueprint, request, Response, jsonify
from utils import (
    validate_user_input,
    generate_salt,
    generate_hash,
    db_write,
    validate_user,
)

authentication = Blueprint("authentication", __name__)


@authentication.route("/register", methods=["POST"])
def register_user():
    user_email = request.json["email"]
    user_password = request.json["password"]
    user_confirm_password = request.json["confirm_password"]

    if user_password == user_confirm_password and validate_user_input(
        "authentication", email=user_email, password=user_password
    ):
        password_salt = generate_salt()
        password_hash = generate_hash(user_password, password_salt)

        if db_write(
            """INSERT INTO users (email, password_salt, password_hash) VALUES (%s, %s, %s)""",
            (user_email, password_salt, password_hash),
        ):
            return Response(status=201)
        else:
            return Response(status=409)
    else:
        return Response(status=400)


@authentication.route("/login", methods=["POST"])
def login_user():
    user_email = request.json["email"]
    user_password = request.json["password"]

    user_token = validate_user(user_email, user_password)

    if user_token:
        return jsonify({"jwt_token": user_token})
    else:
        Response(status=401)

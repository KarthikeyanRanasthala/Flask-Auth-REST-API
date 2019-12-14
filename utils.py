from settings import JWT_SECRET_KEY
from flask_mysqldb import MySQLdb
from hashlib import pbkdf2_hmac

from app import db

import os


def db_read(query, params=None):
    pass


def db_write(query, params):
    pass


def generate_salt():
    pass


def generate_hash(plain_password, password_salt):
    pass


def validate_user(email, password):
    pass

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://<psql_username>:<psql_password>@localhost/flask_family_recipes_app'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:levon4202099@localhost/inote'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

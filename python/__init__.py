# source /Users/tnappy/node_projects/quickstart/python/bin/activate
# Read env vars from .env file
import os

from dotenv import load_dotenv
from flask import Flask
import plaid
from plaid.model.products import Products
from plaid.api import plaid_api


def create_app():
    load_dotenv()


    app = Flask(__name__)




    from .views import views

    app.register_blueprint(views, url_prefix = "/")

    return app

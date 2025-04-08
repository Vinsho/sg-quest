import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    load_dotenv()

    from api.api_crypto_currency import crypto_currency_api
    from views.view_crypto_currency import crypto_currency_view

    app = Flask("flask_pydantic_app")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
    app.register_blueprint(crypto_currency_api, url_prefix="/api/currency")
    app.register_blueprint(crypto_currency_view, url_prefix="/")

    CORS(app)

    from database import db

    db.init_app(app)
    migrate.init_app(app, db)

    return app

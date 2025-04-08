from flask import Blueprint, render_template

from database import db
from models.model_crypto_currency import CryptoCurrency

crypto_currency_view = Blueprint("crypto_currency_view", __name__)


@crypto_currency_view.route("/add")
def add_currency():
    return render_template("currency/add_currency.html")


@crypto_currency_view.route("/")
def all_currencies():
    currencies = (
        db.session.query(CryptoCurrency).join(CryptoCurrency.coin_gecko_currency).all()
    )
    return render_template("currency/currencies.html", currencies=currencies)

from flask import Blueprint, render_template, request

from api.error_handler import htmx_error_handler
from database import db
from models.model_crypto_currency import CryptoCurrency
from serializers.serializer_crypto_currency import (
    CreateCurrencyRequest,
    CryptoCurrencyPatchRequest,
    CryptoCurrencySerializer,
    SearchCurrencyBySymbolRequest,
)
from services.service_coin_gecko import CoinGeckoService

crypto_currency_api = Blueprint("crypto_currency", __name__)


@crypto_currency_api.get("/")
def crypto_currency_get():
    currencies = (
        db.session.query(CryptoCurrency).join(CryptoCurrency.coin_gecko_currency).all()
    )

    return [
        CryptoCurrencySerializer.model_validate(currency).model_dump()
        for currency in currencies
    ]


@crypto_currency_api.post("/")
@htmx_error_handler()
def crypto_currency_post():
    data = CreateCurrencyRequest.model_validate(request.form.to_dict())
    cg_id = data.cg_id

    cg_currency = CoinGeckoService().get_coin(cg_id)
    image = cg_currency["image"]["large"]
    currency = CryptoCurrency(coin_gecko_currency_id=cg_id, image=image)
    db.session.add(currency)
    db.session.commit()

    return render_template("partials/message.html", message="Currency Added")


@crypto_currency_api.patch("/<id>")
def crypto_currency_patch(id):
    data = CryptoCurrencyPatchRequest.model_validate(
        request.form.to_dict()
    ).model_dump()

    db.session.query(CryptoCurrency).filter_by(id=id).update(**data)
    db.session.commit()

    return ""


@crypto_currency_api.delete("/<id>")
def crypto_currency_delete(id):
    db.session.query(CryptoCurrency).filter_by(id=id).delete()
    db.session.commit()

    return ""


@crypto_currency_api.post("/search")
def crypto_currency_search_by_symbol():
    data = SearchCurrencyBySymbolRequest.model_validate(request.form.to_dict())
    symbol = data.symbol

    if symbol == "":
        return ""

    cg_currencies = CoinGeckoService().get_coins_for_symbol(symbol)

    if cg_currencies == []:
        return render_template(
            "partials/message.html", message="Symbol not present on CoinGecko"
        )

    return render_template("partials/currency_select.html", cg_currencies=cg_currencies)

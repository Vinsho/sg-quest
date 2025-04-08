import typing
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import db
from models.table_names import TableNames


if typing.TYPE_CHECKING:
    from models.model_crypto_currency import CryptoCurrency


class CoinGeckoCurrency(db.Model):
    __tablename__ = TableNames.COIN_GECKO_CURRENCY

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    symbol: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    crypto_currencies: Mapped[list["CryptoCurrency"]] = relationship(
        "CryptoCurrency", back_populates="coin_gecko_currency"
    )

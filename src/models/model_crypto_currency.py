from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import ModelBase, db
from models.model_coin_gecko_currency import CoinGeckoCurrency
from models.table_names import TableNames


class CryptoCurrency(db.Model, ModelBase):
    __tablename__ = TableNames.CRYPTO_CURRENCY

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(Text, nullable=True)
    coin_gecko_currency_id: Mapped[str] = mapped_column(
        ForeignKey(f"{TableNames.COIN_GECKO_CURRENCY}.id"), unique=True
    )
    coin_gecko_currency: Mapped["CoinGeckoCurrency"] = relationship(
        back_populates="crypto_currencies"
    )

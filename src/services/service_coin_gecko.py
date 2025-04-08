import os

from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from database import db
from models.model_coin_gecko_currency import CoinGeckoCurrency
from sqlalchemy.dialects.postgresql import insert

from services.singleton import Singleton


class CoinGeckoService(metaclass=Singleton):
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GECKO_DEMO_API_KEY")
        if api_key is None:
            raise Exception("GECKO_DEMO_API_KEY is not set")

        self.client = CoinGeckoAPI(demo_api_key=api_key)
        self.load_coin_list_to_db()

    def get_coins(self):
        return self.client.get_coins_list()

    def get_coin(self, coin_id):
        return self.client.get_coin_by_id(coin_id)

    def load_coin_list_to_db(self):
        coin_gecko_currency = db.session.query(CoinGeckoCurrency).first()
        if coin_gecko_currency is not None:
            return

        print("Loading coins from CoinGecko to DB")
        coins = self.get_coins()
        print(f"Loaded {len(coins)} coins from CoinGecko")

        try:
            stmt = insert(CoinGeckoCurrency).values(coins)
            stmt = stmt.on_conflict_do_nothing(index_elements=["id"])

            db.session.execute(stmt)
            db.session.commit()

            print(f"Loaded {len(coins)} coins from CoinGecko to DB")
        except Exception:
            db.session.rollback()
            raise

    def get_coins_for_symbol(self, symbol) -> list[CoinGeckoCurrency]:
        return (
            db.session.query(CoinGeckoCurrency)
            .filter(CoinGeckoCurrency.symbol == symbol)
            .all()
        )

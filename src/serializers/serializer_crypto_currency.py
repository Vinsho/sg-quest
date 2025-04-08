from pydantic import BaseModel


class SearchCurrencyBySymbolRequest(BaseModel):
    symbol: str


class CreateCurrencyRequest(BaseModel):
    cg_id: str


class CoinGeckoCurrencySerializer(BaseModel):
    id: str
    name: str
    symbol: str

    model_config = {"from_attributes": True}


class CryptoCurrencySerializer(BaseModel):
    id: int
    image: str
    coin_gecko_currency: CoinGeckoCurrencySerializer

    model_config = {"from_attributes": True}


class CryptoCurrencyPatchRequest(BaseModel):
    image: str

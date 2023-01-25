from os import environ
from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class Currencies(Enum):
    BTC = "btc"
    ETH = "eth"


class OrderType(Enum):
    BUY = "market"
    SELL = "stop_limit"
    CANCELED = "stop_market"


CLIENT_ID = environ.get("CLIENT_ID", "CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET", "CLIENT_SECRET")

GAP = float(environ.get("GAP", 100))
GAP_IGNORE = float(environ.get("GAP_IGNORE", 50))

DB_NAME = environ.get('DB_NAME')
DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_PORT = environ.get('DB_PORT')
DB_HOST = environ.get('DB_HOST')

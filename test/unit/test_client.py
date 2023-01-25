import unittest
from app.constants import OrderType
from app.client import Client


class TestClient(unittest.TestCase):

    def test_set_order(self):
        client = Client("test", "test")
        type = OrderType.BUY

        response = client.set_order(type=type, instrument_name="test", amount=1, price=1)

        self.assertEqual(response["result"]["order"]["order_type"], type.value)

        type = OrderType.SELL

        response = client.set_order(type=type, instrument_name="test", amount=1, price=1)

        self.assertEqual(response["result"]["order"]["order_type"], type.value)



from typing import Union
from client import Client
from constants import Currencies, OrderType
from utils import to_fixed
from random import uniform
from Order import Order
from constants import GAP, GAP_IGNORE


class Bot:
    def __init__(self, client: Client):
        self.__client = client

    def get_current_price(self, currency: Currencies) -> float:
        if currency == Currencies.BTC:
            return to_fixed(uniform(23000, 25000))
        return to_fixed(uniform(1000, 15000))

    def set_order_buy(self, price: float, amount: Union[float, int]) -> dict:
        # Send api call or websocket
        return self.__client.set_order(OrderType.BUY, instrument_name='btc-eth', amount=amount, price=price)

    def set_order_sell(self, price: float, amount: Union[float, int]) -> dict:
        # Send api call or websockete
        return self.__client.set_order(OrderType.SELL, instrument_name='btc-eth', amount=amount, price=price)

    def cancel_order(self, order_id: int):
        return self.__client.cancel_order(order_id=order_id)

    def next_step(self, order: Order, amount: int) -> Order:  # Amount value somehow fix
        """
        Choose next step of action bot
        :param order: Order
        :param amount: Amount
        :return: Order
        """
        current_price = self.get_current_price(Currencies.BTC)  # Currency value need fix
        if current_price > order.price + GAP + GAP_IGNORE:
            response = self.cancel_order(order_id=order.order_id)["result"]
            return Order(
                price=response["trigger_price"],
                order_id=response["order_id"],
                amount=response["amount"],
                order_type=response["order_type"],
            )

        if current_price <= order.price:
            sell_price = current_price + GAP
            response = self.set_order_sell(price=sell_price, amount=amount)["result"]
            return Order(
                price=response["order"]["price"],
                order_id=response["order"]["order_id"],
                amount=response["order"]["amount"],
                order_type=response["order"]["order_type"],
            )

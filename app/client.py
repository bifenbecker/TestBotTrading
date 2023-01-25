from typing import Optional, Union
from constants import OrderType
from mocked_response import SET_ORDER_BUY_RESPONSE, SET_ORDER_SELL_RESPONSE, ORDER_CANCEL_RESPONSE


class Client:
    """
    Client that works with connection API or Websocket
    """

    def __init__(self, client_id: str, client_secret: str):
        self.__client_id = client_id
        self.__client_secret = client_secret

    def set_order(self, type: OrderType, instrument_name: str, amount: Union[float, int],
                  price: Optional[float]) -> dict:
        """
        Set order in general
        :param type: OrderType: BUY, SELL
        :param instrument_name: str
        :param amount: float or int
        :param price: float
        :return: dict - response from API or Websocket
        """
        if type == OrderType.BUY:
            return self._set_buy_order(instrument_name=instrument_name, amount=amount, price=price)
        else:
            return self._set_sell_order(instrument_name=instrument_name, amount=amount, price=price)

    def _set_buy_order(self, instrument_name: str, amount: Union[float, int], price: float) -> dict:
        print('Set order BUY - ', instrument_name)
        return SET_ORDER_BUY_RESPONSE

    def _set_sell_order(self, instrument_name: str, amount: Union[float, int], price: float) -> dict:
        print('Set order BUY - ', instrument_name)
        return SET_ORDER_SELL_RESPONSE

    def cancel_order(self, order_id: int) -> dict:
        """
        Cancel order by order_id
        :param order_id: int Order ID
        :return: dict - response from API or Websocket
        """
        print('Cancel order ', order_id)
        return ORDER_CANCEL_RESPONSE

class Order:
    """
    Simple model of order
    Additional abstract layer between API and database
    """

    def __init__(self, price: float, order_id: str, amount: float, order_type: str):
        self.__price = price
        self.__order_id = order_id
        self.__amount = amount
        self.__order_type = order_type

    @property
    def price(self):
        return self.__price

    @property
    def order_id(self):
        return self.__order_id

    @property
    def amount(self):
        return self.__amount

    @property
    def order_type(self):
        return self.__order_type
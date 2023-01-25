from time import sleep
from random import randint
from constants import *
from client import Client
from db_connection import PostgresConnection
from Order import Order
from bot import Bot

ORDERS = []


def run_bot():
    """
    Main loop of program
    :return:
    """
    client = Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    bot = Bot(client=client)
    print("BOT is running....")
    currency = Currencies.BTC
    while True:
        current_price = bot.get_current_price(currency)
        buy_price = current_price - GAP / 2
        amount = randint(10, 20)

        sleep(1)
        print(f"Current price of {currency.value} is {current_price}")

        response = bot.set_order_buy(buy_price, amount=amount)["result"]
        order = Order(
            price=response["order"]["price"],
            order_id=response["order"]["order_id"],
            amount=response["order"]["amount"],
            order_type=response["order"]["order_type"],
        )
        ORDERS.append(order)
        with PostgresConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO orders (id, price, amount, order_type)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (order.order_id, order.price, order.amount, order.order_type))
            conn.commit()
        sleep(1)
        for order in ORDERS:
            if current_price > order.price + GAP + GAP_IGNORE:
                bot.cancel_order(order_id=order.order_id)
                break

            if current_price <= order.price:
                sell_price = current_price + GAP
                response = bot.set_order_sell(price=sell_price, amount=amount)
                ORDERS.append(Order(
                    price=response["order"]["price"],
                    order_id=response["order"]["order_id"],
                    amount=response["order"]["amount"],
                    order_type=response["order"]["order_type"],
                ))


if __name__ == '__main__':
    run_bot()

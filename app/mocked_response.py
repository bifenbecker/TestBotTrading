SET_ORDER_BUY_RESPONSE = {
  "jsonrpc": "2.0",
  "id": 5275,
  "result": {
    "trades": [
      {
        "trade_seq": 1966056,
        "trade_id": "ETH-2696083",
        "timestamp": 1590483938456,
        "tick_direction": 0,
        "state": "filled",
        "self_trade": False,
        "reduce_only": False,
        "price": 203.3,
        "post_only": False,
        "order_type": "market",
        "order_id": "ETH-584849853",
        "matching_id": None,
        "mark_price": 203.28,
        "liquidity": "T",
        "label": "market0000234",
        "instrument_name": "ETH-PERPETUAL",
        "index_price": 203.33,
        "fee_currency": "ETH",
        "fee": 0.00014757,
        "direction": "buy",
        "amount": 40
      }
    ],
    "order": {
      "web": False,
      "time_in_force": "good_til_cancelled",
      "replaced": False,
      "reduce_only": False,
      "profit_loss": 0.00022929,
      "price": 207.3,
      "post_only": False,
      "order_type": "market",
      "order_state": "filled",
      "order_id": "ETH-584849853",
      "max_show": 40,
      "last_update_timestamp": 1590483938456,
      "label": "market0000234",
      "is_liquidation": False,
      "instrument_name": "ETH-PERPETUAL",
      "filled_amount": 40,
      "direction": "buy",
      "creation_timestamp": 1590483938456,
      "commission": 0.00014757,
      "average_price": 203.3,
      "api": True,
      "amount": 40
    }
  }
}

SET_ORDER_SELL_RESPONSE = {
  "jsonrpc": "2.0",
  "id": 2148,
  "result": {
    "trades": [],
    "order": {
      "triggered": False,
      "trigger": "last_price",
      "time_in_force": "good_til_cancelled",
      "trigger_price": 145,
      "reduce_only": False,
      "profit_loss": 0,
      "price": 145.61,
      "post_only": False,
      "order_type": "stop_limit",
      "order_state": "untriggered",
      "order_id": "ETH-SLTS-28",
      "max_show": 123,
      "last_update_timestamp": 1550659803407,
      "label": "",
      "is_liquidation": False,
      "instrument_name": "ETH-PERPETUAL",
      "direction": "sell",
      "creation_timestamp": 1550659803407,
      "api": True,
      "amount": 123
    }
  }
}

ORDER_CANCEL_RESPONSE = {
  "jsonrpc": "2.0",
  "id": 4214,
  "result": {
    "triggered": False,
    "trigger": "index_price",
    "time_in_force": "good_til_cancelled",
    "trigger_price": 144.73,
    "reduce_only": False,
    "profit_loss": 0,
    "price": "market_price",
    "post_only": False,
    "order_type": "stop_market",
    "order_state": "untriggered",
    "order_id": "ETH-SLIS-12",
    "max_show": 5,
    "last_update_timestamp": 1550575961291,
    "label": "",
    "is_liquidation": False,
    "instrument_name": "ETH-PERPETUAL",
    "direction": "sell",
    "creation_timestamp": 1550575961291,
    "api": False,
    "amount": 5
  }
}

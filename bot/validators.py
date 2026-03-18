def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and not price:
        raise ValueError("Price required for LIMIT order")
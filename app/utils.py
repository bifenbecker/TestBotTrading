def to_fixed(num: float, digits: int = 2) -> float:
    """
    Rounding a number to a decimal point
    :param num: Number
    :param digits: Amount of digits after comma
    :return: new number
    """
    return float(f"%.{digits}f" % num)
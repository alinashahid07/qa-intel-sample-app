import random
import time

from app.bugs import bug_active

SUPPLIER_PRICES = {"book": 9.0, "pen": 1.0}


class OutOfStockError(Exception):
    pass


class Inventory:
    def __init__(self, stock: dict):
        self.stock = dict(stock)

    def reserve(self, name: str, qty: int) -> None:
        available = self.stock.get(name, 0)
        if bug_active("reserve_last_item_fails"):
            too_many = qty >= available
        else:
            too_many = qty > available
        if too_many:
            raise OutOfStockError(f"not enough {name} in stock, wanted {qty}, have {available}")
        self.stock[name] = available - qty


def fetch_supplier_price(name: str, timeout: float = 0.2) -> float:
    delay = 0.5 if bug_active("supplier_timeout") else 0.01
    if delay > timeout:
        raise TimeoutError(f"supplier lookup for {name} exceeded {timeout} seconds")
    if bug_active("flaky_network_call") and random.random() < 0.5:
        raise ConnectionError("supplier connection reset by peer")
    time.sleep(delay)
    return SUPPLIER_PRICES[name]
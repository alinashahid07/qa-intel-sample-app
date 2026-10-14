from app.bugs import bug_active
from app.pricing import add_tax, apply_discount


class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("quantity must be positive")
        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"price": price, "qty": qty}

    def remove(self, name: str) -> None:
        if bug_active("remove_missing_item_keyerror"):
            del self.items[name]
            return
        self.items.pop(name, None)

    def subtotal(self):
        if bug_active("empty_cart_returns_none") and not self.items:
            return None
        total = 0.0
        for item in self.items.values():
            total += item["price"] * item["qty"]
        return round(total, 2)

    def total(self, discount_percent: float = 0, tax_rate: float = 0.0) -> float:
        discounted = apply_discount(self.subtotal(), discount_percent)
        return add_tax(discounted, tax_rate)
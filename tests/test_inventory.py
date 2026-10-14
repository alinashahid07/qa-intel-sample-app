import pytest

from app.inventory import Inventory, OutOfStockError, fetch_supplier_price


def test_reserve_reduces_stock():
    inv = Inventory({"book": 5})
    inv.reserve("book", 2)
    assert inv.stock["book"] == 3


def test_reserve_last_item_works():
    inv = Inventory({"book": 1})
    inv.reserve("book", 1)
    assert inv.stock["book"] == 0


def test_reserve_too_many_raises():
    inv = Inventory({"book": 1})
    with pytest.raises(OutOfStockError):
        inv.reserve("book", 2)


def test_supplier_price_lookup():
    assert fetch_supplier_price("book") == 9.0
import pytest

from app.cart import Cart


def make_cart():
    cart = Cart()
    cart.add("book", 12.5, 2)
    cart.add("pen", 1.5, 4)
    return cart


def test_subtotal_counts_quantity():
    assert make_cart().subtotal() == 31.0


def test_adding_same_item_merges_quantity():
    cart = Cart()
    cart.add("book", 12.5)
    cart.add("book", 12.5)
    assert cart.items["book"]["qty"] == 2


def test_add_rejects_zero_quantity():
    with pytest.raises(ValueError):
        Cart().add("book", 12.5, 0)


def test_remove_missing_item_does_nothing():
    cart = Cart()
    cart.remove("ghost")
    assert cart.items == {}


def test_empty_cart_total_is_zero():
    assert Cart().total() == 0


def test_total_with_discount_and_tax():
    assert make_cart().total(discount_percent=10, tax_rate=0.1) == 30.69
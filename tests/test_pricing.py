import pytest

from app.pricing import add_tax, apply_discount


def test_discount_ten_percent():
    assert apply_discount(100.0, 10) == 90.0


def test_discount_zero_percent_keeps_price():
    assert apply_discount(50.0, 0) == 50.0


def test_discount_rejects_over_hundred():
    with pytest.raises(ValueError):
        apply_discount(100.0, 120)


def test_tax_adds_rate():
    assert add_tax(100.0, 0.08) == 108.0


def test_tax_keeps_cents():
    assert add_tax(19.99, 0.1) == 21.99
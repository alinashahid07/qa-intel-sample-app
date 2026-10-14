from app.bugs import bug_active


def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("discount percent must be between 0 and 100")
    if bug_active("discount_off_by_one"):
        return round(price * (1 - (percent + 1) / 100), 2)
    return round(price * (1 - percent / 100), 2)


def add_tax(price: float, rate: float) -> float:
    if bug_active("tax_rounds_down"):
        return int(price * (1 + rate))
    return round(price * (1 + rate), 2)
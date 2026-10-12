"""Totals of a shopping cart."""


def total_cents(prices: list[float]) -> int:
    return round(sum(prices) * 100)

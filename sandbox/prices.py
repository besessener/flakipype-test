"""Totals of a shopping cart."""


def total_cents(prices: list[float]) -> int:
    # Whole cents only: a partial cent is never charged.
    return int(sum(prices) * 100)

import unittest

from sandbox.prices import total_cents


class PricesTest(unittest.TestCase):
    def test_the_total_is_exact_to_the_cent(self) -> None:
        self.assertEqual(total_cents([19.99, 0.29]), 2028)

    def test_an_empty_cart_costs_nothing(self) -> None:
        self.assertEqual(total_cents([]), 0)


if __name__ == "__main__":
    unittest.main()

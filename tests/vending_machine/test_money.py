import pytest

from vending_machine.money import Money


@pytest.mark.parametrize(
    "m, amount",
    [
        (Money.M_1, 1),
        (Money.M_5, 5),
        (Money.M_10, 10),
        (Money.M_50, 50),
        (Money.M_100, 100),
        (Money.M_500, 500),
        (Money.M_1000, 1000),
        (Money.M_2000, 2000),
        (Money.M_5000, 5000),
        (Money.M_10000, 10000),
    ],
)
def test_money_amount(m, amount):
    actual = m.amount
    expected = amount
    assert actual == expected

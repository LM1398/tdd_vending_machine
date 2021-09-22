from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine
import pytest


@pytest.mark.parametrize(
    "cash, change",
    [
        (Money.M_1, [Money.M_1]),
        (Money.M_5, [Money.M_5]),
        (Money.M_10, []),
        (Money.M_50, []),
        (Money.M_100, []),
        (Money.M_500, []),
        (Money.M_1000, []),
        (Money.M_2000, [Money.M_2000]),
        (Money.M_10000, [Money.M_10000]),
    ],
)
def test_change(cash, change):
    vending_machine = VendingMachine()
    vending_machine.insert(cash)
    assert vending_machine.change == change


@pytest.mark.parametrize(
    "cash, money_box",
    [
        (Money.M_1, []),
        (Money.M_5, []),
        (Money.M_10, [Money.M_10]),
        (Money.M_50, [Money.M_50]),
        (Money.M_100, [Money.M_100]),
        (Money.M_500, [Money.M_500]),
        (Money.M_1000, [Money.M_1000],),
        (Money.M_2000, [],),
        (Money.M_10000, [],),
    ],
)
def test_money_box(cash, money_box):
    vending_machine = VendingMachine()
    vending_machine.insert(cash)

    assert vending_machine.money_box == money_box

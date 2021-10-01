from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
from vending_machine.drinks import Drinks


def test_stats():
    vending_machine = VendingMachine()
    for _drink in vending_machine.fridge:
        if _drink.name == "Coke":
            coke = _drink
    vending_machine.insert(Money.M_1000)
    vending_machine.buy(coke)
    for _drink in vending_machine.fridge:
        min_stock = min(
            [vending_machine.stock[_drink] for _drink in vending_machine.stock]
        )
        if vending_machine.stock[_drink.name] == min_stock:
            popular = _drink
    assert popular == coke


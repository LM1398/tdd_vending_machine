from vending_machine.money import Money
from vending_machine.inserts import Inserts


def test_inserts():
    Inserts(Money.M_10)
    Inserts(Money.M_10)
    Inserts(Money.M_500)
    Inserts(Money.M_500)

    total = (
        Money.M_10.amount + Money.M_10.amount + Money.M_500.amount + Money.M_500.amount
    )
    assert total == Inserts.total


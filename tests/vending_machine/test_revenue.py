from vending_machine.money import Money
from vending_machine.inserts import Inserts
from vending_machine.revenue import Revenue


def test_revenue():
    Inserts(Money.M_10)
    Inserts(Money.M_50)
    Inserts(Money.M_100)
    Inserts(Money.M_1000)

    total = (
        Money.M_10.amount
        + Money.M_100.amount
        + Money.M_500.amount
        + Money.M_1000.amount
    )
    assert total == Inserts.revenue


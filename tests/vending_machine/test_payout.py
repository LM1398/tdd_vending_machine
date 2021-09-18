from vending_machine.inserts_and_revenue import Inserts
from vending_machine.money import Money


def test_payout():
    Inserts(Money.M_10)
    Inserts(Money.M_10)
    Inserts(Money.M_500)
    Inserts(Money.M_500)

    total = (
        Money.M_10.amount + Money.M_10.amount + Money.M_500.amount + Money.M_500.amount
    )
    pay = Inserts.payout()
    assert total == pay
    assert Inserts.total == 0

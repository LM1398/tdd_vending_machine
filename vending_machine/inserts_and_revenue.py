from vending_machine.money import Money


class Inserts:
    total = 0
    revenue = 0

    def __init__(self, Money):
        Inserts.total += Money.amount
        Inserts.revenue += Money.amount

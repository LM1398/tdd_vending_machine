from vending_machine.money import Money


class Inserts:
    total = 0

    def __init__(self, Money):
        Inserts.total += Money.amount

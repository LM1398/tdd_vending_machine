from vending_machine.money import Money


class VendingMachine:
    def __init__(self):
        self.money_box = []
        self.change = []

    def insert(self, cash):
        accepted = [
            Money.M_10,
            Money.M_50,
            Money.M_100,
            Money.M_500,
            Money.M_1000,
        ]
        if cash in accepted:
            self.money_box.append(cash)
        else:
            self.change.append(cash)

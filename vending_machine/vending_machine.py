from vending_machine.money import Money


class VendingMachine:
    money_box = []
    change = []

    def insert(cash):
        accepted = [
            (Money.M_10),
            (Money.M_50),
            (Money.M_100),
            (Money.M_500),
            (Money.M_1000),
        ]
        if cash in accepted:
            VendingMachine.money_box.append(cash)
        else:
            VendingMachine.change.append(cash)

from vending_machine.money import Money


class VendingMachine:
    money_box = []

    def insert(cash):
        VendingMachine.money_box.append(cash)

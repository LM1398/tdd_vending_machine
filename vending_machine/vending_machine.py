from vending_machine.money import Money


class VendingMachine:
    money_box = 0

    def insert(cash):
        VendingMachine.money_box += cash.amount

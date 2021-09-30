from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
from vending_machine.drinks import Drinks

coke = Drinks("Coke", 120)
water = Drinks("Water", 100)
redbull = Drinks("Redbull", 200)


vending_machine = VendingMachine()
vending_machine.add_drink(coke, 5)
vending_machine.add_drink(redbull, 5)
vending_machine.add_drink(water, 5)
print(
    "Welcone to the Vending Machine!",
    "",
    "Please choose a funciton:",
    "1. Buy a drink",
    "2. Check revenue",
    "3. Check stock",
    sep="\n",
)

function = input(" ")
if function == "3":
    print(vending_machine.stock)
elif function == "2":
    print(vending_machine.revenue)
elif function == "1":
    print(
        "------------------------------------------------------------ Menu -----------------------------------------------------------------"
    )
    for _drink in set(vending_machine.fridge):
        print(_drink.name, _drink.price, "yen")
    print("")
    choice = input("Choose a drink:")

    for _drink in vending_machine.fridge:
        if _drink.name == choice or _drink.name.lower() == choice:
            print("", f"The price for this drink is {_drink.price} yen", sep="\n")
            selected = _drink
            break

    print(
        "",
        "Please insert money",
        "",
        "Accepeted currencies are: 1000, 500, 100, 50, 10",
        "E.g. Insert: 100, 10, 10",
        "",
        sep="\n",
    )

    coin = input("Insert:")
    inserted = coin.split(",")
    recognized = [int(x) for x in inserted]
    for money in vending_machine.accepted:
        if money.amount in recognized:
            for times in range(recognized.count(money.amount)):
                vending_machine.insert(money)

    print(
        "",
        f"Total amount inserted = {sum(cash.amount for cash in vending_machine.money_box)} yen",
        f"Do you want to buy {choice}?",
        sep="\n",
    )
    answer = input("y(yes) or n(no)")
    if answer == "y":
        returns = sum(x.amount for x in vending_machine.money_box) - selected.price
        vending_machine.buy(selected)
        print(
            "",
            f"Your change is {returns} yen",
            "Thank you for your purchase!",
            "",
            "",
            f"========================================================= {selected.name} =========================================================",
            "",
            "",
            sep="\n",
        )

    else:
        print("See you again")

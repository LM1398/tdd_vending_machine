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
print("Welcone to the Vending Machine!")
print("")
print("Please choose a funciton:")
print("1. Buy a drink")
print("2. Check revenue")
print("3. Check stock")
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

    if choice == "Redbull":
        print("")
        print(f"The price for this drink is {redbull.price} yen")

        selected = redbull

    elif choice == "Coke":
        print("")
        print(f"The price for this drink is {coke.price} yen")

        selected = coke

    elif choice == "Water":
        print("")
        print(f"The price for this drink is {water.price} yen")

        selected = water

    print("")
    print("Please insert money")
    print("")
    print("Accepeted currencies are: 1000, 500, 100, 50, 10")
    print("E.g. Insert: 100, 10, 10")
    print("")
    coin = input("Insert:")
    inserted = coin.split(",")
    recognized = [int(x) for x in inserted]
    if 1000 in recognized:
        for times in range(recognized.count(1000)):
            vending_machine.insert(Money.M_1000)
    if 500 in recognized:
        for times in range(recognized.count(500)):
            vending_machine.insert(Money.M_500)
    if 100 in recognized:
        for times in range(recognized.count(100)):
            vending_machine.insert(Money.M_100)
    if 50 in recognized:
        for times in range(recognized.count(50)):
            vending_machine.insert(Money.M_50)
    if 10 in recognized:
        for times in range(recognized.count(10)):
            vending_machine.insert(Money.M_10)
    print("")
    print(
        f"Total amount inserted = {sum(cash.amount for cash in vending_machine.money_box)} yen"
    )
    print("")
    print(f"Do you want to buy {choice}?")
    answer = input("y(yes) or n(no)")
    if answer == "y":
        returns = sum(x.amount for x in vending_machine.money_box) - selected.price
        vending_machine.buy(selected)
        print("")
        print(f"Your change is {returns} yen")
        print("Thank you for your purchase!")
        print("")
        print("")
        print(
            f"========================================================= {selected.name} ========================================================="
        )
    else:
        print("See you again")


import CoffeeData

def coffee_resources(user_chosen, resources):
    for ingredient in menu[user_chosen]["ingredients"]:
        if resources[ingredient] < menu[user_chosen]["ingredients"][ingredient]:
            return ingredient
    for ingredient in menu[user_chosen]["ingredients"]:
        resources[ingredient] = resources[ingredient] - menu[user_chosen]["ingredients"][ingredient]
    return menu[user_chosen]["cost"]

def transaction(coins, cost):
    for coin in coins:
        user_coin = input(f"How many {coin}?: ")
        try:
            coins[coin] = int(user_coin)
        except ValueError:
            print("Coffee Machine: off")
            return "off"
    for coin in coins:
        if coin == "quarters":
            cost += coins[coin] * 0.25
        elif coin == "dimes":
            cost += coins[coin] * 0.10
        elif coin == "nickles":
            cost += coins[coin] * 0.05
        elif coin == "pennies":
            cost += coins[coin] * 0.01
    return cost

resources = CoffeeData.resources
menu = CoffeeData.MENU
coins = CoffeeData.coins
off = 'on'
cost = 0
costs = 0

while off == "on":
    user_chosen = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_chosen == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${round(costs, 2)}")
    elif user_chosen == "off":
        off = "off"
        print("Coffee Machine: off")
    else:
        result_resources = coffee_resources(user_chosen, resources)
        if result_resources == "water" or result_resources == "coffee" or result_resources == "milk":
            print(f"Sorry there is not enough {result_resources}.")
        else:
            result_transaction = transaction(coins, cost)
            if result_transaction == "off":
                off = "off"
            elif result_transaction < result_resources:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                costs += result_resources
                print(f"Here is ${round(result_transaction - result_resources, 2)} dollars in change.")
                print(f"Here is your {user_chosen}☕ Enjoy!")
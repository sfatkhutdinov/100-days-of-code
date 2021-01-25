MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Checks if there are enough available resources

    Args:
        order_ingredients (int): amount of ingredients

    Returns:
        Bool: returns either true or
        false depending on the availability of resources
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Calculates inserted coins

    Returns:
        total: value of coins
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Checks if the transaction went through

    Args:
        money_received (float): amount of money inserted
        drink_cost (float): the fixed price of a drink

    Returns:
        Bool: returns either true of false depending on
        the amount of money inserted and the cost of the drink
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Makes a coffee using the resources required for
    a selected drink.

    Args:
        drink_name (str): user inputted name
        order_ingredients (dict): the ingredients needed
        to make the selected drink
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


def coffee_machine():
    """Simulates the coffee machine experience
    The machine (function) executes a while-loop
    while it's still on. The drinks are made using
    the internal logic of other functions and the
    machine will operate until it is shut off.
    """
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water:  {resources['water']}ml")
            print(f"Milk:   {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money:  ${round(profit, 2)}")
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])


coffee_machine()

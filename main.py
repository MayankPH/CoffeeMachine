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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    for ingredient, amount in ingredients.items():
        if amount > resources[ingredient]:
            print(f"Sorry!!! There is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickels = int(input("Nickels: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01

    total_coins = quarters + dimes + nickels + pennies
    return total_coins


def make_coffee(choice, coins):
    cost = MENU[choice]["cost"]
    if coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = coins - cost
    resources["money"] += cost
    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {choice}. Enjoy!")

    # Deduct resources
    for ingredient, amount in MENU[choice]["ingredients"].items():
        resources[ingredient] -= amount

    return True


def coffee_machine():
    while True:
        user_choice = input('''
                *** MENU ***
            ESPRESSO        $1.5
            LATTE           $2.5
            CAPPUCCINO      $3.0
            
            Enter your choice: (espresso/latte/cappuccino)
        ''').lower()

        if user_choice == 'off':
            break
        elif user_choice == 'report':
            report()
        elif user_choice in MENU:
            if check_resources(user_choice):
                coins_inserted = process_coins()
                transaction_successful = make_coffee(user_choice, coins_inserted)
                if not transaction_successful:
                    break
            else:
                print("Transaction failed. Please try again.")
        else:
            print("Invalid choice. Please enter a valid option.")


coffee_machine()

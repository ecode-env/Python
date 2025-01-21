from art import *
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
}

def gradient_checker(user_choice):
    for i in user_choice['ingredients']:
        if resources[i] < user_choice['ingredients'][i]:
            print(f"Sorry, we don't have enough {i}!")
            return 0
    for j in user_choice['ingredients']:
        resources[j] -= user_choice['ingredients'][j]
    return 1





machine_on = True
money = 0
while machine_on:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if gradient_checker(MENU[choice]):

            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            money += quarters + dimes + nickels + pennies
            if money < MENU[choice]['cost']:
               print("Sorry that's not enough money. Money refunded.")
            else:
                money -= MENU[choice]['cost']
                print(f"Here is ${money:.2} in change. Enjoy!")




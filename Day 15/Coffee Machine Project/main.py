from random import choice

power = True

while power:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino):").lower()
    # powerOff = input("Do you want to turn the machine off? ").lower()
    if coffeeChoice == "off":
        power = False
    elif coffeeChoice == "report":
        print(resources)

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


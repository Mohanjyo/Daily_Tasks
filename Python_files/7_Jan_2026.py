resources = {
    "milk": 1000,
    "water": 1500,
    "coffee": 500,
    "money": 0.0
}

menu = {
    "espresso": {
        "cost": 150,
        "ingredients": {
            "milk": 0,
            "water": 150,
            "coffee": 36
        }
    },
    "latte": {
        "cost": 180,
        "ingredients": {
            "milk": 100,
            "water": 150,
            "coffee": 36
        }
    },
    "cappuccino": {
        "cost": 200,
        "ingredients": {
            "milk": 50,
            "water": 100,
            "coffee": 24
        }
    }
}

def report():
    print(f"Milk: {resources['milk']} ml")
    print(f"Water: {resources['water']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {resources['money']:.2f} INR")

def check_resources(coffee_ingredients):
    for item, quantity in coffee_ingredients.items():
        if resources[item] < quantity:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins (in Indian Rupees):")
    try:
        ten = int(input("How many 10 rupee coins: ")) * 10
        five = int(input("How many 5 rupee coins: ")) * 5
        two = int(input("How many 2 rupee coins: ")) * 2
        one = int(input("How many 1 rupee coins: ")) * 1
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0.0
    return ten + five + two + one

def is_transaction_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        change = money_received - coffee_cost
        resources["money"] += coffee_cost
        if change > 0:
            print(f"Here is ₹{change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"☕ Here is your {coffee_name}. Enjoy!")

# ------------------ Main Program ------------------
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice == "off":
        machine_on = False
        print("Machine turned off.")
    elif choice == "report":
        report()
    elif choice in menu:
        coffee = menu[choice]
        if check_resources(coffee["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, coffee["cost"]):
                make_coffee(choice, coffee["ingredients"])
    else:
        print("Invalid choice. Please try again.")

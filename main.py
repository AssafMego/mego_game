import random

class Popsicle:
    def __init__(self, color, flavor, coast, dairy, is_healthy, expire_day):
        self.color = color
        self.flavor = flavor
        self.coast = coast
        self.dairy = dairy
        self.is_healthy = is_healthy
        self.expire_day = expire_day
#example_popsicle = Popsicle(orange, sweet, example_smth, True, False, 06.04.2024)

def determine_num_of_buyers(num_of_popsicles, num_of_customers, price):
    num_of_buyers = 0
    for customer in range(num_of_customers):
        willing_to_pay = random.uniform(1,3)
        if willing_to_pay > price:
            if num_of_buyers < num_of_popsicles:
                num_of_buyers += 1
    return num_of_buyers


def simulate_day(num_of_popsicles, price, num_of_customers = 100):
    num_of_buyers = determine_num_of_buyers(num_of_popsicles, num_of_customers, price)
    print(f"Customers today: {num_of_buyers}")
    income = num_of_buyers * price               # Income for the day
    return income

    return income


def main():
    buying_price = 1
    while True:
        print(f"the price of each popsicles is: {buying_price}")
        print("Enter how many popsicles you want to buy (or 'q' to quit):")
        num_of_popsicles_input = input("> ")

        if num_of_popsicles_input.lower() == "q":
            break

        num_of_popsicles = int(num_of_popsicles_input)

        print("Enter the price in which you want to sell each popsicle:")
        price_input = input("> ")

        price = float(price_input)
        expense = buying_price * num_of_popsicles
        income = simulate_day(num_of_popsicles, price)
        print(f"Income for the day: ${income - expense}\n")

    # print(f"\nTotal income: ${total_income}")
    print("Game Over!")

if __name__ == "__main__":
    main()

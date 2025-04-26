#Artha Surya Pratama 
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("\t\t BUS TICKET \t")
print("-" * 20)

ticket_data = [
    ("Prabumulih", [100000, 400000, 700000]),
    ("Muara Enim", [200000, 500000, 800000]),
    ("Lubuklinggau", [300000, 600000, 900000])
]

class_list = ["Economy", "Business", "Executive"]

def calculate_price(city_index, class_index, quantity):
    price_per_ticket = ticket_data[city_index][1][class_index]
    total = 0  # Sequencing

    for i in range(quantity):  # Iteration
        if i == 0:  # Selection
            print("Processing first ticket...")
        elif (i + 1) % 5 == 0:
            print(f"Special: Ticket #{i + 1} processed!")  # More selection
        total += price_per_ticket  # Sequencing continues

    return total 

#Jonathan Alvino 

for i, (city, _) in enumerate(ticket_data, 1):
    print(f"{i}. {city}")

city_choice = int(input("Enter city choice (1-3): ")) - 1

for i, cls in enumerate(class_list, 1):
    print(f"{i}. {cls}")

class_choice = int(input("Enter class choice (1-3): ")) - 1
ticket_quantity = int(input("Enter number of tickets: "))

sub_total = calculate_price(city_choice, class_choice, ticket_quantity) 

discount = 0
if (city_choice == 1 and class_choice == 0) or (city_choice == 2 and class_choice == 2):
    promo = input("Enter promo code: ").strip().lower()
    if promo == "igsontop":
        discount = 0.1 * sub_total

total_payment = sub_total - discount

print(f"\nSubtotal: Rp {sub_total:,}")
print(f"Discount: Rp {discount:,}")
print(f"Total Payment: Rp {total_payment:,}")
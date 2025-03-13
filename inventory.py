import os
from tabulate import tabulate

# Define the Shoe class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} | {self.code} | {self.product} | R{self.cost:.2f} | {self.quantity} units"

# List to store shoe objects
shoe_list = []

# Function to read data from the inventory file
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 5:
                    shoe_list.append(Shoe(*data))
        print("Inventory data loaded successfully.\n")
    except FileNotFoundError:
        print("Error: 'inventory.txt' not found. Please ensure the file exists.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

# Function to capture a new shoe
def capture_shoe():
    country = input("Enter country: ")
    code = input("Enter product code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    
    try:
        new_shoe = Shoe(country, code, product, float(cost), int(quantity))
        shoe_list.append(new_shoe)
        print("Shoe added successfully!\n")

        # Update the file
        with open("inventory.txt", "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
    except ValueError:
        print("Invalid input! Ensure cost and quantity are numeric values.\n")

# Function to display all shoes
def view_all():
    if not shoe_list:
        print("No shoes in inventory.\n")
        return

    table = [[shoe.country, shoe.code, shoe.product, f"R{shoe.cost:.2f}", shoe.quantity] for shoe in shoe_list]
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()

# Function to restock the shoe with the lowest quantity
def re_stock():
    if not shoe_list:
        print("No shoes in inventory.\n")
        return

    lowest_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"Lowest stock item:\n{lowest_shoe}")

    try:
        add_quantity = int(input(f"Enter quantity to add to {lowest_shoe.product}: "))
        lowest_shoe.quantity += add_quantity

        # Update the inventory file
        update_inventory_file()
        print(f"{lowest_shoe.product} restocked successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Function to update the inventory file
def update_inventory_file():
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")  # Rewrite header
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# Function to search for a shoe by code
def search_shoe():
    code = input("Enter the shoe code to search: ").strip()
    found_shoe = next((shoe for shoe in shoe_list if shoe.code == code), None)

    if found_shoe:
        print("Shoe found:\n", found_shoe, "\n")
    else:
        print("No shoe found with that code.\n")

# Function to calculate the total value for each shoe
def value_per_item():
    if not shoe_list:
        print("No shoes in inventory.\n")
        return

    print("\nTotal Value of Each Shoe:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: R{value:.2f}")
    print()

# Function to display the shoe with the highest quantity
def highest_qty():
    if not shoe_list:
        print("No shoes in inventory.\n")
        return

    highest_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"Shoe with highest stock:\n{highest_shoe}\nThis shoe is on SALE!\n")

# Function to display the menu and execute user choices
def menu():
    read_shoes_data()  # Load inventory when the program starts

    while True:
        print("\nInventory Management System")
        print("1. View all shoes")
        print("2. Capture a new shoe")
        print("3. Restock a shoe")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Find highest quantity shoe")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoe()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program. Goodbye!\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.\n")

# Run the program
menu()

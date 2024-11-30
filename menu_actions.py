# menu_actions.py

from product_operations import view_products, add_product, update_product, delete_product

# Function to handle view action
def handle_view():
    print(view_products())

# Function to handle add action
def handle_add():
    name = input("Enter the product name: ")
    try:
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        print(add_product(name, price, quantity))
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be an integer.")

# Function to handle update action
def handle_update():
    print(view_products())
    try:
        index = int(input("Enter the product number to update: ")) - 1
        name = input("Enter the new product name: ")
        price = float(input("Enter the new product price: "))
        quantity = int(input("Enter the new product quantity: "))
        print(update_product(index, name, price, quantity))
    except ValueError:
        print("Invalid input. Ensure proper values for index, price, and quantity.")

# Function to handle delete action
def handle_delete():
    print(view_products())
    try:
        index = int(input("Enter the product number to delete: ")) - 1
        print(delete_product(index))
    except ValueError:
        print("Invalid input. Enter a valid product number.")
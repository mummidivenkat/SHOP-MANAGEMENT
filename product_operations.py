# product_operations.py

products = []  # List to store products

# Function to view all products
def view_products():
    if not products:
        return "No products available."
    result = "Current Products:\n"
    for index, product in enumerate(products, start=1):
        result += f"{index}. Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}\n"
    return result

# Function to add a new product
def add_product(name, price, quantity):
    products.append({"name": name, "price": price, "quantity": quantity})
    return f"Product '{name}' added successfully!"

# Function to update an existing product
def update_product(index, name, price, quantity):
    if 0 <= index < len(products):
        products[index] = {"name": name, "price": price, "quantity": quantity}
        return f"Product updated successfully!"
    return "Invalid product index."

# Function to delete a product
def delete_product(index):
    if 0 <= index < len(products):
        removed_product = products.pop(index)
        return f"Product '{removed_product['name']}' deleted successfully!"
    return "Invalid product index."

def build_cart():
    cart = {}

    while True:
        item = input("Enter item name (or 'done' to finish): ")

        if item.lower() == "done":
            break

        price = float(input("Enter item price: "))
        cart[item] = price

    return cart


def cart_total(cart):
    total = sum(cart.values())
    return total


# Main program
cart = build_cart()

print("\nShopping Cart:")
for item, price in cart.items():
    print(f"{item}: {price:.2f}")

print(f"Total: {cart_total(cart):.2f}")
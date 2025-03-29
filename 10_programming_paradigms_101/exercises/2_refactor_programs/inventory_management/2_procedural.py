import pprint


def view_items(inventory):
    print("\nInventory:")
    pprint.pprint(inventory)


def add_item(inventory):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    inventory[name] = {"price": price, "quantity": quantity}
    print(f"{quantity} {name}(s) added to inventory")


def update_quantity(inventory):
    name = input("Enter item name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = quantity
        print(f"{name} quantity updated to {quantity}")
    else:
        print("Item not found in inventory")


def calculate_total_value(inventory):
    return sum(
        item["price"] * item["quantity"] for item in inventory.values()
    )


def print_final_inventory(inventory):
    print("\nFinal Inventory:")
    for name, details in inventory.items():
        print(f"{name}: ${details['price']} x {details['quantity']}")
    total_value = calculate_total_value(inventory)
    print(f"Total value: ${total_value:.2f}")


def main():
    inventory = {}
    while True:
        print("\nOptions:")
        print("1. View items")
        print("2. Add item")
        print("3. Update quantity")
        print("4. Calculate total inventory value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_items(inventory)

        elif choice == "2":
            add_item(inventory)

        elif choice == "3":
            update_quantity(inventory)

        elif choice == "4":
            total_value = calculate_total_value(inventory)
            print(f"Total inventory value: ${total_value:.2f}")

        elif choice == "5":
            print_final_inventory(inventory)
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

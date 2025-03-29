import pprint


class InventoryManager:
    """
    A simple inventory management system.

    This class allows users to add items, update quantities,
    view the inventory, calculate the total value of all items,
    and display a final summary.

    Attributes:
        inventory (dict): Stores item data with price and quantity.

    Methods:
        add_item(): Prompts user to add a new item to the inventory.
        update_quantity(): Updates the quantity of an existing item.
        view_items(): Displays all items in the inventory.
        calculate_total_value(): Calculates and returns the total inventory value.
        print_final_inventory(): Prints all inventory items and their total value.
        main(): Runs the menu-driven interaction loop.
    """

    def __init__(self):
        self.inventory = {}

    def view_items(self):
        print("\nInventory:")
        pprint.pprint(self.inventory)

    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        self.inventory[name] = {"price": price, "quantity": quantity}
        print(f"{quantity} {name}(s) added to inventory")

    def update_quantity(self):
        name = input("Enter item name to update: ")
        if name in self.inventory:
            quantity = int(input("Enter new quantity: "))
            self.inventory[name]["quantity"] = quantity
            print(f"{name} quantity updated to {quantity}")
        else:
            print("Item not found in inventory")

    def calculate_total_value(self):
        return sum(
            item["price"] * item["quantity"] for item in self.inventory.values()
        )

    def print_final_inventory(self):
        for name, details in self.inventory.items():
            print(f"{name}: ${details['price']} x {details['quantity']}")
        total = self.calculate_total_value()
        print(f"Total value: ${total:.2f}")

    def main(self):
        while True:
            print("\nOptions:")
            print("1. View items")
            print("2. Add item")
            print("3. Update quantity")
            print("4. Calculate total inventory value")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.view_items()

            elif choice == "2":
                self.add_item()

            elif choice == "3":
                self.update_quantity()

            elif choice == "4":
                total = self.calculate_total_value()
                print(f"Total inventory value: ${total:.2f}")

            elif choice == "5":
                self.print_final_inventory()
                break

            else:
                print("Invalid choice. Please try again.")


im = InventoryManager()
im.main()

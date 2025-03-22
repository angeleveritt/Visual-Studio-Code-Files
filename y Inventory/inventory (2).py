# Assignment - Inventory - Angelique  Everitt
print()
print("Assignment - Inventory")
print()

class Product:
    """
    A class representing a product in an inventory.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new Product instance.

        Args:
            name (str): The name of the product
            price (float): The price of the product
            quantity (int): The available quantity of the product
        """
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def display_info(self):
        """Display the product information."""
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available Quantity: {self.quantity}")
        print(f"Total Value: ${self.get_value():.2f}")

    def get_value(self):
        """
        Calculate the total value of this product.

        Returns:
            float: The total value (price * quantity)
        """
        return self.price * self.quantity

    def update_quantity(self, change):
        """
        Update the quantity of the product.

        Args:
            change (int): The change in quantity (positive for restock, negative for sales)

        Returns:
            bool: True if update is successful, False if would result in negative quantity
        """
        new_quantity = self.quantity + change
        if new_quantity < 0:
            print(f"Error: Cannot reduce quantity below 0. Current quantity: {self.quantity}")
            return False

        self.quantity = new_quantity
        return True

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"


class Inventory:
    """
    A class representing an inventory that manages products.
    """

    def __init__(self):
        """Initialize a new Inventory instance with an empty product list."""
        self.products = []

    def add_product(self, name, price, quantity):
        """
        Add a new product to the inventory.

        Args:
            name (str): The name of the product
            price (float): The price of the product
            quantity (int): The initial quantity of the product

        Returns:
            Product: The newly created Product object
        """
        # Check if product already exists
        existing_product = self.find_product(name)
        if existing_product:
            print(f"Product '{name}' already exists in inventory.")
            return None

        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        return new_product

    def find_product(self, name):
        """
        Find a product in the inventory by name.

        Args:
            name (str): The name of the product

        Returns:
            Product or None: The found Product object or None if not found
        """
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def display_all_products(self):
        """Display all products in the inventory."""
        if not self.products:
            print("The inventory is empty.")
            return

        print("\nInventory Products:")
        print("-" * 60)
        print(f"{'#':<3} {'Name':<20} {'Price':<10} {'Quantity':<10} {'Value':<10}")
        print("-" * 60)
        for i, product in enumerate(self.products, 1):
            print(f"{i:<3} {product.name:<20} ${product.price:<9.2f} {product.quantity:<10} ${product.get_value():<9.2f}")
        print("-" * 60)

    def calculate_total_value(self):
        """
        Calculate the total value of all products in the inventory.

        Returns:
            float: The total value of the inventory
        """
        total = sum(product.get_value() for product in self.products)
        return total

    def display_inventory_summary(self):
        """Display a summary of the inventory including total value."""
        print("\nInventory Summary:")
        print(f"Total number of products: {len(self.products)}")
        print(f"Total inventory value: ${self.calculate_total_value():.2f}")

    def remove_product(self, name):
        """
        Remove a product from the inventory.

        Args:
            name (str): The name of the product to remove

        Returns:
            bool: True if product was found and removed, False otherwise
        """
        product = self.find_product(name)
        if product:
            self.products.remove(product)
            return True
        return False


class InventoryUI:
    """
    A simple text-based user interface for interacting with the inventory.
    """

    def __init__(self):
        """Initialize the UI with a new inventory."""
        self.inventory = Inventory()
        self.running = False

        # Add some sample products
        self.add_sample_products()

    def add_sample_products(self):
        """Add sample products to the inventory for demonstration."""
        self.inventory.add_product("Laptop", 999.99, 5)
        self.inventory.add_product("Smartphone", 599.99, 10)
        self.inventory.add_product("Headphones", 149.99, 15)

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 40)
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. View All Products")
        print("2. Add New Product")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Search for Product")
        print("6. View Inventory Summary")
        print("7. Exit")
        print("=" * 40)

    def get_menu_choice(self):
        """Get the user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def view_all_products(self):
        """Display all products in the inventory."""
        self.inventory.display_all_products()
        input("\nPress Enter to continue...")

    def add_new_product(self):
        """Add a new product to the inventory."""
        print("\nADD NEW PRODUCT")
        print("-" * 40)

        name = input("Enter product name: ")

        if self.inventory.find_product(name):
            print(f"Error: A product with the name '{name}' already exists.")
            input("\nPress Enter to continue...")
            return

        while True:
            try:
                price = float(input("Enter product price: $"))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        while True:
            try:
                quantity = int(input("Enter product quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")

        product = self.inventory.add_product(name, price, quantity)
        if product:
            print(f"\nProduct '{name}' added successfully!")

        input("\nPress Enter to continue...")

    def update_product_quantity(self):
        """Update the quantity of a product."""
        print("\nUPDATE PRODUCT QUANTITY")
        print("-" * 40)

        name = input("Enter the name of the product to update: ")
        product = self.inventory.find_product(name)

        if not product:
            print(f"Product '{name}' not found in inventory.")
            input("\nPress Enter to continue...")
            return

        print(f"\nCurrent product: {product}")

        while True:
            try:
                action = input("\nDo you want to (A)dd or (R)emove quantity? ").upper()
                if action not in ['A', 'R']:
                    print("Please enter 'A' for add or 'R' for remove.")
                    continue

                quantity = int(input("Enter quantity to change: "))
                if quantity < 0:
                    print("Quantity change must be positive.")
                    continue

                if action == 'A':
                    product.update_quantity(quantity)
                    print(f"Added {quantity} to '{product.name}'. New quantity: {product.quantity}")
                else:  # action == 'R'
                    if product.update_quantity(-quantity):
                        print(f"Removed {quantity} from '{product.name}'. New quantity: {product.quantity}")
                    else:
                        print("Operation failed.")

                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")

        input("\nPress Enter to continue...")

    def remove_product(self):
        """Remove a product from the inventory."""
        print("\nREMOVE PRODUCT")
        print("-" * 40)

        name = input("Enter the name of the product to remove: ")

        if self.inventory.remove_product(name):
            print(f"Product '{name}' removed successfully!")
        else:
            print(f"Product '{name}' not found in inventory.")

        input("\nPress Enter to continue...")

    def search_product(self):
        """Search for a product in the inventory."""
        print("\nSEARCH PRODUCT")
        print("-" * 40)

        name = input("Enter the name of the product to search for: ")
        product = self.inventory.find_product(name)

        if product:
            print("\nProduct found!")
            print("-" * 40)
            product.display_info()
        else:
            print(f"Product '{name}' not found in inventory.")

        input("\nPress Enter to continue...")

    def view_inventory_summary(self):
        """Display a summary of the inventory."""
        self.inventory.display_inventory_summary()
        input("\nPress Enter to continue...")

    def run(self):
        """Run the UI main loop."""
        self.running = True

        while self.running:
            self.display_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.view_all_products()
            elif choice == 2:
                self.add_new_product()
            elif choice == 3:
                self.update_product_quantity()
            elif choice == 4:
                self.remove_product()
            elif choice == 5:
                self.search_product()
            elif choice == 6:
                self.view_inventory_summary()
            elif choice == 7:
                print("\nThank you for using the Inventory Management System!")
                self.running = False


# Run the application
if __name__ == "__main__":
    ui = InventoryUI()
    ui.run()

print()
print("fin")
print()


# Parent Class
class Smartphone:
    def __init__(self, brand, model, price):
        """Initialize the attributes of the Smartphone class."""
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute for encapsulation
    
    def get_price(self):
        """Access the private price attribute."""
        return self.__price
    
    def set_price(self, new_price):
        """Set a new price, ensuring it's a positive value."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive.")
    
    def details(self):
        """Print details about the smartphone."""
        return f"{self.brand} {self.model} - Price: ${self.__price:.2f}"

# Child Class for Gaming Smartphones
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, cooling_system):
        """Initialize attributes of the parent and child class."""
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.cooling_system = cooling_system
    
    def details(self):
        """Override the details method to include gaming features."""
        return (f"{self.brand} {self.model} (Gaming Edition) - "
                f"Price: ${self.get_price():.2f}\n"
                f"GPU: {self.gpu}, Cooling System: {self.cooling_system}")

# Demonstrate Polymorphism
def smartphone_info(smartphone):
    print(smartphone.details())

# Create instances of the classes
regular_phone = Smartphone("Apple", "iPhone 14", 999)
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 1099, "Adreno 730", "Advanced Vapor Chamber")

# Access details
print("Regular Smartphone:")
smartphone_info(regular_phone)

print("\nGaming Smartphone:")
smartphone_info(gaming_phone)

# Demonstrate Encapsulation
print("\nChanging price of the regular phone...")
regular_phone.set_price(899)
print(regular_phone.details())

print("\nAttempting to set an invalid price...")
regular_phone.set_price(-50)  # Invalid

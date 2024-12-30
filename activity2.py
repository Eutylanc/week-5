# Base class
class Vehicle:
    def move(self):
        """Default move method for vehicles."""
        print("The vehicle is moving.")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        """Override move method for Car."""
        print("The car is driving 🚗.")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        """Override move method for Plane."""
        print("The plane is flying ✈️.")

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        """Override move method for Boat."""
        print("The boat is sailing 🚤.")

# Derived class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        """Override move method for Bicycle."""
        print("The bicycle is pedaling 🚴.")

# Polymorphism in action
def demonstrate_movement(vehicle):
    """Calls the move() method of the given vehicle."""
    vehicle.move()

# Create instances of each class
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# List of vehicles
vehicles = [car, plane, boat, bicycle]

# Demonstrate movement
print("Demonstrating vehicle movements:")
for v in vehicles:
    demonstrate_movement(v)

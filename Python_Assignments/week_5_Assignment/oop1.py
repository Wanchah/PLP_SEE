# Define a class named 'car' to represent a basic car
class car:

    # Constructor method to initialize car's name and model
    def __init__(self, name, model):
        self.name = name      # Store the car's name
        self.model = model    # Store the car's model

    # Method to display car information in a formatted string
    def display_info(self):
        return f"Car Name: {self.name}, Model: {self.model}"

    # Method to simulate the car driving
    def drive(self):
        return f"{self.name} of model {self.model} is driving"


# Define a subclass 'superCar' that inherits from the 'car' class
class superCar(car):

    # Constructor method for superCar, adds top_speed in addition to name and model
    def __init__(self, name, model, top_speed):
        super().__init__(name, model)     # Call the parent class constructor
        self.top_speed = top_speed        # Store the car's top speed

    # Override the display_info method to include top speed
    def display_info(self):
        return f"Super Car Name: {self.name}, Model: {self.model}, Top Speed: {self.top_speed} km/h"

    # Override the drive method to include top speed in the message
    def drive(self):
        return f"{self.name} of model {self.model} is driving at top speed of {self.top_speed} km/h"


# Create an instance of the 'car' class
car1 = car("Toyota", "Corolla")

# Create an instance of the 'superCar' subclass
car2 = superCar("Ford", "Mustang", 300)

# Print information and driving status of car1
print(car1.display_info())
print(car1.drive())

# Print information and driving status of car2
print(car2.display_info())
print(car2.drive())
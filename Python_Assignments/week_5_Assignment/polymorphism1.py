# Define a base class called 'mover'
# This acts as a generic template for anything that can move
class mover:
    def move(self):
        # Placeholder method to be overridden by subclasses
        pass


# Define a subclass 'car' that inherits from 'mover'
class car(mover):
    def move(self):
        # Override the move method to describe car movement
        return "Driving."


# Define a subclass 'bicycle' that inherits from 'mover'
class bicycle(mover):
    def move(self):
        # Override the move method to describe bicycle movement
        return "Pedaling."


# Define a subclass 'airplane' that inherits from 'mover'
class airplane(mover):
    def move(self):
        # Override the move method to describe airplane movement
        return "Flying."


# Define a subclass 'dog' that inherits from 'mover'
class dog(mover):
    def move(self):
        # Override the move method to describe dog movement
        return "Running on all fours."


# Define a subclass 'fish' that inherits from 'mover'
class fish(mover):
    def move(self):
        # Override the move method to describe fish movement
        return "Swimming."


# Create instances (objects) of each subclass
car1 = car()             # Create a car object
bicycle1 = bicycle()     # Create a bicycle object
airplane1 = airplane()   # Create an airplane object
fish1 = fish()           # Create a fish object
dog1 = dog()             # Create a dog object


# Call the move method on each object and print the result
# __class__.__name__ dynamically gets the class name of the object
print(f"{car1.__class__.__name__} movement type:  {car1.move()}")
print(f"{bicycle1.__class__.__name__} movement type:  {bicycle1.move()}")
print(f"{airplane1.__class__.__name__} movement type:  {airplane1.move()}")
print(f"{dog1.__class__.__name__} movement type:  {dog1.move()}")
print(f"{fish1.__class__.__name__} movement type:  {fish1.move()}")
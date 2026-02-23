class Car: 
    #  attributes
    def __init__(self,name, color, model, size):
        self.name = name
        self.color = color
        self.model = model
        self.size = size

    # behavoirs - methods

    def carDescription(self):
       print(f"This is a {self.model} it is of color {self.color}")



toyota = Car("Buddy", "green","Toyota", "4X4")

#  accesed the attributes
output = toyota.name
output = toyota.color
output = toyota.model

#  access ythe behaviours:

toyota.carDescription()

mazda = Car("Kadogo", "blue","MAZDA - XR", "4X4")
mazda.carDescription()

output = f" FIRST CAR: {mazda.name} SECOND-CAR: {toyota.name}"
mazda.name
# INHERITANCE:  You have parent class and a child class( the child class inherits evryhitng form the parent class)

print("======================")
print(output)
print("======================")
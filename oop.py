
"""
CLASS: blueprint that helps create an real object
"""

# defining a Class
class Monitor:
    # attribute
    # shape ="rectangular"
    # resolution="1080"
    # size = "large"
    # yom = 2020

#  an initialize invoked the moment the object is created
    def __init__(self, shape, resolution,size, yom, color):
        self.shape = shape
        self.resolution = resolution
        self.size = size
        self.yom = yom 
        self.color = color 

    # methods (function taht resides inside a class)
    def switchOnMonitor(self):
        print("turning on monitor")

    def displayInterface(self):
        print("diplaying OS")

# OBJECTS: Instances of classes ("a real world thing")
# create objects
hpMonitor = Monitor()
dellMonitor = Monitor()

hpMonitor.switchOnMonitor()
dellMonitor.switchOnMonitor()

print(f"===> {hpMonitor.shape}")
print(f"===> {dellMonitor.shape}")
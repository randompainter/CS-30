# OOP Backpack Class Assignment

class Backpack:
    def __init__(self, color, size):
        # Attributes
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    # Open backpack
    def openBag(self):
        self.open = True
        print("Backpack opened")
    # Close backpack
    def closeBag(self):
        self.open = False
        print("Backpack closed")
    # Put item in backpack
    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(item, "Item added to backpack")
    # Take item from backpack
    def takeout(self, item):
        if self.open == True:
            self.items.remove(item)
            print(item, "Item has been removed from backpack")

# Create 3 backpacks
small_blue_backpack = Backpack("blue", "small")
medium_red_backpack = Backpack("red", "medium")
large_green_backpack = Backpack("green", "large")

small_blue_backpack.openBag()
small_blue_backpack.putin("Grilled Cheese")
small_blue_backpack.putin("Winter Jacket")
small_blue_backpack.closeBag()
small_blue_backpack.openBag()
small_blue_backpack.takeout("Winter Jacket")
small_blue_backpack.closeBag()

        
        
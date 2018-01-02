class Animals:
    age = 0
    health = 100
    status = "life"

    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    def update_status(self):
        if self.health < 0:
            self.status = "die"
        return self.status

    def feed(self):
        self.health += 10
        print("You feed the animal\nhealth = ", self.health)

    def hunger(self, ):
        self.health -= 1000


class Sheep(Animals):
    def __init__(self, name):
        super().__init__(name, weight=5)
        self.wool = 0

    def shear(self):
        self.wool += 10
        print("You cut a Sheep and get some wools")
        return self.wool

    def get_wool(self):
        print(f"You have {self.wool} wools")


class HollandSheep(Sheep):
    def __init__(self, name):
        super().__init__(name)

    def shear(self):
        self.wool += 15
        print("You cut a HollandSheep and get some wools")
        return self.wool


class Pig(Animals):
    def __init__(self, name):
        super().__init__(name, weight=40)
        self.meat = 0

    def kill(self):
        self.status = "die"
        self.meat = self.weight
        return print(f"The pig {self.status}, You get {self.meat} meat")


class Cow(Animals):
    def __init__(self, name):
        super().__init__(name, weight=80)
        self.milk = 100

    def get_milk(self):
        self.milk -= 10
        if not self.milk < 0:
            print(f"You get {10} liters")
        else:
            print("Cow is tired")


class Birds(Animals):
    def __init__(self, name, ):
        super().__init__(name, weight=1)
        self.eggs = 0


class Chicken(Birds):
    def __init__(self, name):
        super().__init__(name)
        self.eggs = 3

    def get_eggs(self):
        print(f"You get {self.eggs} eggs")


class Duck(Birds):
    def __init__(self, name):
        super().__init__(name)
        self.eggs = 2


class Goose(Birds):
    def __init__(self, name):
        super().__init__(name)
        self.eggs = 1


class Goat(Animals):
    def __init__(self, name):
        super().__init__(name, weight=30)
        self.meat = 0
        self.milk = 6

    def kill(self):
        self.status = "die"
        self.meat = self.weight
        return print(f"The goat {self.status}, You get {self.meat} meat")

    def get_milk(self):
        self.milk -= 2
        if not self.milk < 0:
            print(f"You get {2} liters")
        else:
            print("The goat is tired")


class Animals:
    age = 0
    health = 100
    status = "life"
    weight = 0
    name = "unnamed"

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


class Mammals(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.meat = int(self.weight * 0.6)


class Sheep(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.wool = 0

    def shear(self):
        self.wool += 10
        print("You cut a Sheep and get some wools")
        return self.wool

    def get_wool(self):
        print(f"You have {self.wool} wools")

    def kill(self):
        self.status = "die"
        return print(f"The sheep {self.status}, You get {self.meat} meat")


class HollandSheep(Sheep):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def shear(self):
        self.wool += 15
        print("You cut a HollandSheep and get some wools")
        return self.wool


class Pig(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def kill(self):
        self.status = "die"
        return print(f"The pig {self.status}, You get {self.meat} meat")


class Cow(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.milk = 100

    def get_milk(self):
        self.milk -= 10
        if not self.milk < 0:
            print(f"You get {10} liters")
        else:
            print("Cow is tired")

    def kill(self):
        self.status = "die"
        return print(f"The Cow {self.status}, You get {self.meat} meat")


class Birds(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 0


class Chicken(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 3

    def get_eggs(self):
        print(f"You get {self.eggs} eggs")


class Duck(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 2


class Goose(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 1


class Goat(Mammals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.milk = 6

    def kill(self):
        self.status = "die"
        return print(f"The goat {self.status}, You get {self.meat} meat")

    def get_milk(self):
        self.milk -= 2
        if not self.milk < 0:
            print(f"You get {2} liters")
        else:
            print("The goat is tired")


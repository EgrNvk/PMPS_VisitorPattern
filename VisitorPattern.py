class Sedan:

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def accept(self, visitor):
        visitor.visit_sedan(self)

class SUV:

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def accept(self, visitor):
        visitor.visit_suv(self)

class Sunroof:

    def accept(self, visitor, car):
        visitor.visit_sunroof(self, car)

class LeatherInterior:

    def accept(self, visitor, car):
        visitor.visit_leather(self, car)

class Autopilot:

    def accept(self, visitor, car):
        visitor.visit_autopilot(self, car)

class PriceVisitor:

    def __init__(self):
        self.total = 0

    def visit_sedan(self, car):

        print("Авто:", car.model)
        print("Базова ціна:", car.price)

        self.total += car.price

        for option in car.options:
            option.accept(self, car)

    def visit_suv(self, car):

        print("Авто:", car.model)
        print("Базова ціна:", car.price)

        self.total += car.price

        for option in car.options:
            option.accept(self, car)

    def visit_sunroof(self, option, car):

        if isinstance(car, Sedan):
            price = 1500
        else:
            price = 2500

        print("\tПанорамний дах +", price)
        self.total += price


    def visit_leather(self, option, car):

        if isinstance(car, Sedan):
            price = 2000
        else:
            price = 3000

        print("\tШкіряний салон +", price)
        self.total += price

    def visit_autopilot(self, option, car):

        if isinstance(car, Sedan):
            price = 3000
        else:
            price = 5000

        print("\tАвтопілот +", price)
        self.total += price

car = Sedan("Tesla Model Y", 25000)

car.add_option(Sunroof())
car.add_option(LeatherInterior())
car.add_option(Autopilot())

visitor = PriceVisitor()
car.accept(visitor)

print("Загальна ціна:", visitor.total, "\n")


car = SUV("Range Rover", 55000)

car.add_option(Sunroof())
car.add_option(LeatherInterior())

visitor = PriceVisitor()
car.accept(visitor)

print("Загальна ціна:", visitor.total)
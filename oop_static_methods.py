# staticmethods - to organized functions in a class

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def print_stuff():
        print("I am running")


print(Math.add5(3))
print(Math.add10(5))
Math.print_stuff()

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say.")


class Cat(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # to add a new parameter for the init
    # we need to redefine the initializtion method(same as parent class)
    # and call the initialization method of the parent class to get the attributes(variables) using 'super()'
    def __init__(self, name, age, color):
        super().__init__(name, age)  # 'self' not included
        self.color = color

    def speak(self):
        print("meow!")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print("bark!")


pet = Pet("tim", 19)
pet.show()
pet.speak()
cat = Cat("Isa", 16, "Brown")
cat.show()
cat.speak()
dog = Dog("Mike", 12)
dog.show()
dog.speak()

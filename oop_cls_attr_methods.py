class Person:
    # class attribute - not specific to an instance
    static_number = 8
    number_of_people = 0

    def __init__(self, name):
        self.name = name

        # increments the class attribute everytime it initialize an object
        # Person.number_of_people += 1
        # or use the class methods
        Person.add_person()

    # class methods - not specific to an instance
    @classmethod
    def get_number_of_people(cls):  # cls - access only the class attributes
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Isa")
print(p1.number_of_people)
p2 = Person("Mike")
print(p2.number_of_people)
# p1.static_number = 4
# print(p1.static_number)
# print(Person.static_number)

# Person.static_number = 12
# print(p1.static_number)
# print(Person.static_number)

print(Person.get_number_of_people())

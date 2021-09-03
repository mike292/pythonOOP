class Person:
    # parameters are required when object is first initialized
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self, name):
        return self.name

    def get_age(self, age):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        average = total/len(self.students)
        return average


s1 = Student("Tim", 19, 95)
s2 = Student("Alyssa", 19, 80)
s3 = Student("Mike", 21, 75)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())

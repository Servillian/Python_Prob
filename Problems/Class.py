class person:
    def speak(self):
        print("hello, I am", self.name)
    # def __repr__(self):
    #     return self.name
    # def __eq__(self, other):
    #     return self.age == other.age
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.age - other.age
class student(person):
    # def __repr__(self):
    #     return self.name + " student"
    def speak(self):
        print("hello, I am", self.name, "school is to hard i want to die")





a = student(7, "jim")
# b = a
b = student(7, "james")
# print(a - b)
print(a)
a.speak()
# a.age = 7
# a.name = "Felix Shellberg"
# b = person()
# b.age = 7
#
# print("equal", b == a)
# print(a.age, a.name)
# person.age = 6
# print(person.age)
# a.speak()
#
# def this(a):
#     a.age = 4
#     return a
#
# print(this(a))

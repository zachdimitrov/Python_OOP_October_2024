class Circle:
    def __init__(self, r):
        self.r = r  # public
        self.__pi = 3.14  # private only in class
        self._diameter = 2 * self.r  # protected

    def check_pi(self):
        return self.__pi


c = Circle(8)
# print(c.__pi)  # not accessible
print(c._diameter)  # accessible, but not advisable
print(c.check_pi())
print(c.__dict__.keys())
print(c._Circle__pi)  # name mangling


class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

    def __full_name(self):  # private method
        return "Full Name"


p = Person(5)
print(p.age)
print(p._Person__full_name())  # method name mangling

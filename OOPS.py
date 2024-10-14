""" class Student:
    college = "Aligarh Institute of Technology"

    # Static methods are used when you need a function that logically belongs to a class but doesn't need access to instance or class variables.
    @staticmethod  # The @staticmethod decorator indicates that hello is a static method. Static methods do not require access to instance (self) or class (cls) variables. Can be called using either Student.hello() or student1.hello().
    def hello():
        print("Hello World")

    def __init__(self, name, marks):
        # Initializes instance variables name and marks
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

    def get_average(self):
        return sum(self.marks.values()) / len(self.marks)


student1_marks = {"english": 80, "urdu": 90, "maths": 92}
student2_marks = {"pst": 80, "islamiyat": 90, "php": 85}

student1 = Student("Muhammad Huzaifa", student1_marks)
# print(student1.name, student1.marks, student1.college)
print(student1.get_average())
student1.hello()

# WE CAN ALSO GET THE COLLEGE NAME DIRECTLY THROUGH THE CLASS
# print(Student.college)
# static method Can be called using either the class name or an instance 
# print(Student.hello()) """

# definition of instance method, @staticmethod, @classmethod and @property
""" Their are 4 types of methods in class constructors: [instance method, @staticmethod: example is on line no 107, @classmethod: example is on line no 189, @property: example is on line no 208]
instance method: Instance methods indeed take self as the first argument and don't require any decorators. However, they are not used to create new instances; that's the role of the __init__ constructor or class methods acting as alternative constructors. Instance methods are used to access or modify the state of an instance.
@staticmethod: Static methods do not receive the implicit self or cls arguments, which means they cannot access or modify the instance or class state. However, they can accept other arguments. They're essentially namespaced functions within a class and are useful for utility functions related to the class.
@classmethod: Class methods receive the class (cls) as the first argument and can access or modify class-level attributes. They're often used for alternative constructors or methods that need to affect the class as a whole rather than individual instances.
@property: The @property decorator allows you to define methods that can be accessed like attributes. This is useful for computed attributes, where you want to compute a value on the fly based on other attributes, and ensure that it always reflects the current state. """


# OOPS concept have four Pillars: [Abstraction, Encapsulation, Inheritance: example and definition is on line no 107, Polymorphism: example and definition is on line no 238]


# Abstraction and Encapsulation
""" # Abstraction: Hiding the complex implementation(unnecessary things for the user) details of a class and exposing (showing) only the essential(necessary) features(things) to the user is called abstraction
# Encapsulation: Bundling data(attributes) and methods(functions) into a single unit(object) that operate on the data within one unit is called encapsulation
class Car:
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.accelerator = True
        return "Car Started"
    
car1 = Car()

print(car1.start()) """


# Practice for Abstraction and Encapsulation
""" class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, debit_amount):
        if debit_amount > self.balance:
            return "can't debit more than your balance"
        else:
            self.balance -= debit_amount
            return f"{debit_amount} bucks debited. Current balance is {self.balance}"
        
    def credit(self, credit_amount):
        self.balance += credit_amount
        return f"{credit_amount} bucks creditted to your account. Current balance is ${self.balance}"
    
    def print_balance(self):
        return f"You've {self.balance} bucks in your account"

user1 = Account(500, "abc123") """


# ====================================================================================


# public and private attribute:
""" # Some attributes should not be accessable outside of it's class scope because it could be sensitive information. In our scenario anyone will be able to access acc_pass outside of the class scope so instead of creating it as a public attribute we should create it as a private attribute. For example instead of self.acc_pass we should fo self.__acc_pass. It'll make it a private attribute.
# In Python, name mangling with double underscores changes the attribute name internally to _ClassName__attributeName. While this provides a level of privacy, it's still accessible if someone knows the mangled name
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        # self.acc_pass = acc_pass
        self.__acc_pass = acc_pass

user1 = Account("abc123", '987654')
print(user1._Account__acc_pass) """


# =========================================================================================


# Inheritance: Allowing a new class to acquire (inherit) the properties (attributes) and behaviors (methods) of an existing class, enabling code reusability and hierarchical relationships, is called inheritance.
# Their are three types of inheritance: [Single inheritance, Multi-level Inheritance, Multiple Inheritance]

# Single inheritance / Single-level Inheritance
""" class Car:
    @staticmethod
    def start():
        return "car started..."
    
    @staticmethod
    def stop():
        return "car stopped..."

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Mercedes")

print(car1.start()) """

# Multi-level Inheritance
""" class Car:
    @staticmethod
    def start():
        return "car started..."
    
    @staticmethod
    def stop():
        return "car stopped..."

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.start()) """

# Multiple Inheritance
""" class A:
    varA = "Welcome to class A"
    
class B:
    varB = "Welcome to class B"
    
class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA) """


# ====================================================================


# Super Method: super() method is used to access methods of the parent class
""" class Car:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        return "car started..."
    
    @staticmethod
    def stop():
        return "car stopped..."

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        
car1 = ToyotaCar("prius", "electric")
print(car1.type) """


# ========================================================================

# @classmethod:
""" class Person:
    name = "anonymous"
    
    # def change_name(self, name):
    #     # self.name = name # by doing this it'll create a new name instance for us and it's value will be "Huzaifa". The problem here is if we try to print p1.name it'll return "huzaifa" ut if we try to print Person.name it'll still return "anonymous". So to resolve it we've two option eithor instaed of self.name = name we could do Person.name = name or we could do self.__class__.name = name these both method will resolve this issue
    #     self.__class__.name = name # if we're wanted to directly access the class method we've other options for it like a decorator @classmethod

    @classmethod # Decorator to define a class method
    def change_name(cls, name):
        cls.name = name # Modifies the class variable 'name' directly

p1 = Person()
p1.change_name("Huzaifa")
print(p1.name)
print(Person.name) """


# =========================================================================


# @propertymethod:
""" class Student:
    def __init__(self, maths, engish, urdu):
        self.maths = maths
        self.engish = engish
        self.urdu = urdu
        # self.percentage = f"{(self.maths + self.engish + self.urdu) / 3}%" # Problem explained in line no 214
        
    # def calcPercentage(self): # trying to resolve percentage issue explained in line no 219
    #     self.percentage = f"{(self.maths + self.engish + self.urdu) / 3}%"
    
    @property # this is a decorator to directly change the value by returning it. It'll resolve our percentage issue and we'll get the correct percentage
    def percentage(self):
        return f"{(self.maths + self.engish + self.urdu) / 3}%"

s1 = Student(98, 80, 85) # Now let's suppose if by mistake the teacher had passes wrong marks for the maths subject. Now they wanna change it using s1.maths = 89
print(s1.percentage)
s1.maths = 89 # the problem is it'll changes the maths marks but will not change the percentage. The percentage will still be calculated with the wrong marks 
# s1.calcPercentage() # this is one of a way to resolve this but their is one more way to resolve this issue which is by @property method
print(s1.percentage) """


# ========================================================================


""" Polymorphism: Polymorphism in Python demonstrated with operator overloading

Example of polymorphism using the + operator:
print(1 + 2)         # Adds integers
print("Muhammad " + "Huzaifa")  # Concatenates strings
print([1, 4, 5] + [8, 9, 7])  # Merges lists

Operator Overloading in Polymorphism: 
When the same operator has different meanings depending on the context, it is called operator overloading in polymorphism. """

""" class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(f"{self.real} + {self.imaginary}i")
    
    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginary)
    
    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return Complex(new_real, new_imaginary)

num1 = Complex(8, 6)
num1.showNumber()

num2 = Complex(4, 3)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num3 - num2
num4.showNumber() """


# ===========================================================================


# practice for OOPS:
""" class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * self.radius**2

    def perimeter(self):
        return 2 * (22 / 7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter()) """

""" class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        return {
            "role": self.role,
            "department": self.department,
            "salary": self.salary,
        }
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "50k")
    
eng1 = Engineer("Muhammad Huzaifa", 19)
print(eng1.showDetails()) """

""" class Order():
    def __init__(self, order, price):
        self.order = order
        self.price = price
        
    def __gt__(self, other):
        return self.price > other.price
        
order1 = Order("Tea", 299)
order2 = Order("Chips", 20)
print(order1 > order2) """
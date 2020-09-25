# Q1.. Explain OOPS principles with code examples to demonstrate them.


class Oops_Principles:

    def __init__ (self):

        self.fullform = "Object Oriented Programmings"
        self.elements = "Class, Object, Attributes, Methods"
        self.concepts = "Inheritence, Polymorphism, Abstraction, Encapsulation"
        self.principles = "Let's get to know morw about OOPS..."

    def method1(self):

        print("Executing method1: This is a METHOD inside the CLASS 'Oops_Principles'\n")
        print("Let's demonstrate some features of OOPS here:")

        I = input("""
                     *** Press 1 to know about Inheritence ***
                     *** Press 2 to know about Encapsulation ***
                     *** Press 3 to know about Abstraction ***
                     *** Press 4 to know about Polymorphism ***
                        **** PRESS any other key to EXIT ****
                     """)
        if I == "1":
            Oops_Principles.Inheritence(self)
        elif I == "2":
            Oops_Principles.Encapsulation(self)
        elif I =="3":
            Oops_Principles.Abstraction(self)
        elif I == "4":
            Oops_Principles.Polymorphism(self)
        else:
            print("Thank you for youe interest, come back later !")

    def Inheritence(self):
        print("""
                 Thank you for your response! You can read about Inheritence below:

                                ****** I N H E R I T E N C E ******

                Inheritance allows us to define a class that inherits all the methods and properties from another class.

                Parent class is the class being inherited from, also called base class.

                Child class is the class that inherits from another class, also called derived class. 
                See the below example:              

                class Person:                                # ....Parent Class or Base class....
                    def __init__(self, fname, lname):
                        self.firstname = fname
                        self.lastname = lname

                    def printname(self):
                        print(self.firstname, self.lastname)

                class Student(Person):                         ### .... Child class or Derived class....
                    def __init__(self, fname, lname):
                        super().__init__(fname, lname)
                        self.graduationyear = 2019) 
                 
                 """)
        Oops_Principles.method1(self)
    def Encapsulation(self):
        print("""
                 Thank you for your response! You can read about Encapsulation below:

                                ****** E N C A P S U L A T I O N ******

                Using OOP in Python, we can restrict access to methods and variables. 
                This prevents data from direct modification which is called ENCAPSULATION. 
                In Python, we denote private attributes using underscore as the prefix 
                i.e single _ or double __ .

                See below example:

                class Computer:
                    def setMaxPrice(self, price):
                        self.__maxprice = price     ## .....here, __maxprice is Encapsulated.....
                
                
                """)
        Oops_Principles.method1(self)

    def Polymorphism(self):
        print("""
                 Thank you for your response! You can read about Encapsulation below:                
                 
                              ****** P O L Y M O R P H I S M ******       

                Polymorphism in python defines methods in the child class that have the same name as the methods 
                in the parent class. In inheritance, the child class inherits the methods from the parent class. 
                Also, it is possible to modify a method in a child class that it has inherited from the parent class.
                 
                 """)
        Oops_Principles.method1(self)

    def Abstraction(self):
        print("""
                 Thank you for your response! You can read about Encapsulation below:                
                 
                              ****** A B S T R A C T I O N ****** 
                 
                 Abstraction in Python is the process of hiding the real implementation 
                 of an application from the user and emphasizing only on usage of it. 
                 For example, consider you have bought a new electronic gadget
                 """)
        Oops_Principles.method1(self)

oops = Oops_Principles()

print("\nFull form of OOPS is", oops.fullform, ".\n")
print(f"OOPS has following Elements: {oops.elements}.\n")
print(f"The following concepts/Principles are used in OOPS: {oops.concepts}.\n")
print(f"{oops.principles}.\n")

oops.method1()
class Student:
    def __init__(self, name, age, degree, payment, language):
        self.name = name
        self.age = age
        self.degree = degree
        self.payment = payment
        self.language = language

    def show_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Degree:", self.degree)
        print("Expected Payment:", self.payment)
        print("Master Language:", self.language)


name = input("Enter your name: ")
age = input("Enter your age: ")
degree = input("What's your degree: ")
payment = input("Enter your expected payment: ")
language = input("Enter your master language: ")

student1 = Student(name, age, degree, payment, language)

student1.show_info()

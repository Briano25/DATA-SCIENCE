# Define the class
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, age, grade):
        self.name = name      # attribute 1
        self.age = age        # attribute 2
        self.grade = grade    # attribute 3

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    # Method to check if student has passed
    def has_passed(self):
        if self.grade >= 50:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")

# Create an object (instance) of the class
student1 = Student("Alice", 17, 85)
student2 = Student("Bob", 18, 45)

# Call methods on the objects
student1.display_info()
student1.has_passed()

print("-----------")

student2.display_info()
student2.has_passed()

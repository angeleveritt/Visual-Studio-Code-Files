# Assignment - Student Database - Angelique Everitt
print()
print("Assignment - Student Database")
print()

class Student:
    """
    A class to represent a student with name, age, and grades.
    """
    students_db = []  # Class variable to store all students

    def __init__(self, name, age, grades=None):
        """Initialize a student with name, age, and grades."""
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    @classmethod
    def create(cls, name, age, grades=None):
        """Class method to create a new Student instance and add it to the database."""
        student = cls(name, age, grades)
        cls.students_db.append(student)
        return student

    def display_info(self):
        """Display student information."""
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        avg = self.calculate_average()
        if avg is not None:
            print(f"Average Grade: {avg:.2f}")
        else:
            print("No grades available")

    def calculate_average(self):
        """Calculate the average of student grades."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade):
        """Add a new grade to the student's grades list."""
        self.grades.append(grade)

    @classmethod
    def add_student(cls):
        """Interactive method to add a new student to the database."""
        name = input("Enter student name: ")

        while True:
            try:
                age = int(input("Enter student age: "))
                break
            except ValueError:
                print("Please enter a valid age (integer).")

        grades = []
        add_grades = input("Do you want to add grades now? (y/n): ").lower()
        if add_grades == 'y':
            while True:
                try:
                    grade = float(input("Enter grade (or -1 to finish): "))
                    if grade == -1:
                        break
                    grades.append(grade)
                except ValueError:
                    print("Please enter a valid grade.")

        student = cls.create(name, age, grades)
        print(f"Student {name} has been added to the database.")
        return student

    @classmethod
    def display_all_students(cls):
        """Display information for all students in the database."""
        if not cls.students_db:
            print("No students in the database.")
            return

        print("\n--- All Students ---")
        for i, student in enumerate(cls.students_db, 1):
            print(f"\nStudent #{i}:")
            student.display_info()
            print("-" * 20)


# Demonstration scenario
if __name__ == "__main__":
    print("Welcome to Student Database Management System")

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            Student.add_student()
        elif choice == '2':
            Student.display_all_students()
        elif choice == '3':
            print(
                "Thank you for using the Student Database Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

print()
print("fin")
print()


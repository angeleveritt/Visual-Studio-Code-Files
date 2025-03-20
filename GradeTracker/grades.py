# Assignment - GradeTracker - Angelique Everitt
print()
print("Assignment GradeTracker")
print()

import csv
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        average = self.get_average()
        grade_str = ", ".join(str(grade) for grade in self.grades)
        return f"{self.name}: {grade_str} (Average: {average:.2f})"


class GradeTracker:
    def __init__(self, filename="student_grades.csv"):
        self.students = {}
        self.filename = filename
        self.load_grades()
    
    def add_student(self, name):
        """Add a new student if they don't already exist."""
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists.")
        
    def add_grade(self, name, grade):
        """Add a grade for a student."""
        if name in self.students:
            self.students[name].add_grade(grade)
            print(f"Added grade {grade} for {name}")
        else:
            print(f"Student {name} not found. Please add the student first.")
    
    def display_students(self):
        """Display all students and their grades."""
        if not self.students:
            print("No students found.")
            return
        
        print("\nStudent Grades:")
        print("-" * 40)
        for name, student in sorted(self.students.items()):
            print(student)
        print("-" * 40)
    
    def save_grades(self):
        """Save all student grades to a CSV file."""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Student Name', 'Grades'])
                
                for name, student in self.students.items():
                    # Convert grades list to comma-separated string
                    grades_str = ",".join(str(grade) for grade in student.grades)
                    writer.writerow([name, grades_str])
                    
            print(f"Grades saved to {self.filename}")
            return True
        except Exception as e:
            print(f"Error saving grades: {e}")
            return False
    
    def load_grades(self):
        """Load student grades from a CSV file."""
        if not os.path.exists(self.filename):
            print(f"No existing grade file found. Will create {self.filename} when saving.")
            return
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                # Skip header row
                next(reader, None)
                
                for row in reader:
                    if len(row) >= 2:
                        name = row[0]
                        
                        # Create student if they don't exist
                        if name not in self.students:
                            self.students[name] = Student(name)
                        
                        # Parse grades
                        if row[1]:  # Check if grades exist
                            grades_str = row[1].split(',')
                            for grade_str in grades_str:
                                try:
                                    grade = float(grade_str)
                                    self.students[name].add_grade(grade)
                                except ValueError:
                                    print(f"Ignoring invalid grade '{grade_str}' for {name}")
            
            print(f"Loaded grades from {self.filename}")
            return True
        except Exception as e:
            print(f"Error loading grades: {e}")
            return False


def get_valid_grade():
    """Get a valid numerical grade from the user."""
    while True:
        grade_input = input("Enter grade (0-100): ")
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tracker = GradeTracker()
    
    while True:
        print("\nStudent Grade Tracker Menu:")
        print("1. Add a new student")
        print("2. Add a grade for a student")
        print("3. Display all students and grades")
        print("4. Save grades to file")
        print("5. Load grades from file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            tracker.add_student(name)
            
        elif choice == "2":
            name = input("Enter student name: ")
            if name in tracker.students:
                grade = get_valid_grade()
                tracker.add_grade(name, grade)
            else:
                print(f"Student {name} not found. Please add the student first.")
                
        elif choice == "3":
            tracker.display_students()
            
        elif choice == "4":
            tracker.save_grades()
            
        elif choice == "5":
            tracker.load_grades()
            tracker.display_students()
            
        elif choice == "6":
            print("Saving before exit...")
            tracker.save_grades()
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

print()
print("fin")
print()

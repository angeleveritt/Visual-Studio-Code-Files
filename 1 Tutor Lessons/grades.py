# 2025 05 29 exercises
print()
print("student grades analysis")
print()
import pprint

student_grades = {}
student_grades = {
    "AEveritt": {"average" : 80, "highest" : 95, "lowest" : 70},
    "JDoe": {"average" : 90, "highest" : 100, "lowest" : 85},
    "JMSmith" : {"average" : 70, "highest" : 85, "lowest" : 60}
}
pprint.pprint(student_grades)
print()
print("##########################")
print()

print("another way of printing this content")
print()
for name, stats in student_grades.items():
    print(f"{name}: average={stats['average']}, highest={stats['highest']}, lowest={stats['lowest']}")

print()
print("#################")

print()
print("asking for input")
print()
while True:
    print()
    name = input("Enter student's name or enter DONE to finish : ")                  # note the samples he gave for input include 4 numbers sometimes.  Not sure what he wanted here.
    if name == "DONE":
        break
    try:
        average = float(input(f"Enter average: "))
        highest = float(input(f"Enter highest grade: "))
        lowest = float(input("Enter lowest grade: "))
        student_grades[name] = {"average": average, "highest": highest, "lowest": lowest}
    except ValueError:
        print("Please enter numbers for average, highest, and lowest.")

    print("\nStudent Grades: ")
    for name, stats in student_grades.items():
        print(f"{name}: average={stats['average']}, highest={stats['highest']}, lowest={stats['lowest']}")

print()
print("################")
print()

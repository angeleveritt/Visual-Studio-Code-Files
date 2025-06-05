# 2025 05 29 exercises
print()
print("student grades analysis")
print()
import pprint


# do this again but input just grades and then create a new dictionary stats that holes average, highest, and lowest
grades = {
    "andy": [85, 90, 78],
    "fred": [88, 92, 79, 95],
    "jane": [70, 75, 80, 65],
    "douglas": [10, 10, 50, 50, 90,90],
    "jacques": [90, 95, 80, 85]
}
print("These are the original student grades:")
pprint.pprint(grades)

print()

stats = {}

print()
for student, grades in grades.items():
    avg_grade = sum(grades) / len(grades)
    highest_grade = max (grades)
    lowest_grade = min(grades)
    
    stats[student] = {
        "average": round(avg_grade, 2), #rounded for readability
        "highest": highest_grade,
        "lowest": lowest_grade
    }
print("These are the stats")  
pprint.pprint(stats)

print()





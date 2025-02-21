def average(students_grades_data):
    grades = students_grades_data.values()
    average = 0
    for grade in grades:
        average += grade
    return average / len(grades)

def highest(students_grades_data):
    grades = students_grades_data.values()
    highest_grade = max(grades)
    student = [key for key, value in students_grades_data.items() if value == highest_grade]
    return highest_grade, student[0]

def lowest(students_grades_data):
    grades = students_grades_data.values()
    lowest_grade = min(grades)
    student = [key for key, value in students_grades_data.items() if value == lowest_grade]
    return lowest_grade, student[0]

def performance(student_data, student_name):
    grade = student_data[student_name]
    if grade >= 90:
        performance = "Excellent"
    elif grade >= 75:
        performance = "Good"
    else:
        performance = "Need Improvement"
    return performance


students_grades = {}
while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done":
        break
    grade = int(input(f"Enter {name}'s grade: "))
    students_grades[name] = grade

highest_grade, highest_student = highest(students_grades)
lowest_grade, lowest_student = lowest(students_grades)

print("\nClass Performance Report")
print("-------------------------")

print(f"Total students_grades: {len(students_grades)}")
print(f"Average Grade: {average(students_grades)}")
print(f"Highest Grade: {highest_grade} ({highest_student})")
print(f"Lowest Grade: {lowest_grade} ({lowest_student})")

print("\nPerformance Breakdown:")
print("-------------------------")
for student in students_grades:
    print(f"{student} - {students_grades[student]} ({performance(students_grades, student)})")
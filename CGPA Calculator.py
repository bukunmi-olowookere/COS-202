print("=" * 40)
print("   PERSONAL POCKET CGPA CALCULATOR")
print("=" * 40)

num_courses = int(input("Enter the number of courses: "))
total_grade_points = 0
total_credit_units = 0
for i in range(1, num_courses + 1):
    print("\nCourse", i)
    credit = int(input("Enter credit unit: "))
    grade = input("Enter grade (A, B, C, D, E, F): ").upper()
    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    elif grade == "F":
        point = 0
    else:
        print("Invalid grade! Grade point set to 0.")
        point = 0
    total_grade_points += point * credit
    total_credit_units += credit
gpa = total_grade_points / total_credit_units
print("\n" + "=" * 40)
print("Semester GPA =", round(gpa, 2))
choice = input("Do you want to calculate your CGPA? (YES/NO): ").upper()
if choice == "YES":
    previous_cgpa = float(input("Enter your previous CGPA: "))
    previous_units = int(input("Enter your previous total credit units: "))
    new_total_points = (previous_cgpa * previous_units) + total_grade_points
    new_total_units = previous_units + total_credit_units
    cgpa = new_total_points / new_total_units
    print("Your New CGPA =", round(cgpa, 2))
    if cgpa >= 4.50:
        print("Class of Degree: First Class")
    elif cgpa >= 3.50:
        print("Class of Degree: Second Class Upper")
    elif cgpa >= 2.40:
        print("Class of Degree: Second Class Lower")
    elif cgpa >= 1.50:
        print("Class of Degree: Third Class")
    elif cgpa >= 1.00:
        print("Class of Degree: Pass")
    else:
        print("Class of Degree: Fail")
else:
    print("Thank you for using the Personal Pocket CGPA Calculator.")

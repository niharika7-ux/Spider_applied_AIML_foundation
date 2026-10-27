# Practising variables and Python data types

student_name = "Niharika"
semester = 5
attendance_percentage = 86.5
submitted_assignment = True

subjects = ["Python", "Mathematics", "DBMS"]
student_profile = {
    "name": student_name,
    "semester": semester,
    "subjects": subjects
}

print("Student:", student_name)
print("Semester:", semester)
print("Attendance:", attendance_percentage)
print("Assignment submitted:", submitted_assignment)

print("\nTypes of the values:")
print(type(student_name))
print(type(semester))
print(type(attendance_percentage))
print(type(submitted_assignment))
print("Profile:", student_profile)

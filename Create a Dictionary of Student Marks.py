student_marks={
    "Ram" : 80,
    "shyam" : 90,
    "Alice" : 85
}
student_name= input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found")

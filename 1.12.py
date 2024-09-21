def student_with_highmarks():
    N = int(input("Enter the number of students:"))

    students={}

    for i in range(N):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        total_mark = int(input("Enter total marks: "))

        students[roll_no] = {
            "name": name,
            "roll_no": roll_no,
            "total_mark": total_mark
        }

    highest_mark_student = max(students.values(),key=lambda x:x["total_mark"])\

    print("\nDetails of the student with the highest total mark:")
    print(f"Name: {highest_mark_student['name']}")
    print(f"Roll No: {highest_mark_student['roll_no']}")
    print(f"Total Mark: {highest_mark_student['total_mark']}")
student_with_highmarks()

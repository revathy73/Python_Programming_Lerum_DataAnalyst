from to_do import TODO


def guide3(classroom: dict[str, float], students: list[str]) -> str:

    highest_grade = -1.0
    highest_student = ""
    for student in students:
        student_grade = classroom.get(student, -1.0)
        if student_grade > highest_grade:
            highest_student = student
            highest_grade = student_grade

    return highest_student

if __name__ == "__main__":

    # classroom = {"Jane" to 10.0,"John" to 9.5,"Petter" to 8.0},
    # students =["Petter", "Jose", "Richard", "Ana"]
    print(guide3(classroom={"Jane": 10.0, "John" : 9.5, "Petter" : 8.0},
    students = ["Petter", "Jose", "Richard", "Ana"]))

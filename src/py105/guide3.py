"""
You are given a map called classroom in which the keys are the names of
students and the values are their final grades.

You are also given a list called students, which represents the names of
students. Find the student from the list students who has the highest grade.

Save your result in a variable called result

Example Solution
Assume that
classroom is
{
    "Jane" to 10.0,
    "John" to 9.5,
    "Petter" to 8.0
}
students is
["Petter", "Jose", "Richard", "Ana"]
Then
result is Petter
Notes
Assume that there is always a single student with the highest grade.
The smallest grade a student can have is 0.0
Set the result to be an empty string in case no student in students is in
classroom

"""
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

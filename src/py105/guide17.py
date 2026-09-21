"""
You are given the variable education, which is a collection of courses.
Each course is represented as a map in which the key is the course name and
the value is the number of enrolled students in the course.

Determine the class with the most enrolled students and save your
result in a variable called result

Example Solution
Assume that
education is
{
    "history" to {
        "enrolled" to 30,
        "days" to 3
    },
    "programming" to {
        "enrolled" to 100,
        "days" to 5
    },
    "physics" to {
        "enrolled" to 80,
        "days" to 2
    },
}
Then
result is programming
Hint
The inner map will always have a key called enrolled where you can find the
number of enrolled students.
"""

from to_do import TODO


def guide17(education: dict[str, dict[str, int]]) -> str:

    most_enrolled_class = ""
    most_enrolled_students = 0
    for course, details in education.items():
        no_of_enrolled_students = details["enrolled"]
        if no_of_enrolled_students > most_enrolled_students:
            most_enrolled_class = course
            most_enrolled_students = no_of_enrolled_students

    return most_enrolled_class

if __name__ == "__main__":
    edu = {
            "history":{"enrolled":30,"days":3},
            "programming":{"enrolled":100,"days":5},
            "physics":{"enrolled":80,"days":2}
            }
    print(guide17(education=edu))
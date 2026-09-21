"""
You are given the variable classroom, which is a collection of students.
Each student is represented as a map in which the key is gpa and the value
is the GPA of that student.

Calculate the average GPA of the classroom and save your result in a
variable called result

Example Solution
Assume that
classroom is
[
    {"gpa" to 10.0},
    {"gpa" to 9.0},
    {"gpa" to 7.5}
]
Then
result is 8.83
Hint
The inner map will always have a key called gpa where you can find the grade
of a given student.
"""

from to_do import TODO


def guide18(classroom: list[dict[str, float]]) -> float:

    # solution 1:
    if len(classroom) == 0:
        return 0.0

    total_gpa = 0.0
    result = 0.0
    for student in classroom:
        #for gpa_value in student.values():
            total_gpa += student["gpa"]

    result = total_gpa / len(classroom)
    return result
    """
    if len(classroom) == 0:
        return 0.0

    total_gpa = 0.0
    result = 0.0
    for student in classroom:
        gpa_value = student["gpa"]
        total_gpa += gpa_value

    result = total_gpa / len(classroom)
    return result

    # solution 2: sum()
    if len(classroom) == 0:
        return 0.0

    for student in classroom:
        for gpa_value in student.values():
            total_gpa = sum(gpa_value)

    result = total_gpa / len(classroom)
    return result
   
    # solution 3: List comprehension , sum()
    if len(classroom) == 0:
        return 0.0
    total_gpa = [student["gpa"] for student in classroom]
    result = sum(total_gpa) / len(total_gpa) # len(classroom)
    return result
    """



if __name__ == "__main__":

    classroom = [{"gpa":10.0},{"gpa":9.0},{"gpa":7.5}]
    print(guide18(classroom = [{"gpa":10.0},{"gpa":9.0},{"gpa":7.5}]))


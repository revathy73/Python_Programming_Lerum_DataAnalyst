"""
You are given the variable grades, which is a map containing the list of all
the grades for various students. Determine the student that has the highest
average grade in the class

Save your result in a variable called result.

Example Solution
Assume that
grades is
{
    "Ana"  to [4.0, 4.5, 5.0],
    "John" to [5.0, 5.0, 3.0],
    "Lise" to [5.0, 5.0, 5.0]
}
Then
result is Lise
Notes
Use conditional statements and loops in your solution.
Assume that no two students will have the same average grade.
Do not use the built-in function sum().
Do not use the built-in function average().
"""

from to_do import TODO


def task8(grades: dict[str, list[float]]) -> str:

    result = ""
    highest_grade = -1.0
    for student_name,grade in grades.items():
        total = 0.0
        for mark in grade:
            total += mark
        average = total / len(grade)
        if average > highest_grade:
            highest_grade = average
            result = student_name

    return result


if __name__ == "__main__":

    # grades = {"Ana":[4.0, 4.5, 5.0],"John":[5.0, 5.0, 3.0],"Lise":[5.0, 5.0, 5.0]}
    print(task8(grades = {"Ana":[4.0, 4.5, 5.0],"John":[5.0, 5.0, 3.0],"Lise":[5.0, 5.0, 5.0]}))

    print(task8(grades = {'Ana': [3.9, 2.5, 2.5], 'John': [4.3, 4.2, 4.7], 'Lise': [4.2, 4.3, 4.4]}))

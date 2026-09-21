"""
You are given the map grades. It contains a list of grades for various
students. Determine the average grade of the class.

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
result is 4.61
Notes
Do not use the built-in function sum().
Do not use the built-in function average().
Use conditional statements and loops in your solution.
"""

from itertools import count

from to_do import TODO


def task9(grades: dict[str, list[float]]) -> float:

    result = 0.0
    total = 0.0
    no_of_mark = 0
    for student_name,grade in grades.items():
        for mark in grade:
            total += mark
            no_of_mark += 1
        result = total / no_of_mark

    return result

if __name__ == "__main__":

    # grades = {"Ana" : [4.0, 4.5, 5.0],"John" : [5.0, 5.0, 3.0],"Lise" :[5.0, 5.0, 5.0]}
    print(task9(grades = {"Ana" : [4.0, 4.5, 5.0],"John" : [5.0, 5.0, 3.0],"Lise" :[5.0, 5.0, 5.0]}))
    #print(task9(grades = {}))

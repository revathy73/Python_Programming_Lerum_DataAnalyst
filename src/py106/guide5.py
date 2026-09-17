"""
You are given a variable called classroom, which represents a collection
of student grades.

Calculate the average grade of the class.

Raise an Assertion exception in case there are no grades in classroom.

Save your result in a variable called result

Example Solution 1::
Assume that
classroom is [4.5, 4.0, 3.5]
Then
result is 4.0
Example Solution 2::
Assume that
classroom is []
Then
An Assertion exception is raised
Notes
Do not use any built-in function like sum(), average(), etc. to calculate
the average grade.
"""
from to_do import TODO


def guide5(classroom: list[float]) -> float:


    result = []
    total = 0.0
    assert (len(classroom) != 0) #  assert (len(classroom) > 0)

    for grade in classroom:
        total += grade
        result = total / len(classroom)

    return result
    # Solution 2:
    """
    assert (len(classroom) > 0)
    return sum(classroom) / len(classroom)
    """

if __name__ == "__main__":

    # classroom = [4.5, 4.0, 3.5]
    print(guide5(classroom=[4.5, 4.0, 3.5]))

    # classroom = [3.5, 4.0, 3.0]
    print(guide5(classroom=[3.5, 4.0, 3.0]))





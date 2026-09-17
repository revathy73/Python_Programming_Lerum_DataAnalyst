"""
You are given a variable called script, which represents a function that returns a non-empty collection of grades; however, the function may also produce an exception.

Call the function to retrieve the grades and determine the highest grade.

In case an exception of type MissingGrades is produced, then set -1.0 as the result.

In case an exception of type LowAttendance is produced, then set -2.0 as the result.

Save your result in a variable called result

Example Solution 1::
Assume that
script() returns [4.0, 5.0, 4.5]
Then
result is 5.0
Example Solution 2::
Assume that
script() produces a MissingGrades exception
Then
result is -1.0
Notes
Assume the collection is never empty.
"""
from typing import Callable

from linero_tech_errors import MissingGradesError, LowAttendanceError
from to_do import TODO


def guide3(script: Callable[[], list[float]]) -> float:
    """
    Use the code `from linero_tech_errors import MissingGradesError, LowAttendanceError`
    to import the necessary errors
    """
    # solution 1:
    """
    try:
        grades = script()
        highest_grade = grades[0]
        for grade in grades:
            if grade > highest_grade:
                highest_grade = grade

        return highest_grade

    except MissingGradesError:
        return -1.0
    except LowAttendanceError:
        return -2.0
    """
    # solution 2:
    try:

        grades = script()
        result = max(grades)
        return result
        """
        grades = script()
        return max(grades)
        return max(script()) --> Inline
        """
    except MissingGradesError:
        return -1.0
    except LowAttendanceError:
        return -2.0

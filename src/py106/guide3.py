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

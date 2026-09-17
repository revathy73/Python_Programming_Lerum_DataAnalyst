"""
You are given a variable called classroom, which represents students and their
properties.

Among the available properties are the student’s current grades. Replace all
the grades that are null with a value of 0.0

Save your result in a variable called result

Example Solution
Assume that
classroom is
{
  "Petter" to {
    "student-id" to 1234,
    "grades" to [4.0, 5.0, null, 4.4, null, 5.0, 5.0]
  },
  "Johan" to {
    "student-id" to 4563,
    "grades" to [3.0, null, 3.3, 5.0, null, null, 5.0]
  },
  "Handra" to {
    "student-id" to 7584,
    "grades" to [null, 3.0, null, 4.4, null, 4.0, 4.3]
  },
}
Then
result is
{
  "Petter" to {
    "student-id" to 1234,
    "grades" to [4.0, 5.0, 0.0, 4.4, 0.0, 5.0, 5.0]
  },
  "Johan" to {
    "student-id" to 4563,
    "grades" to [3.0, 0.0, 3.3, 5.0, 0.0, 0.0, 5.0]
  },
  "Handra" to {
    "student-id" to 7584,
    "grades" to [0.0, 3.0, 0.0, 4.4, 0.0, 4.0, 4.3]
  },
}
Notes
Assume the key grades will always be present in the collection classroom
"""
from typing import Any

from to_do import TODO


def guide9(classroom: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:

    """
    result = {}
    for student_name,details in classroom.items():
         dirty_grades = details["grades"]
         clean_grades = list(map(lambda grade: 0.0 if grade is None else grade, dirty_grades))
         result[student_name] = {"student-id":details["student-id"],"grades":clean_grades}
    return result
    """
    # solution 2: Do not create a new variable
    for student_name, details in classroom.items():
        dirty_grades = details["grades"]
        clean_grades = list(map(lambda grade: 0.0 if grade is None else grade,dirty_grades))
        classroom[student_name]["grades"] = clean_grades

    return classroom




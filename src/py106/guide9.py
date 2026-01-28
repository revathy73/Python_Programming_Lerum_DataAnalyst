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




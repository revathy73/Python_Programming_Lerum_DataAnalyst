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
            #no_of_mark = grade.count(mark)

        result = total / no_of_mark
    # result = total / (len(grades) * len (grade))

    return result

if __name__ == "__main__":

    # grades = {"Ana" : [4.0, 4.5, 5.0],"John" : [5.0, 5.0, 3.0],"Lise" :[5.0, 5.0, 5.0]}
    print(task9(grades = {"Ana" : [4.0, 4.5, 5.0],"John" : [5.0, 5.0, 3.0],"Lise" :[5.0, 5.0, 5.0]}))


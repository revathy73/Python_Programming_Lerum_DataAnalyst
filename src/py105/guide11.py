from to_do import TODO


def guide11(classroom: dict[str, float]) -> float:
    """
    # solution 1: For loop
    if len(classroom) == 0:
        return 0.0

    result = 0.0
    total = 0.0
    for grade in classroom.values():
        total += grade
        result = total / len(classroom)

    return result
    """
    # solution 2: sum() function
    if len(classroom) == 0:
        return 0.0

    total_grade = sum(classroom.values())
    result = total_grade / len(classroom)
    return  result


if __name__ == "__main__":

    # classroom = {"Far":5.0,"Bob":4.5,"Ben":5.0}
    print(guide11(classroom = {"Far":5.0,"Bob":4.5,"Ben":5.0}))

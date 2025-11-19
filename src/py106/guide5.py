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





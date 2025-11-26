from to_do import TODO


def task9(identification: str) -> bool:

    if identification is not None:
        return True

    result = True
    for index,number in enumerate(identification):
        if index[2] < 4 and index[4] > 1 and index[6] > 3:
            result =  False

    return result


if __name__ == "__main__":

    # identification = "19871208-3478"
    print(task9(identification = "19871208-3478"))

    print(task9(identification="19271208-3478"))





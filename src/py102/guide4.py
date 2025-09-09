from to_do import TODO


def guide4(length: float) -> float:

    perimeter_of_square = 4 * length
    return perimeter_of_square

if __name__ == "__main__":

    # length = 4 --> 16
    print(guide4(length = 4))

    # side = 0 --> 0
    print(guide4(length = 0))

    # side = 5.20 --> 20.8
    print(guide4(length = 5.20))


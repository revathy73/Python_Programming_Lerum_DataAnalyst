from to_do import TODO


def guide4(length: float) -> float:

    result = 4 * length
    return result

if __name__ == "__main__":

    # length = 4 --> 16
    print(guide4(length = 4))

    # side = 0 --> 0
    print(guide4(length = 0))

    # side = 5.20 --> 20.8
    print(guide4(length = 5.20))


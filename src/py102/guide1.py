from to_do import TODO


def guide1(length: float, width: float, height: float) -> float:

    result = length * width * height
    return result


if __name__ == "__main__":
    #length = 5.0, width = 2.0, height = 8.0 --> 80.00
    print(guide1(length=5.0, width=2.0, height=8.0))

    # length = 3.2, width = 2.5, height = 4.03 --> 32.24
    print(guide1(length=3.2, width=2.5, height=4.03))

    # length = 0.0, width = 2.0, height = 7.01 --> 0.0
    print(guide1(length=0.0, width=2.0, height=7.01))

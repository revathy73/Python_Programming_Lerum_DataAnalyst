from to_do import TODO


def guide5(a: float, b: float, c: float) -> float:
    # Calculate the perimeter using the formula
     result = a + b + c
    # Output the result
     return result


if __name__ == "__main__":

    # a = 2.0, b = 3.0, c = 6.0 --> 36.0
    print(guide5(a = 2.0, b = 3.0, c = 6.0))

    # a = 7.2, b = 3.1, c = 6.5 --> 16.8
    print(guide5(a=7.2, b=3.1, c=6.5))
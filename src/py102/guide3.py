from to_do import TODO


def guide3(radius: float) -> float:

    # Input the radius of the Sphere
    # Calculate volume of the Sphere
    # Output the Result

    pi = 3.14116
    result = pi * (radius**3) * (4/3)
    return result

if __name__ == "__main__":

    # radius = 4.25 ---> 321.51
    print(guide3(radius = 4.25))

    # radius = 0.0 --- 0.0
    print(guide3(radius = 0.0))

    # radius = 7.0 ---> 1436.55
    print(guide3(radius = 7.0))
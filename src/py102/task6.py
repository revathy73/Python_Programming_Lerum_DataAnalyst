from to_do import TODO


def task6(base1: float, base2: float, height: float) -> float:
    # Input base1 ,base2 and height for trapezoid
    # Calculate the area of trapezoid

    result = (base1 + base2 ) * height * 0.5
    return result

if __name__ == "__main__":

    # base1 = 5.0, base2 = 3.0, height = 8.0
    print(task6(base1 = 5.0,base2 = 3.0, height =8.0))

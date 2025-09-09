from to_do import TODO


def guide2(base: float, height: float) -> float:
    area_of_triangle = base * height * 0.5
    return area_of_triangle

if __name__ == "__main__":

    # base = 5.0 , height = 7.0 --> 35.0
    print(guide2(base=5.0, height=7.0))

    # base = 3.02 , height = 0.0 --> 0.0
    print(guide2(base=3.02, height=0.0))

    # base = 7.08 , height = 2.10 --> 14.868
    print(guide2(base=7.08, height=2.10))



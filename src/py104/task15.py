from to_do import TODO


def task15(sells: list[int]) -> int:

    result = 0
    for sell in sells:
        result += sell

    return result

if __name__ == "__main__":

    # sells = [20, 100, 800, 768, 765, 90, 10]  --> 2553
    print(task15(sells = [20, 100, 800, 768, 765, 90, 10]))

from to_do import TODO


def guide6(items: list[int]) -> list[int]:

    result = []
    for number in items:
        if number % 5 == 0 and number > 10:
            result.append(number)

    return result

    # solution : List comprehension
    # result = [number for number in items if number % 5 == 0 and number > 10]
    # return result

if __name__ == "__main__":

    # items = [5, 10, 15, 20, 25, 30]
    print(guide6(items=[5,11,12, 10, 15, 20, 25,26,28, 30]))

    print(guide6(items = []))

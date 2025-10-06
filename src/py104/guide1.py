from pkgutil import iter_modules

from to_do import TODO


def guide1(items: list[int]) -> int:

    if len(items) <= 5:
        return  -1

    first_element = items[0]
    third_element = items[2]
    fifth_element = items[4]
    last_element = items[-1]

    result = first_element * third_element * fifth_element * last_element
    return result

if __name__ == "__main__":

    # items = [1,2,3,4,5]
    print((guide1(items=[1,2,3,4,5])))

    # items = [1,2,3,4,5,6]
    print((guide1(items=[1,2,3,4,5,6])))

    # items = [1,2,3]
    print((guide1(items=[1,2,3])))





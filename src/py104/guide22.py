from to_do import TODO


def guide22(a: int) -> set[int]:
    result = set()
    number = a

    while len(result) < 10:
        if number % a == 0:
            result.add(number)
        number += 1

    return result
if __name__ == "__main__":

    # a = 5 ---> {5,10,15,20,25,30,35,40,45,50}
    print(guide22( a = 5))

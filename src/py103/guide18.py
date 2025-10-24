from to_do import TODO


def guide18(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 1
    counter = a
    while counter <= b:
          if counter % 5 == 0:
              result *= counter

          counter += 1

    return result

if __name__ == "__main__":

    # a = 1, b= 20 ---> 15000
    print(guide18(a=1, b= 20))

     # a = 10, b= 2 ---> -1
    print(guide18(a=10, b=2))

    # a = 1, b= 3 ---> 1
    print(guide18(a=1, b=3))



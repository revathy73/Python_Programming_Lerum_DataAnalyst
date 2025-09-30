from to_do import TODO


def task4() -> int:

    result = 0
    for integer in range(1, 1000+1):
        if integer % 9 == 0:
           result += integer

    return result

if __name__  == "__main__":

    print(task4())




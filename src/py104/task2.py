from to_do import TODO

def task2(items: list[int]) -> int:

    if not items:
        return  -1

    result = 0
    for index,item in enumerate(items):
        if index % 2 == 0:
            result = result + item

    return result

if __name__ == "__main__":

    # items = [1,2,3,4]
    print(task2(items = [1,2,3,4]))

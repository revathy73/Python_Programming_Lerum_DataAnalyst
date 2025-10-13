from to_do import TODO


def task5(items: list[int]) -> list[int]:

    result = []
    for index,item in enumerate(items):
        value = item * index
        result.append(value)
        #result.append(item * index)

    return result

if __name__ == "__main__":

    # items = [1, 5, 11]
    print(task5(items = [1, 5, 11]))
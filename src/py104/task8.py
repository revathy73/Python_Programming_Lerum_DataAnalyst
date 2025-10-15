from to_do import TODO


def task8(items: list[int]) -> list[int]:

    result = []
    highest_value = items[0]
    while len(result) < 3:
        for index,item in enumerate(items):
            if item > highest_value:
                value = item
                if index[0] 
                result.append(highest_value)
                items.remove(item)
            item += 1

    return result


if __name__ == "__main__":

    # items = [60, 9, 70, 10] ---> [10, 60, 70]
    print(task8(items = [60, 9, 70, 10]))

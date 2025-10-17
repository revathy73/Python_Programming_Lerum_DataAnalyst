from to_do import TODO


def task8(items: list[int]) -> list[int]:

    unique_values = list(set(items))
    sorted_list = sorted(unique_values)

    if len(sorted_list) >= 3:
        last_index = len(sorted_list) - 1

        third_item = sorted_list[last_index]
        second_item = sorted_list[last_index - 1]
        first_item = sorted_list[last_index - 2]
        result = [first_item, second_item, third_item]
    else:
        result = sorted_list

    return result

    """
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
    """


if __name__ == "__main__":

    # items = [60, 9, 70, 10] ---> [10, 60, 70]
    print(task8(items = [60, 9, 70, 10]))

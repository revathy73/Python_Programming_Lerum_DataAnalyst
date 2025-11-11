from pygments.unistring import combine

from to_do import TODO


def task12(a: list[int], b: list[str]) -> dict[int, str]:

    result = {}
    for index,number in enumerate(a):
        #for index2, letter in enumerate(b):
            #a[index1] = b[index2]
            result[number] = b[index]

    return result

    """
    result = {}
    for number in range(a , b):
        result[a[number]]  = b[number]

    return result
    
    cost = supermarket.get(item, 0.0)
        result += cost
    """

if __name__ == "__main__":

    # a = [1, 2, 3, 4] ,b = ["W", "X", "Y", "Z"]
    print(task12(a = [1, 2, 3, 4] ,b = ["W", "X", "Y", "Z"]))

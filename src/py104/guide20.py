from to_do import TODO


def guide20(a: set[int], b: set[int]) -> set[int]:
    """
    # solution 1: for loop using list and type acsting
    result = []
    for number in a:
        if number in b:
            result.append(number)

    return set(result)

    # solution 2: for loop in set
    result = set()

    for number in a:
        if number in b:
            result.add(number)

    return result

    # solution 3: set comprehension
    result = set((number for number in a if number in b))
    return result
    """
    # solution 3: set comprehension (Refactoring)
    return set((number for number in a if number in b))


    # solution 3: type casting from  List
    #result = [number for number in a if number in b]
    #return set(result)

if __name__ == "__main__":

    # a= {1,2,3,4,5,6} ,b = {4,5,6}
    print(guide20(a= {1,2,3,4,5,6} ,b = {4,5,6}))

    # a= {2,3,6} ,b = {4,5,6}
    print(guide20(a = {2,3,6}, b = {4, 5, 6}))

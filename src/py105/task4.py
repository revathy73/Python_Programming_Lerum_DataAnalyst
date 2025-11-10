from to_do import TODO


def task4(mapa: dict[int, int], parameter: int) -> list[int]:

     result = mapa.get(item, 0.0)
     return result

 """
 result = []
    for number in parameter:
        id = mapa.get(item, 0.0 )
        result.append(id)
    return result


 result = 0.0
    for item in ingredients:
        cost = supermarket.get(item, 0.0)
        result += cost

    return result
"""

if __name__ == "__main__":
    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task4(mapa = {1:100, 2:100, 3:200} ,parameter = 100))


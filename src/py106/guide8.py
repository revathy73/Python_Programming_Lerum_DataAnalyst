def guide8(a: int, b: int) -> dict[int, dict[str, list[int]]]:
    result = {}
    for number in range(a, b):
        result[number] = {
            "Multiplication": [number + number for number in range(1, 10)],
            "Summation": [number * number for number in range(1, 10)],
        }

    return result


if __name__ == "__main__":
    print(guide8(a=1, b=3))
    print(guide8(a=10, b=3))

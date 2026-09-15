"""
Create a function called converter that satisfies the following requirements:

1.One argument of type Int.
2.The return type is an Int.
3.Returns the result of converting hours to milliseconds.
Example Solution:
a)Assume the input is
1
b)The function returns
3600000
Notes:
Do not use any built-in function associated with time conversion.
"""
def converter(number : int) -> int:

    result = number * 3600000
    return result


if __name__ == "__main__":

    print(converter(number = 60))



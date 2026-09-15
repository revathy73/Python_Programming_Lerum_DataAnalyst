"""
Create a function called fizz that satisfies the following requirements:

1.One argument of type Int.
2.The return type is a String.
3.The function must:
a)Return Fizz if the input number is a multiple of 3;
b)Return Buzz if the input number is a multiple of 5;
c)Return FizzBuzz if the input number is a multiple of both 3 and 5;
d)For all other numbers that are not multiples of 3 or 5, return Foo.
Example Solution #1:
a)Assume the input is
3
b)The function returns
Fizz
Example Solution #2:
a)Assume the input is
5
b)The function returns
Buzz
Example Solution #3
a)Assume the input is
15
b)The function returns
FizzBuzz
Example Solution #4
a)Assume the input is
2
b)The function returns
Foo
"""
def fizz(number : int) -> str:

    result = ""
    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"
    else:
        result = "Foo"

    return result

if __name__ == "__main__":

    print(fizz(number = 3))
    print(fizz(number = 15))
    print(fizz(number = 20))
    print(fizz(number = 17))

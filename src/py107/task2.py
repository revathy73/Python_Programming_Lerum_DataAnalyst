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

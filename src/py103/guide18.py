"""
You are given the variables a and b. Using a while loop, multiply all
numbers between a and b, inclusive, which are multiples of 5.

Save your result in a variable called result

Notes
In the case that a is greater than or equal to b, set the result to be -1.
In case there are no values between a and b which are multiples of 5, set
the result to be 1
Example Solution
Assume that
a is 1
b is 20
Then
result is 15000
Notes
Use a while loop to solve the problem
"""

from to_do import TODO


def guide18(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 1
    counter = a
    while counter <= b:
          if counter % 5 == 0:
              result *= counter
          counter += 1
    return result

if __name__ == "__main__":

    # a = 1, b= 20 ---> 15000
    print(guide18(a=1, b= 20))

     # a = 10, b= 2 ---> -1
    print(guide18(a=10, b=2))

    # a = 1, b= 3 ---> 1
    print(guide18(a=1, b=3))



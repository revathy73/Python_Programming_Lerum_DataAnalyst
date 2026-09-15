"""
Create a function called counter that satisfies the following requirements:

1. One argument of type String.
2. The return type is a Boolean.
3. Returns true if the sum of the position of every letter is even and false
otherwise.
Example Solution::
Assume the input is
alexa
The function returns
false
Hint
From the alphabet
a) a is at position 1
b) l is at position 12
c) e is at position 5
d) x is at position 24
e) a is at position 1
Therefore,

a) alexa –> 1 + 12 + 5 + 24 + 1 –> 43

b) 43 is an odd number and thus the function returns false

Notes::
a) Your code must not be case sensitive
b) Do not count spaces
c) Assume the input will never contain special characters, numbers, or be an
empty string.
"""
def counter(string) -> bool:

    #result = True
    total = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in string:
        if char.lower() in alphabet:
            position = alphabet.index(char.lower()) + 1
            total += position

    return total % 2 == 0


if __name__ == "__main__":

    print(counter("alexa"))
    print(counter("hello"))
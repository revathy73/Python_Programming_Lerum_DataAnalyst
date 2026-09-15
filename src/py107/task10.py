"""
Create a function called tweet that satisfies the following requirements:

1) One argument of type String.
2) The return type is a String.
3) A tweet can have at most 280 characters. The function accepts a string and
fills any remaining space with @ until the message reaches the 280 character
limit.

Example Solution::
a) Assume the input is
"I feel good today!"
The function returns::
"I feel good today!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

Hint::
a)) The string I feel good today! has 18 characters. So the function filled the
remaining 262 characters with the @ symbol to reach the 280 tweet limit.
"""
def tweet(sentence : str) -> str:

    #result = ""
    size = len(sentence)
    result = sentence + ("@" * (280- size))

    return result


if __name__ == "__main__":

    print(tweet(sentence= "I feel good today!"))

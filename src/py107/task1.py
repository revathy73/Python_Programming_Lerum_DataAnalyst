"""
Create a function called remover that satisfies the following requirements:
1.One argument of type String.
2.The return type is a String.
3.Removes all the vowels from the input string. It then returns the string
with no vowels.
Example Solution #1
1. Assume the input is
"Sweden is nice"
2. The function returns
"Swdn s nc"
Example Solution #2
1. Assume the input is
"HELLO"
2. Your function returns
"HLL"
Notes:
1.Use a, e, i, o, u as your vowels.
2.Consider capitalized vowels.
3.Do not use the replace() function.
"""
def remover(input : str) -> str:

    """
    result = []
    text = list(input)
    vowels = "AEIOU"
    for letter in text:
        if letter.lower() not in vowels.lower():
            result.append(letter)

    return str(result)
    """

    result = ""
    vowels = "AEIOU"
    for letter in input:
        if letter.lower() not in vowels.lower():
            result += letter

    return result


if __name__ == "__main__":

    print(remover(input = "Sweden is nice"))
    print(remover(input = "HELLO"))

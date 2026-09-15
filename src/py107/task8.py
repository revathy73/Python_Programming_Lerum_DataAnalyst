"""
Create a function called vowels that satisfies the following requirements:

1) One argument of type String.
2) The return type is an Int.
3) Imagine that each vowel has a value (see below). The function returns the sum of all the vowels of the argument string.
Vowel	 Value
a or A	   5
e or E	   4
i or I	   3
o or O	   2
u or U	   1

Example Solution #1::
a) Assume the input is
"I love kotlin"
The function returns
14
Example Solution #2::
a) Assume the input is
"N vwls hr"
The function returns
0
"""
def vowels(text : str) -> int :

    vowel_letters = dict({"a" : 5,"e" : 4 ,"i" : 3, "o" : 2, "u" : 1})
    vowel_counter = 0

    for letter in text.lower():
        if letter in vowel_letters.keys():
            vowel_value = vowel_letters[letter]
            vowel_counter += vowel_value

    return vowel_counter


if __name__ == "__main__":

    print(vowels(text= "I love kotlin"))
    print(vowels(text= "N vwls hr"))












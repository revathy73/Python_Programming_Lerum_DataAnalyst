"""
Create a function called equalizer that accepts any two strings and returns
a list with all the characters that are found in both strings.

Notes
The resulting list cannot have repeated items.
Your solution has to be case-sensitive
"""
def equalizer(text1= "",text2= ""):

    result = []
    for letter in text1:
        if letter in  text2 and not letter in result:
            result.append(letter)

    return result

if __name__ == "__main__":

    print(equalizer(text1= "This is sentence",text2="This is sentence2"))

    print(equalizer(text2="vertical",text1="horizontal"))

    text1 = "parallel"
    text2  = "vertical"
    print(equalizer(text2,text1))

    print(equalizer(text1 = text1, text2 = text2))


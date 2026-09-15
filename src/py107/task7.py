"""
Create a function called censorship that satisfies the following requirements:

a) One argument of type String.
b) The return type is a String.
c) The function censors all words that are more than four characters long with *.
Ignore special characters such as: ,, ;, ., :.
Example Solution::
1) Assume the input is
"I live in Sweden"
a) The function returns
"I live in ******"
"""
def censorship(sentence : str) -> str :

    result = []

    for text in sentence.split():
        word = ""
        special_char = ""
        for letter in text:
            if letter.isalnum():
                word += letter
            else:
                special_char += letter
        if len(word) > 4:
            word = "*" * len(word)

        result.append(word + special_char)

    return " ".join(result)

if __name__ == "__main__":

    #print(censorship(sentence="wrds."))  # word.
    print(censorship(sentence="wor.ds"))  # *****.
    print(censorship(sentence = "Avoid saying bad words"))
    print(censorship(sentence="I live in Sweden"))





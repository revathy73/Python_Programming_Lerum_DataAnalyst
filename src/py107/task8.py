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












from to_do import TODO
import  string

def guide5() -> list[str]:

    alphabet = string.ascii_lowercase
    result = []

    for index,letter in enumerate(alphabet):
        if index % 2 == 0:
            result.append(letter.upper())
        else:
            result.append(letter.lower())
        """    
         letter_to_append = letter.upper() if index % 2 == 0 else letter
         result.append(letter_to_append)
        """
    return result

if __name__ == "__main__":


    # ['A','b','C','d'...]
    print(guide5())
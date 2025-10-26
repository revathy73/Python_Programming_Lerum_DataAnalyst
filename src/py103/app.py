import string
from ctypes import HRESULT

if __name__ == "__main__":
    pass

    """
    age = 90
    AGE = 30
    print(f"The age is {age} and the second one is {AGE}")
    
    # Assignment Operator vs Equality Operator
    # Examples of Assignment Operator Usage
    age = 90
    country = "Panama"
    Capital = "Oslo"
    height = 10

    # Examples of Equality Operator Usage
    9 == 9
    80 == 30
    15 == 15
    45 == 90

    if height == 9:
        print("They are equal")
 
    A = 1 > 2
    B = 1 == 1
    print(f"A AND B ---> {A and B}")
    print(f"A OR B  ---> {A or B}")
    print(f"NOT A   ---> {not A}")
    print(f"NOT B   ---> {not B}")

    #ORDER OF PRECEDENCE
    print(f"NOT A AND B OR NOT A ---> {not A and B or not A}")
    
    capital = "oslo"
    continent = "Europe"

    if capital == "stockholm" and continent == "Europe":
        country = "Sweden"
    else:
        country = "N/A"
    print(f"The country is {country}")
    
    
    for iteration in range(1, 10):
        print("Welcome to python")
        print("We are learning control flow")

    for iteration in range(1, 10):
        print(iteration)

    for number in range(1, 10):
        print(number)

    # Looping for a number 
    for number in range(1, 10):
        print(f"The variable number has a value of {number}")
   
    # Looping for a string
    sentence = "Welcome to Python"
    for letter in sentence:
        print(letter)
         

    # combine decision making with Looping
    for number in range(1, 30):
        if number % 2 == 0:
            print(number)

    number = 1000
    for number in range(1, 11):
        print(f"The variable number has a value of {number}")

    print(number)  ----> o/p : 10
 
    number =1000
    for integer in range(1, 11):
        print(f"The variable number has a value of {integer}")

    print(number) ----> o/p: 1000

    # Range of loops vs Iterations
    for age in range(50, 55):
        print(age)
        
    # Example of FOR LOOP

    name = "python"
    for letter in name:
        print(letter)

    for index,letter in enumerate(name):
        print(f"At position {index} ---> {letter}")

    for number in range(1, 11):
        print(number)
      
    # While loop
    counter = 0
    while counter < 10:
        print(f"Hello world ---> {counter}")
        counter += 1

    # Looping over the letter of a string
    counter = 0
    sentence = "Hello World"
    while counter < len(sentence):
        print(f"{sentence[counter]}")
        counter += 1

    # Looping over a range of number
    counter2 = 1
    while counter2 < 11:
        print(counter2)
        counter2 += 1
        
        
    number = 678
    result = number / 10
    print(result)

    number1 = 678
    result1 = number1 // 10
    print(result1)

    number2 = 678
    result2 = number2 % 10
    print(result2)
   
    number = 1000
    for number in range(1, 11):
        print(f"The variable number has a value of {number}")
    #print(number) - ---> o / p: 10

    number = 1000
    for integer in range(1, 11):
        print(f"The variable number has a value of {integer}")
    #print(number) - ---> o / p: 10
    
    counter = 0
    while counter < 10:
        print(f"{counter}")
        counter += 1

    for number in range(1, 11):
        print(f"the number is {number}")

    sentence = "sweden"
    for index,letter in enumerate(sentence):
        print(f"{index}  ---> {letter}")
        
    # Practice:

    A = 1 > 2
    B = 1 == 1
    print(f"A AND B ---> {A and B}")
    print(f"A OR B  ---> {A or B}")
    print(f"NOT A   ---> {not A}")
    print(f"NOT B   ---> {not B}")

    # ORDER OF PRECEDENCE
    print(f"NOT A AND B OR NOT A ---> {not A and B or not A}")

    print(f"A AND B ---> {A and B}")
    print(f"A OR B ---> {A or B}")
    print(f"NOT A  ---> {not A}")
    print(f"Not B  ---> {not B}")

    # order of precedence
    print(f"NOT A AND B OR NOT A ---> {not A and B or not A}")

    # order of precedence
    print(f"NOT A AND B OR C ---> {not A and B or C}")

    if capital == "Oslo" and country == "Norway":
        result = "Europe"

    alphabet = "sweden"
    for letter in alphabet:
        print(letter)

    for index,letter in enumerate(alphabet):
        print(f"{index} --- > {letter}")

    for number in range(1, 11):
        print(number)

    for number in range(1, 11):
        if number % 2 == 0:
            print(number)

    for index,element in enumerate(range(1, 11)):
        print(f"{index} ---> {element}")

    for number in reversed(range(1, 11)):
        print(number)
            
    for number in range(1, 11, 2):
        print(number)

    for number in range(0, 11, 2):
        print(number)
   
    for number in range(10, 0, -1):
        print(number)

    for number in reversed(range(0, 11)):
        print(number)
   
    for number in range(0, 11, 2):
        print(number)

    for number in reversed(range(0, 11, 2)):
        print(number)
    
    for number in range(10, 0, -2):
        print(number)

    for letter in string.ascii_lowercase:
        print(letter)

    for letter in string.ascii_uppercase:
        print(letter)
    # While loop
    counter = 0
    while counter < 10:
        print(f"Hello world ---> {counter}")
        counter += 1

    # Looping over the letter of a string
    counter = 0
    sentence = "Hello World"
    while counter < len(sentence):
        print(f"{sentence[counter]}")
        counter += 1

    # Looping over a range of number
    counter2 = 1
    while counter2 < 11:
        print(counter2)
        counter2 += 1
    
    counter = 0
    while counter < 10:
        print(f"Hello world ---> {counter}")
        counter += 1

    counter1 = 1
    while counter1 < 11:
        print(f"Hello world ---> {counter1}")
        counter1 += 1
    
    counter2 = 0
    sentence = "Sweden"
    while counter2 < len(sentence):
        print(sentence[counter2])
        counter2 += 1
    
    number = 678
    result = number / 10
    print(result)

    number1 = 678
    result1 = number1 // 10
    print(result1)

    number3 = 678
    result3 = number3 % 10
    print(result3)
    
    day = 1
    if day == 1:
        print("MONDAY")
    elif day == 2:
        print(day)
    else:
        print(day)
    """
    # guide : 9

    email = maria@gmail.com
    is_not_empty = len(email) > 0
    contains_at_sign = "@" in email
    has_correct_ending = ".se" in email[-3:]

    if is_not_empty and contains_at_sign and has_correct_ending:
        return True
    else:
        return False



    return is_not_empty and contains_at_sign and has_correct_ending
    return len(email) > 0 and contains_at_sign and has_correct_ending




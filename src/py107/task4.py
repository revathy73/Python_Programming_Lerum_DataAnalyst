"""
On average, a person washes his or her hands for 21 seconds to help prevent
the spread of viruses. Use this information to create a function called
washing that satisfies the following requirements:
1. The function must accept two arguments of type Int.
a) The first argument of the function is the number of times a person washes
their hands per day.
b) The second argument of the function is the number of months he or she
followed this routine.
2. The return type is a Double.
a) The return type represents the total time, in minutes, that the person
spent washing his or her hands.
Example Solution:
Assume that:
a) A person washes his or her hands 8 times per day
b) A person follows this routine for 7 months
Then
c) The person spent 588.0 minutes washing his or her hands.
Notes
1) Assume a month has 30 days
"""
def washing(number_of_times : int, number_of_months : int) -> float:

    #result = 0.0

    result = number_of_times * number_of_months * 30  * (21 / 60)
    return result


if __name__ == "__main__":

    print(washing( number_of_times = 8,number_of_months = 7))


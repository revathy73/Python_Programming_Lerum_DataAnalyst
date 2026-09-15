"""
Create a class called Student that satisfies the following requirements:

1. The class has one attribute called grades of type List of Double:

grades can be read but not modified from outside the class.
2. A method called gpa

No parameters
The method can be executed from outside the class
Returns the student’s grade point average, or GPA, as Double
3. A method called bonus

No parameters
Adds 1 point to each grade
The method can be executed from outside the class
The method does not return any value
4. A method called lowest

No parameters
The method can be executed from outside the class
Returns the lowest grade as a Double
5. A method called highest

No parameters
The method can be executed from outside the class
Returns the highest grade as a Double
"""
import math
from itertools import count


class Student:

    def __init__(self,grades):
        self.grades = grades

    def get_grades(self):
        return self.grades

    def gpa(self):

        if len(self.grades) == 0:
            return 0.0

        total = 0.0
        result = 0.0
        for grade in self.grades:
            total += grade

        result = total / len(self.grades)
        return result

    def bonus(self):

        result = []
        for grade in self.grades:
            new_grade = grade + 1
            result.append(new_grade)
        self.grades = result
        return self.grades

    def lowest(self):
        if len(self.grades) == 0:
            return 0.0

        lowest_grade = math.inf
        for grade in self.grades:
            if grade < lowest_grade:
                lowest_grade = grade

        return lowest_grade

    def highest(self):

        highest_grade = 0.0
        for grade in self.grades:
            if grade > highest_grade:
                highest_grade = grade

        return highest_grade


if __name__ == "__main__":

      john = Student([77.0, 79.0, 88.0, 90.0, 100.0])
      print(john.grades)
      print(john.gpa())
      print(john.lowest())
      print(john.highest())
      print(john.bonus())
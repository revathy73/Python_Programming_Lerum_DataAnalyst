"""Part #1
Create a class called Learner, which contains the following attributes:

firstname
lastname
learnerId, which is an integer
department
major
grades, a map in which the keys represent class names and the values are grades represented as decimals.
The value of each attribute must be provided through a constructor.

Part #2
Extend the Learner class to contain the following methods:

Method #1:
Name: details
Does not have parameters
The method prints the learner’s details in the following format:
--- Learner Details ---
Name: Humberto Linero
ID: 183937
Department: Engineering
Major: Computer Science
Method #2:

Name: gpa
Does not have any parameters
This method returns the grade point average of the learner.
If the learner does not have any grades, return 0.0.
Method #3:

Name: highestCourse
Does not have any parameters
This method returns a key-value pair with the course that has the highest grade. For example, {"Programming": 5.0}
Method #4:

Name: lowestCourse
Does not have any parameters
This method returns a key-value pair with the course that has the lowest grade. For example, {"History": 4.0}
Method #5:

Name: addGrade
Does not have a return type
Has one parameter of type map
This method adds a new grade to the collection of grades.
Notes
Assume that the collection grades will never be empty.
Part #3
Refactor the class Learner to comply with the following requirements:

The attribute grades is set to private.
All learner instances must have an attribute called School, which has a value of LTH.
The caller cannot initialize the attribute grades via the constructor. Instead, grades has an initial value of an empty collection.
Create a method called grades that returns the grades of the learner.
Part #4
Create a new class called Course, which contains the following attributes:

name
grade
elective
department
All attributes need to be injected via the constructor.

Proceed to make the following refactorings in the class Learner:

The attribute grades is renamed to courses, but keep the visibility. The variable courses represents the list of courses the student is registered for.
Update all the methods affected by this change.
Update the method grades to return the list of grades.
Rename the method addGrade to addCourse.
All other behaviors and attributes must remain the same."""

import math

class Course:
    def __init__(self,name,grade,elective,department):

        self.name = name
        self.grade = grade
        self.elective = elective
        self.department = department


class Learner:

    School = "LTH"

    def __init__(self,firstname,lastname,learner_id,department,major):
        self.firstname = firstname
        self.lastname = lastname
        self.learnerId = learner_id
        self.department = department
        self.major = major
        self.courses = []

    def details(self):
        print("--- Learner Details ---")
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"ID: {self.learnerId}")
        print(f"Department: {self.department}")
        print(f"Major: {self.major}")

    def gpa(self) -> float:

        if len(self.courses) == 0:
            return 0.0

        result = 0.0
        for course in self.courses:
            result += course.grade

        return result / len(self.courses)

    def highestCourse(self) -> dict[str,float]:

        highest_course = ""
        highest_grade = 0.0

        for course in self.courses:
            if course.grade > highest_grade:
                highest_grade = course.grade
                highest_course = course.name

        return {highest_course:highest_grade}

    def lowestCourse(self) -> dict[str,float]:

        lowest_course = ""
        lowest_grade = math.inf

        for course in self.courses:
            if course.grade < lowest_grade:
                lowest_grade = course.grade
                lowest_course = course.name

        return {lowest_course:lowest_grade}

    def addCourse(self,course: Course):
        self.courses.append(course)

    def grades(self) -> list[float]:

        result = []
        for course in self.courses:
            result.append(course.grade)
        return result

if __name__ == "__main__":
        # This is a creating instances of Learner
    john = Learner(
            "john",
            "smith",
            1818,
            "Engineering",
            "computer science",
        )
    john.details()

    programming = Course("Programming 1", 5.0, True, "Engineering")
    autocad = Course("Autocad 1", 4.5, False, "Engineering")

    john.addCourse(programming)
    john.addCourse(autocad)

    print(john.grades())
    print(john.gpa())

    print(john.highestCourse())
    print(john.lowestCourse())




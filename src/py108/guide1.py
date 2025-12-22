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




import math

class Course:
    def __init__(self,name,grade,elective,department):
        self.name = name
        self.grade = grade
        self.elective = elective
        self.department = department

class Learner:
    School = "LTH"
    # This is a perfect example of class and it is a template of a class
    def __init__(self,firstname,lastname,learnerId ,department,major):
        self.firstname = firstname
        self.lastname = lastname
        self.learnerId  = learnerId
        self.department = department
        self.major = major
        self.__courses = []

    def details(self):
        print("-------- Learner Details----------")
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"ID: {self.learnerId}")
        print(f"Department: {self.department}")
        print(f"Major: {self.major}")

    def gpa(self) -> float:
        if len(self.__courses) == 0:
            return 0.0

        result = 0.0
        for course in self.__courses:
            result += course.grade

        return result / len(self.__courses)

    def highestCourse(self) -> dict[str, float]:
        if len(self.__courses) == 0:
            return 0.0

        result = {}
        highest_course_grade = 0.0
        highest_course_name = ""
        for course in self.__courses:
            if course.grade > highest_course_grade:
                highest_course_grade = course.grade
                highest_course_name = course.name
                result[highest_course_name] = highest_course_grade

        return result
        """
        max_of_grades = max(self.grades.values())
        return max_of_grades
        """

    def lowestCourse(self) -> dict[str, float]:
        if len(self.__courses) == 0:
            return 0.0

        #result = {}
        lowest_course_name = ""
        lowest_course_grade = math.inf

        for course in self.__courses:
            if course.grade < lowest_course_grade:
                lowest_course_grade = course.grade
                lowest_course_name = course.name
                #result[lowest_course_name] = lowest_course_grade

        return {lowest_course_name : lowest_course_grade} # return result

    def addCourse(self, course: Course):
        self.__courses.append(course)

    def grades(self) -> list[float]:
        result = []
        for course in self.__courses:
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

    programming = Course("Programming 1",5.0,True,"Engineering")
    autocad = Course("Autocad 1",4.5,False,"Engineering")

    john.addCourse(programming)
    john.addCourse(autocad)

    print(john.grades())
    print(john.gpa())

    print(john.highestCourse())
    print(john.lowestCourse())

    """
    john.addGrade({"Python": 4.0})  
    """

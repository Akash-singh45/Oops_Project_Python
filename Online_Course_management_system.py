class OnlineCourse():
    def __init__(self,course,instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_students(self,name):
        self.students.append(name)
        print(f"{name} has enrolled in the {self.course} course.")

    def course_detail(self):
        print(f"course: {self.course}")
        print(f"instructor : {self.instructor}")
        print(f"Enrolled students:{','.join(self.students)}")

    def completed_course(self,name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed the course .")
        else:
            print("f{name} has not enrolled in the course ")

    def avg_grade(self,grades):
        total = sum(grades)
        average = total/len(grades)
        print(f"the average grade is :{average}")

course_input = input("enter a course: ").lower()
name = input("enter the name of the instructor: ").lower()
student = input("enter the name of the student: ").lower()

course = OnlineCourse(course_input,name)
grades =[98,89,99,97,96]

course.avg_grade(grades)
course.enroll_students(student)
course.course_detail()










class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_to_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):

    def rate_to_std(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Alla', 'Gurina', 'female')
student_1.courses_in_progress += ['Python']

student_2 = Student('John', 'Snow', 'male')
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Aria', 'Stark')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Bob', 'Marley')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Nik', 'Kim')
reviewer_1.courses_attached += ['Python']

student_1.rate_to_lec(lecturer_1, 'Python', 10)
student_1.rate_to_lec(lecturer_1, 'Python', 10)

student_1.rate_to_lec(lecturer_2, 'Python', 10)
student_1.rate_to_lec(lecturer_2, 'Python', 10)


reviewer_1.rate_to_std(student_1, 'Python', 10)
reviewer_1.rate_to_std(student_1, 'Python', 10)
reviewer_1.rate_to_std(student_2, 'Python', 10)

print(student_1.grades)
print(lecturer_2.grades)

from numpy import average


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

    def get_average_grade(self):
        if self.grades:
            return average(list(self.grades.values()))
        else:
            return 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) or 'Нет'
        finished_courses = ', '.join(self.finished_courses) or 'Нет'
        return f'''
        === Student ===
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {avg_grade}
        Курсы в процессе изучения: {courses_in_progress}
        Завершенные курсы: {finished_courses}
        '''

    def __lt__(self, another_student):
        if isinstance(another_student, Student):
            return self.get_average_grade() < another_student.get_average_grade()
        else:
            return 'Ошибка. Сравнивать можно только с другим студентом'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        if self.grades:
            return average(list(self.grades.values()))
        else:
            return 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return f'''
        === Lecturer ===
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {avg_grade}
        '''

    def __lt__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            return self.get_average_grade() < another_lecturer.get_average_grade()
        else:
            return 'Ошибка. Сравнивать можно только с другим лекторами'


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

    def __str__(self):
        return f'''
        === Reviewer ===
        Имя: {self.name}
        Фамилия: {self.surname}
        '''


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
student_1.rate_to_lec(lecturer_1, 'Python', 7)

student_1.rate_to_lec(lecturer_2, 'Python', 5)
student_1.rate_to_lec(lecturer_2, 'Python', 6)


reviewer_1.rate_to_std(student_1, 'Python', 10)
reviewer_1.rate_to_std(student_1, 'Python', 2)
reviewer_1.rate_to_std(student_2, 'Python', 9)


print(reviewer_1)
print(lecturer_2)
print(student_1)



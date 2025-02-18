class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students.append(self)

    def average_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        return \
            f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за домашние задания: {round(self.average_grade(), 1)}\n' \
            f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
            f'Завершенные курсы: {self.finished_courses}\n'


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
        self.lecturers.append(self)

    def average_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return "Ошибка"

    def __str__(self):
        return \
            f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {round(self.average_grade(), 1)}\n' \


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return \
            f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n'


def average_grade_all_lecturers(lecturers, course_name):
    all_lecturers_average_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            all_lecturers_average_grade += lecturer.average_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Ошибка'
    return round(all_lecturers_average_grade / lecturers_count, 2)


def average_grade_all_students(students, course_name):
    all_students_average_grade = 0
    students_count = 0
    for student in students:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            all_students_average_grade += student.average_grade()
            students_count += 1
    if students_count == 0:
        return 'Ошибка'
    return round(all_students_average_grade / students_count, 2)


some_reviewer = Reviewer('Some','Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.courses_attached += ['Введение в программирование']

some_lecturer = Lecturer('Some','Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_lecturer.courses_attached += ['Введение в программирование']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.add_courses('Введение в программирование')

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)

some_student.rate_lecturer(some_lecturer,'Python',10)
some_student.rate_lecturer(some_lecturer,'Python',10)
some_student.rate_lecturer(some_lecturer,'Python',10)
some_student.rate_lecturer(some_lecturer,'Python',9)
some_student.rate_lecturer(some_lecturer,'Git',10)
some_student.rate_lecturer(some_lecturer,'Git',10)
some_student.rate_lecturer(some_lecturer,'Python',10)
some_student.rate_lecturer(some_lecturer,'Git',10)

print(some_reviewer)
print(some_lecturer)
print(some_student)



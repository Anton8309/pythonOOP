from statistics import mean

student_list = []
lecturer_list = []


def get_average(grades):
    average = 0
    len = 0
    for key, value in grades.items():
        average += mean(value)
        len += 1
    if len == 0:
        average = 0
    else:
        average = average / len
    return average


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}

    def get_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        return f'print(some_student)' \
               f'\nИмя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашние задания: {self.grades}' \
               f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'print(some_lecturer)' \
               f'\nИмя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.grades}'

    def __ge__(self, other):
        print('Больше или равно >=')
        return self.grades >= other.grades

    def __le__(self, other):
        print('<= меньше или равно.')
        return self.grades <= other.grades

    def __eq__(self, other):
        print('Равно == ')
        return self.grades == other.grades

    def __lt__(self, other):
        print('< Меньше')
        return self.grades < other.grades

    def __gt__(self, other):
        print('Больше > ')
        return self.grades < other.grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'print(some_reviewer)' \
               f'\nИмя: {self.name}' \
               f'\nФамилия: {self.surname}'


def average_for_course(students, course):
    av_for_course = 0
    len = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            av_for_course += mean(student.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course


def average_for_lecturer(lecturers, course):
    av_for_course = 0
    len = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            av_for_course += mean(lecturer.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course


class Info:
    def get_info(self):
        print(f"Средняя оценка студентов за курс Python: {average_for_course(student_list, 'Python'):.2f}")
        print(f"Средняя оценка лекторов за курс Html: {average_for_lecturer(lecturer_list, 'Html'):.2f}")


some_reviewer = Reviewer('Sam', 'Buddy')
print(some_reviewer)

cool_reviewer = Reviewer('Bob', 'Marley')
print(cool_reviewer)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = 9.9
print(some_lecturer)

cool_lecturer = Lecturer('Fenton', 'Сrack')
cool_lecturer.grades = 8.5
print(cool_lecturer)

some_student = Student('Ruoy', 'Eman')
some_student.grades = 9.9
some_student.courses_in_progress = 'Python,Git'
some_student.finished_courses = 'Введение в программирование'
print(some_student)

best_student = Student('Mary', 'Сracker')
best_student.grades = 7.5
best_student.courses_in_progress = 'Python,Git'
best_student.finished_courses = 'Введение в программирование'
print(best_student)

print(some_lecturer == some_student)
print(some_lecturer < some_student)
print(some_lecturer > some_student)
print(some_lecturer <= some_student)
print(some_lecturer >= some_student)
print('-' * 25)

student1 = Student('Ivan', 'Ivanov')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.courses_in_progress += ['React']

student2 = Student('Petr', 'Petrov')
student2.courses_in_progress += ['CSS']
student2.courses_in_progress += ['Html']

lecturer1 = Lecturer('Semen', 'Semenov')
lecturer1.courses_attached += ['CSS']
lecturer1.courses_attached += ['Html']

lecturer2 = Lecturer('Fedr', 'Petcovich')
lecturer2.courses_attached += ['Git']
lecturer2.courses_attached += ['Html']

reviewer = Reviewer('Andrew', 'Comedian')
reviewer.courses_attached += ['React']
reviewer.courses_attached += ['Python']

reviewer2 = Reviewer('Ignat', 'Ignatov')
reviewer2.courses_attached += ['Git']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)

student2.rate_lecturer(lecturer2, 'Git', 8)
student2.rate_lecturer(lecturer2, 'Git', 6)
student2.rate_lecturer(lecturer1, 'Git', 7)

student2.rate_lecturer(lecturer1, 'Html', 9)
student2.rate_lecturer(lecturer1, 'Html', 9)
student2.rate_lecturer(lecturer2, 'Html', 7)

reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student1, 'React', 7)
reviewer2.rate_hw(student1, 'React', 7)
reviewer2.rate_hw(student1, 'React', 6)

reviewer.rate_hw(student2, 'CSS', 9)
reviewer2.rate_hw(student2, 'CSS', 8)

student_list += [student1]
student_list += [student2]
lecturer_list += [lecturer1]
lecturer_list += [lecturer2]

info = Info()
info.get_info()


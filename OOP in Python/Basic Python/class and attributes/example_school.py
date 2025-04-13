# practice class

class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id= id
    
    def __repr__(self):
        return f'student name: {self.name}, class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject= subject
        self.id = id

    def __repr__(self):
        return f'Course Teacher: {self.name}, course: {self.subject}, id: {self.id}'

class School:
    def __init__(self, name):
        self.name = name
        self.teachers =[]
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def new_enroll(self, name, fee):
        if fee < 20500:
            return f'not enough fee'
        else:
            id = len(self.students) + 1001
            student = Student(name, 'CSE', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'


    def __repr__(self):
        print('welcome to', self.name)

        print('----Our Teacher------')
        for teacher in self.teachers:
            print(teacher)

        print('----Our Students ------')
        for student in self.students:
            print(student)
        return 'all done now'

# alia = Student('alia', 9, 1)
# BossTeacher = Teacher('Boss', 'All course', 199991)
# print(alia)
# print(BossTeacher)

fakeSchool = School('fake school')
fakeSchool.new_enroll('faltu', 22000)
fakeSchool.new_enroll('baltu', 23322)

fakeSchool.add_teacher('nai sir', 'oop')
fakeSchool.add_teacher('hai sir', 'DSA')

print(fakeSchool)
class Student:
    def __init__(self):
        self.reg_no = 'not set'
        self.name = 'not set'

    def set_reg_no(self, reg_no):
        self.reg_no = reg_no

    def set_name(self, name):
        self.name = name

    def get_reg_no(self):
        return f'Student Registration Number: {self.reg_no}'

    def get_name(self):
        return f'Student Name: {self.name}'


class Exam:
    def __init__(self):
        self.exam_no = 'not set'
        self.pattern = 'not set'
        self.semester = 'not set'

    def set_data(self, exam_no, pattern, semester):
        self.exam_no = exam_no
        self.pattern = pattern
        self.semester = semester

    def get_data(self):
        return (f'Exam No: {self.exam_no}\t' +
                f'Exam Pattern: {self.pattern}\t' +
                f'Semester: {self.semester}')


class Result(Student, Exam):
    def __init__(self):
        super().__init__()
        self.phy_marks = 0
        self.chem_marks = 0
        self.math_marks = 0

    def set_marks(self, phy, chem, math):
        self.phy_marks = phy
        self.chem_marks = chem
        self.math_marks = math

    def get_marks(self):
        return (f'Physics: {self.phy_marks}\t' +
                f'Chemistry: {self.chem_marks}\t' +
                f'Math: {self.math_marks}')

    def grade(self):
        res = self.phy_marks + self.chem_marks + self.math_marks
        res = (res / 300) * 100

        if res >= 90:
            return 'A'
        elif res >= 80:
            return 'B'
        elif res >= 70:
            return 'C'
        elif res >= 60:
            return 'D'
        elif res >= 50:
            return 'E'
        else:
            return 'F'


break_line = "=" * 20

result = Result()
print('For Exam,')
result.set_data(input('Exam No: '), input('Pattern: '), input('Semester: '))
print(break_line)

print('For Student,')
result.set_reg_no(input('Reg No: '))
result.set_name(input('Name: '))
print(break_line)

while 1:
    try:
        print('For Marks,')
        result.set_marks(int(input('Physics: ')), int(input('Chemistry: ')), int(input('Mathematics: ')))
        print(break_line)
        break
    except ValueError:
        print("ERROR: Value provided must be of type 'int'! Try again...")

print('RESULT DATA')
print(break_line)

print(result.get_data())
print(f'{result.get_reg_no()}\t{result.get_name()}')

print('Marks')
print(result.get_marks())
print(f'Grade: {result.grade()}')
print(break_line)

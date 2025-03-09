import types


class Student:
    pass


def set_data(self, reg_no, name):
    setattr(self, "reg_no", reg_no)
    setattr(self, "name", name)


def get_data(self):
    if not (hasattr(self, "reg_no") or hasattr(self, "name")):
        return 'No data!'

    return f"Reg No: {self.reg_no}\nName: {self.name}"


print('Student Data')
while 1:
    try:
        reg_no = int(input('Reg No: '))
        break
    except ValueError:
        print("ERROR: Values provided must be of type 'int'! Try again...")

name = input('Name: ')

student = Student()
student.setData = types.MethodType(set_data, student)
student.getData = types.MethodType(get_data, student)

student.setData(reg_no, name)
print('Data Provided,')
print(student.getData())

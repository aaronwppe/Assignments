import types


class Student:
    pass


def set_data(self, reg_no, name):
    setattr(self, "reg_no", reg_no)
    setattr(self, "name", name)


def get_data(self):
    if hasattr(self, "reg_no"):
        return f"Reg No: {self.reg_no}"

    if hasattr(self, "name"):
        return 'type.me'


types.MethodType()

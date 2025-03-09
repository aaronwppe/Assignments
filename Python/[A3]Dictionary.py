import re

student = dict()

TUPLE_FEATURES = ('rno', 'name', 'blood type')

MIN_RNO = 1
MAX_RNO = 100

MIN_NAME = 1
MAX_NAME = 20
PATTERN_NAME = r"^[A-Za-z ]+$"

TUPLE_BLOOD_TYPES = ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+')


def constraint_rno(rno: int):
    if not (MIN_RNO <= rno <= MAX_RNO):
        return f"Roll number '{rno}' out of bounds!"

    if rno in student:
        return f"Roll number '{rno}' already exists!"

    return 0


def constraint_name(name: str):
    if not (MIN_NAME <= len(name) <= MAX_NAME):
        return f"Name '{name}' out of bounds!"

    if not (re.match(PATTERN_NAME, name)):
        return f"Name '{name}' must follow regular expression: {PATTERN_NAME}!"

    return 0


def constraint_blood_type(blood_type: str):
    if blood_type not in TUPLE_BLOOD_TYPES:
        return f"Blood Type can only have values {TUPLE_BLOOD_TYPES}!"


def insert(rno: int, name: str, blood_type: str):
    ret = constraint_rno(rno)
    if ret:
        return ret

    ret = constraint_name(name)
    if ret:
        return ret

    ret = constraint_blood_type(blood_type)
    if ret:
        return ret

    student[rno] = {TUPLE_FEATURES[1]: name, TUPLE_FEATURES[2]: blood_type}
    return f"{student[rno]} inserted!"


def read(rno: int):
    return str(student.get(rno, f"Roll Number {rno} does not exist!"))


def search_features(feature: str, value):
    for i in student.values():
        if i[feature] == value:
            return i

    return f"{feature} '{value}'does not exist!"


def search(feature: str, value):
    if feature not in TUPLE_FEATURES:
        return f"Feature '{feature}' does not exist!"

    if feature == TUPLE_FEATURES[0]:
        return read(int(value))

    return search_features(feature, value)


# anonymous functions with single expressions
def switch(command, *args):
    switcher = {
        "insert": lambda: insert(int(*args[0]), *args),
        "read": lambda: read(int(*args[0])),
        "search": lambda: search(*args)
    }
    func = switcher.get(command, lambda: "Invalid Command")
    return func()


insert(1, "aaron", "A+")

while True:
    input_string = input("student> ")

    if len(input_string) == 0:
        continue

    if input_string == "exit":
        break

    token = input_string.split(sep=' ')

    command = token[0]
    args = token[1:]
    output_string = switch(command, *args)

    print(output_string)
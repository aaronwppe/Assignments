import re
from switch import *

PATTERN_NAME = re.compile(r"^(Mr. |Ms. |Mrs. )?[A-Z][a-z]*( ([A-Z]')?[A-Z][a-z]*)?$")
PATTERN_MOBILE = re.compile(r'^[789]\d{9}$')
PATTERN_PAN = re.compile(r'^[A-Z]{5}\d{4}[A-Z]$')
PATTERN_AADHAAR = re.compile(r'^(\d{4}[- ]?){3}$')

validation_types = {
    'name': {"pattern": PATTERN_NAME,
             "success": "Name is valid.",
             "failure": "Name is not valid!"},

    'mobile': {"pattern": PATTERN_MOBILE,
               "success": "Mobile number is valid.",
               "failure": "Mobile number is not valid!"},

    'pan': {"pattern": PATTERN_PAN,
            "success": "PAN number is valid.",
            "failure": "PAN number is not valid!"},

    'aadhaar': {"pattern": PATTERN_AADHAAR,
                "success": "Aadhaar number is valid.",
                "failure": "Aadhaar number is not valid!"}
}


def validate(check_type, check_string):
    validation = validation_types.get(check_type, None)

    if validation is None:
        exit(1)

    if validation['pattern'].match(check_string):
        return validation['success']
    else:
        return validation['failure']


switch = Switch()
switch.add_case("Validate Name", lambda: print(validate("name", input("Name: "))))
switch.add_case("Validate Mobile", lambda: print(validate("mobile", input("Mobile Number: "))))
switch.add_case("Validate PAN", lambda: print(validate("pan", input("PAN: "))))
switch.add_case("Validate Aadhaar Number", lambda: print(validate("aadhaar", input("Aadhaar Number: "))))
switch.run()
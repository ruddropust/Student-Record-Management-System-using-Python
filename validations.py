import re

def validate_name(name: str) -> bool:
    if not name:
        print("Error: Name cannot be empty!")
        return False
    if any(char.isdigit() for char in name):
        print("Error: Name cannot contain numbers!")
        return False
    if not all(char.isalpha() or char.isspace() for char in name):
        print("Error: Name can contain only letters and spaces!")
        return False
    return True

def validate_roll(sroll: str, students: list) -> bool:
    if not sroll:
        print("Error: Student Roll cannot be empty!")
        return False
    if not sroll.isdigit():
        print("Error: Student Roll must be numeric!")
        return False
    if len(sroll) != 6:
        print("Error: Student Roll must be 6 digits!")
        return False
    roll_int = int(sroll)
    if roll_int <= 0:
        print("Error: Student Roll must be positive!")
        return False
    if any(s.student_roll == roll_int for s in students):
        print("Error: Student Roll already exists!")
        return False
    return True

def validate_dept(dept: str) -> bool:
    if not dept:
        print("Error: Dept. cannot be empty!")
        return False
    if any(char.isdigit() for char in dept):
        print("Error: Dept cannot contain numbers!")
        return False
    if not all(char.isalpha() or char.isspace() for char in dept):
        print("Error: Dept can contain only letters and spaces!")
        return False
    return True

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        print("Error: Email cannot be empty!")
        return False
    if not re.match(pattern, email):
        print("Error: Invalid email format! (Example: name@domain.com)")
        return False
    return True

def validate_cgpa(cgpa: str) -> bool:
    if not cgpa:
        print("Error: CGPA is needed!")
        return False
    try:
        cgpa_float = float(cgpa)
        if 0.0 <= cgpa_float <= 4.0:
            return True
        print("Error: CGPA must be between 0.0 and 4.0!")
        return False
    except ValueError:
        print("Error: CGPA must be a number!")
        return False

def validate_phone(phone: str) -> bool:
    if not phone:
        print("Error: Phone cannot be empty!")
        return False
    if not phone.isdigit():
        print("Error: Phone must be numeric!")
        return False
    if len(phone) != 11:
        print("Error: Phone must be 11 digits!")
        return False
    if not phone.startswith("01"):
        print("Error: Phone must start with 01!")
        return False
    return True

def validate_semester(semester: str) -> str | None:
    if not semester:
        print("Error: Semester cannot be empty!")
        return None
    if not semester.isdigit():
        print("Error: Semester must be numeric!")
        return None
    sem_int = int(semester)
    if not (1 <= sem_int <= 8):
        print("Error: Semester must be between 1 and 8!")
        return None
    suffix = {1: "st", 2: "nd", 3: "rd"}
    return f"{sem_int}{suffix.get(sem_int, 'th')}"

class Student:
    def __init__(self, name, student_roll, cgpa, email, dept, semester, phone):
        self.name = name
        self.student_roll = student_roll
        self.cgpa = cgpa  
        self.email = email
        self.dept = dept
        self.semester = semester
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.student_roll,
            "cgpa": self.cgpa,
            "email": self.email,
            "dept": self.dept,
            "semester": self.semester,
            "phone": self.phone
        }

import os
import json
from models import Student
from validations import validate_cgpa, validate_email, validate_name, validate_phone, validate_roll, validate_semester, validate_dept

class StudentManager:
    def __init__(self, filename="students_db.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Student(
                    s['name'],s['roll'],s['cgpa'],s['email'],s['dept'],s['semester'],s['phone']
                ) for s in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([s.to_dict() for s in self.students], file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_student(self):

        print("\n--- Add New Student ---")
        # Name
        while True:
            name = input("Enter Name: ").strip()
            if validate_name(name):
                break
            else:
                continue

        # Roll
        while True:
            sroll = input("Enter Student Roll: ").strip()
            if validate_roll(sroll, self.students):
                sroll = int(sroll)
                break
            else:
                continue

        # Dept
        while True:
            dept = input("Enter Dept: ").strip()
            if validate_dept(dept):
                break
            else:
                continue

        # Email
        while True:
            email = input("Enter Email: ").strip().lower()
            if email and validate_email(email):
                if any(s.email.lower() == email for s in self.students):
                    print("Error: Email already exists!")
                else:
                    break
            else: 
                continue
            

        # CGPA
        while True:
            cgpa = input("Enter CGPA: ").strip()
            if validate_cgpa(cgpa):
                cgpa = float(cgpa)
                break
            else:
                continue

        # Phone
        while True:
            phone = input("Enter Phone: ").strip()
            if validate_phone(phone):
                break
            else:
                continue
        

        # Semester
        while True:
            semester = input("Enter Semester (1-8): ").strip()
            if validate_semester(semester) is not None:
                semester = validate_semester(semester)
                break
            else:
                continue
        try:
            # Add student
            new_student = Student(name, sroll, cgpa, email, dept, semester, phone)
            self.students.append(new_student)
            self.save_data()
            print("Student added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")

    def view_all(self):
        width = 162
        print(f"\n{'--- Student Records ---':^{width}}")
        if not self.students:
            print("No records found.")
            return

        print("-" * width)
        print(f"{'':<3}{'Name':<25} {'Roll':<10} {'CGPA':<6} {'Email':<40} {'Dept':<40} {'Semester':<10} {'Phone':<15}")
        print("-" * width)

        for s in sorted(self.students, key=lambda x: x.student_roll):
            print(f"{'':<3}{s.name:<25} {s.student_roll:<10} {float(s.cgpa):<6.2f} {s.email:<40} {s.dept:<40} {s.semester:<10} {s.phone:<15}")

        print("-" * width)

    def search_student(self):
        print("\nSearch Student By:")
        print("1. Roll")
        print("2. Name")
        print("3. Email")

        choice = input("Select option (1–3): ").strip()

        if choice == "1":  # Roll
            sroll = input("Enter Roll: ").strip()
            if sroll.isdigit():
                sroll = int(sroll)
                for s in self.students:
                    if s.student_roll == sroll:
                        print(f"Found: {s.name} | {s.dept} | {s.email} | {s.cgpa} | {s.semester} | {s.phone}")
                        return
            print("Student not found.")

        elif choice == "2":  # Name
            name = input("Enter Name: ").strip().lower()
            results = [s for s in self.students if name in s.name.lower()]
            if results:
                for s in results:
                    print(f"Found: {s.name} | {s.student_roll} | {s.dept} | {s.email} | {s.cgpa} | {s.semester} | {s.phone}")
            else:
                print("Student not found.")

        elif choice == "3":  # Email
            email = input("Enter Email: ").strip().lower()
            for s in self.students:
                if s.email.lower() == email:
                    print(f"Found: {s.name} | {s.student_roll} | {s.dept} | {s.cgpa} | {s.semester} | {s.phone}")
                    return
            print("Student not found.")
        else:
            print("Invalid choice.")

    def delete_student(self):
        sroll = input("\nEnter Roll to delete: ").strip()
        if not sroll.isdigit():
            print("Error: Roll must be numeric!")
            return
        sroll = int(sroll)
        for i, s in enumerate(self.students):
            if s.student_roll == sroll:
                confirm = input(f"Are you sure you want to delete {s.name}? (y/n): ").strip().lower()
                if confirm in ["y", "yes"]:
                    self.students.pop(i)
                    self.save_data()
                    print("Student deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return
        print("Student not found.")
    
    def update_student(self):
        sroll = input("\nEnter Roll to update: ").strip()
        if not sroll.isdigit():
            print("Error: Roll must be numeric!")
            return
        sroll = int(sroll)

        # Find student
        for s in self.students:
            if s.student_roll == sroll:
                print(f"Updating student: {s.name} | {s.dept} | {s.email} | {s.cgpa} | {s.semester} | {s.phone}")

                # Name
                while True:
                    new_name = input(f"Enter Name [{s.name}][Press Enter to keep current]: ").strip()
                    if not new_name:
                        new_name = s.name
                    if validate_name(new_name):
                        s.name = new_name
                        break

                # Dept
                while True:
                    new_dept = input(f"Enter Dept [{s.dept}][Press Enter to keep current]: ").strip()
                    if not new_dept:
                        new_dept = s.dept
                    if validate_dept(new_dept):
                        s.dept = new_dept
                        break

                # Email
                while True:
                    new_email = input(f"Enter Email [{s.email}][Press Enter to keep current]: ").strip().lower()
                    if not new_email:
                        new_email = s.email
                    if validate_email(new_email) or new_email == s.email:
                        s.email = new_email
                        break

                # CGPA
                while True:
                    new_cgpa = input(f"Enter CGPA [{s.cgpa}][Press Enter to keep current]: ").strip()
                    if not new_cgpa:
                        break
                    if validate_cgpa(new_cgpa):
                        s.cgpa = float(new_cgpa)
                        break

                # Phone
                while True:
                    new_phone = input(f"Enter Phone [{s.phone}][Press Enter to keep current]: ").strip()
                    if not new_phone:
                        break
                    if validate_phone(new_phone):
                        s.phone = new_phone
                        break

                # Semester
                while True:
                    new_semester = input(f"Enter Semester [({s.semester}), Ex. 1,2,3][Press Enter to keep current]: ").strip()
                    if not new_semester:
                        break
                    sem_val = validate_semester(new_semester)
                    if sem_val:
                        s.semester = sem_val
                        break

                self.save_data()
                print("Student updated successfully.")
                return

        print("Student not found.")

        

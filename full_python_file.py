import json
import os
import re

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
                return [Student(s['name'], s['roll'], s['cgpa'], s['email'], s['dept'],  s['semester'], s['phone']) for s in data]
        except (json.JSONDecodeError, IOError):
            return []
    def validate_email(self, email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if re.match(pattern, email):
                return True
            else:
                print("Error: Invalid email format! (Example: name@domain.com)")
                return False

    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([s.to_dict() for s in self.students], file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_student(self):
        print("\n--- Add New Student ---")
        # Name Validation
        while True:
            name = input("Enter Name: ").strip()

            if not name:
                print("Error: Name cannot be empty!")
                continue

            if any(char.isdigit() for char in name):
                print("Error: Name cannot contain numbers!")
                continue

            if not all(char.isalpha() or char.isspace() for char in name):
                print("Error: Name can contain only letters and spaces!")
                continue

            break

        
        # Roll Validation
        while True:
            sroll = input("Enter Student Roll: ").strip()

            if not sroll:
                print("Error: Student Roll cannot be empty!")
                continue

            if not sroll.isdigit():
                print("Error: Student Roll must be numeric!")
                continue
            if len(str(sroll)) != 6:
                print("Error: Student Roll must be 6 digits!")
                continue

            sroll = int(sroll)

            if sroll <= 0:
                print("Error: Student Roll must be a positive number!")
                continue

            if any(s.student_roll == sroll for s in self.students):
                print("Error: Student Roll already exists!")
                continue

            break

        # Dept Validation
        while True:
            dept = input("Enter Dept: ").strip()

            if not dept:
                print("Error: Dept cannot be empty!")
                continue

            if any(char.isdigit() for char in dept):
                print("Error: Dept cannot contain numbers!")
                continue

            if not all(char.isalpha() or char.isspace() for char in dept):
                print("Error: Dept can contain only letters and spaces!")
                continue

            break

        # Email Validation
        while True:
            email = input("Enter Email: ").strip().lower()
            if email == "":
                print("Error: Email cannot be empty!")
                continue
            if not self.validate_email(email):
                continue
            if any(s.email.lower() == email for s in self.students):
                print("Error: Email already exists!")
            else:
                break
        
        # CGPA Validation
        while True:
            cgpa = input("Enter CGPA: ").strip()

            if not cgpa:
                print("CGPA is needed!")
                continue

            try:
                cgpa = float(cgpa)
            except ValueError:
                print("Error: CGPA must be a float!")
                continue

            if not (0.0 <= cgpa <= 4.0):
                print("Error: CGPA must be between 0.0 and 4.0!")
                continue

            break

        # Phone Validation
        while True:
            phone = input("Enter Phone: ")
            if phone.strip() == "":
                print("Error: Phone cannot be empty!")
                continue
            elif not phone.isdigit():
                print("Error: Phone must be numeric!")
                continue
            elif not len(phone) == 11:
                print("Error: Phone must be 11 digits!")
                continue
            elif not phone.startswith("01"):
                print("Error: Phone must start with 01!")
                continue

            else:
                break
        # Semester Validation
        while True:
            semester = input("Enter Semester (1–8): ").strip()

            if not semester:
                print("Error: Semester cannot be empty!")
                continue

            if not semester.isdigit():
                print("Error: Semester must be numeric!")
                continue

            semester = int(semester)

            if not (1 <= semester <= 8):
                print("Error: Semester must be between 1 and 8!")
                continue

            suffix = {1: "st", 2: "nd", 3: "rd"}
            semester = f"{semester}{suffix.get(semester, 'th')}"
            break


        try:
            # All validations passed, add the student
            new_student = Student(name, sroll, cgpa, email, dept, semester, phone)
            self.students.append(new_student)
            self.save_data()
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. Please try again.")

    def view_all(self):
        print('\n')
        width = 162
        print(f"{'--- Student Records ---' :^{width}}")
        
        if not self.students:
            print("No records found.")
            return
        print("-" * width)
        print(f"{'':<3}{'Name':<25} {'Roll':<10} {'CGPA':<6} {'Email':<40} {'Dept':<40} {'Semester':<10} {'Phone':<15}")
        print("-" * width)
        students_sorted = sorted(self.students, key=lambda s: int(s.student_roll))        
        for s in students_sorted:
            print(f"{'':<3}{s.name:<25} {s.student_roll:<10} {s.cgpa:<6} {s.email:<40} {s.dept:<40} {s.semester:<10} {s.phone:<15}")
        print("-" * width)
        print('\n')

    # Search Student By Roll, Name, Email
    def search_student(self):
        print("\nSearch Student By:")
        print("1. Roll")
        print("2. Name")
        print("3. Email")

        choice = input("Select option (1–3): ").strip()

        #  Search by Roll
        if choice == "1":
            sroll = input("Enter Roll: ").strip()

            if not sroll:
                print("Error: Roll cannot be empty!")
                return

            if not sroll.isdigit():
                print("Error: Roll must be numeric!")
                return

            sroll = int(sroll)

            for s in self.students:
                if s.student_roll == sroll:
                    print(f"Found- Student Name: {s.name} | Dept: {s.dept} | Email: {s.email} | CGPA: {s.cgpa} | Semester: {s.semester} | Phone: {s.phone}")
                    return

            print("Student not found.")

        #  Search by Name
        elif choice == "2":
            name = input("Enter Name: ").strip().lower()

            if not name:
                print("Error: Name cannot be empty!")
                return

            results = [s for s in self.students if name in s.name.lower()]

            if results:
                for s in results:
                    print(f"Found- Student Roll: {s.student_roll} | Dept: {s.dept} | Email: {s.email} | CGPA: {s.cgpa} | Semester: {s.semester} | Phone: {s.phone}")
            else:
                print("Student not found.")

        #  Search by Email
        elif choice == "3":
            email = input("Enter Email: ").strip().lower()

            if not email:
                print("Error: Email cannot be empty!")
                return

            for s in self.students:
                if s.email.lower() == email:
                    print(f"Found- Name: {s.name} | Dept: {s.dept} | Roll: {s.student_roll} | CGPA: {s.cgpa} | Semester: {s.semester} | Phone: {s.phone}")
                    return

            print("Student not found.")

        else:
            print("Invalid choice.")


    def delete_student(self):
            sroll = input("\nEnter Roll to delete: ")
            
            if not sroll.strip():
                print("Error: Roll cannot be empty!")
                return
            try:
                sroll = int(sroll)
                for i, s in enumerate(self.students):
                    if s.student_roll == sroll:
                        # Add the confirmation prompt here
                        confirm = input(f"Are you sure you want to delete {s.student_roll}? (y/n):").strip().lower()

                        if confirm == "y" or confirm == "yes":
                            self.students.pop(i)
                            self.save_data()
                            print("Record deleted successfully.")
                        else:
                            print("Deletion cancelled.")
                        return
                
                print("Student not found.")
            except ValueError:
                print("Error: Roll must be a number!")
                return



def main():
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    manager = StudentManager()
    
    menu_options = {
        '1': manager.add_student,
        '2': manager.view_all,
        '3': manager.search_student,
        '4': manager.delete_student,
        '5': exit
    }

    while True:
        print("\n")
        print("="*14 +" Menu " +"="*14)
        print("1. Add Student\n2. View All Student\n3. Search Student\n4. Delete Student\n5. Exit")
        print("=" * 34)
        choice = input("Select an option: ")
        
        action = menu_options.get(choice)
        if action:
            if choice == '5':
                print("Thank you for using the Student Record Management System. Goodbye!")
                action()
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
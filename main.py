import json
import os
import re

class Student:
    def __init__(self,name, student_roll, email,dept, cgpa=None):
        self.name = name
        self.student_roll = student_roll
        self.email = email
        self.dept = dept
        self.cgpa = cgpa
        

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.student_roll,
            "email": self.email,
            "dept": self.dept,
            "cgpa": self.cgpa
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
                return [Student(s['name'], s['roll'], s['email'], s['dept'], s['cgpa']) for s in data]
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
            name = input("Enter Name: ")
            if name.strip() == "":
                print("Error: Name cannot be empty!")
            elif name.isnumeric():
                print("Error: Name cannot be numeric!")
            else:
                break
        
        # Roll Validation
        while True:
            sroll = input("Enter Student Roll: ")
            if sroll.strip() == "":
                print("Error: Student Roll cannot be empty!")
                continue
            try:
                sroll = int(sroll)
            except ValueError:
                print("Error: Student Roll must be a number!")
                continue
            if any(s.student_roll == sroll for s in self.students):
                print("Error: Student Roll already exists!")
            else:
                break
        # Dept Validation
        while True:
            dept = input("Enter Dept: ")
            if dept.strip() == "":
                print("Error: Dept cannot be empty!")
            elif dept.isnumeric():
                print("Error: Dept cannot be numeric!")
            else:
                break

        # Email Validation
        while True:
            email = input("Enter Email: ")
            if email == "":
                print("Error: Email cannot be empty!")
                continue
            if not self.validate_email(email):
                continue
            if any(s.email == email for s in self.students):
                print("Error: Email already exists!")
            else:
                break
        
        # CGPA Validation
        while True:

            cgpa = input("Enter CGPA: ")
            if cgpa.strip() == "":
                print("CGPA is needed!")
                continue
                
            try:
                cgpa = float(cgpa)
                if not (0.0 <= cgpa <= 4.0):
                    print("Error: CGPA must be between 0.0 and 4.0!")
            except ValueError:
                print("Error: CGPA must be a float!")
                continue
                
            else:
                break

        try:
            # All validations passed, add the student
            new_student = Student(name, sroll, email, dept, cgpa)
            self.students.append(new_student)
            self.save_data()
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. Please try again.")

    def view_all(self):
        print('\n')
        print(f"{'--- Student Records ---' :^154}")
        
        if not self.students:
            print("No records found.")
            return
        print("-" * 154)
        print(f"{": ":<3}{'Name':<35} {'Roll':<10} {'CGPA':<6} {'Email':<50} {'Dept':<45}:")
        print("-" * 154)
        students_sorted = sorted(self.students, key=lambda s: int(s.student_roll))        
        for s in students_sorted:
            print(f"{": ":<3}{s.name:<35} {str(s.student_roll):<10} {s.cgpa:<6.2f} {s.email:<50} {s.dept:<45}:")
        print("-" * 154)
        print('\n')

    def search_student(self):
        sroll = input("\nEnter Roll to search: ")
        if not sroll.strip():
            print("Error: Roll cannot be empty!")
            return
        try:
            sroll = int(sroll)
            for s in self.students:
                if s.student_roll == sroll:
                    print(f"Found: {s.name} | Dept: {s.dept} | Email: {s.email} | CGPA: {s.cgpa}")
                    return
        except ValueError:
            print("Error: Roll must be a number!")
            return
        
        print("Student not found.")

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
from manager import StudentManager

def main():
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    RED = "\033[31m"
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print(f"{RED}Make Full Screen for Better Experience!{RESET}")

    manager = StudentManager()
    menu_options = {
        '1': manager.add_student,
        '2': manager.view_all,
        '3': manager.search_student,
        '4': manager.delete_student,
        '5': manager.update_student,
        '6': exit
    }

    while True:
        print("\n")
        print("="*14 +" Menu " +"="*14)
        print(f"{CYAN}1. Add Student\n2. View All Student\n3. Search Student\n4. Delete Student\n5. Update Student\n6. Exit{RESET}")
        print("=" * 34)
        choice = input("Select an option: ")
        
        action = menu_options.get(choice)
        if action:
            if choice == '6':
                print("Thank you for using the Student Record Management System. Goodbye!")
                action()
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

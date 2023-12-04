import admin_module
import student_module
from database import Database

def main():
    database = Database()
    database.load_data()

    while True:
        print("\nWelcome to the MaswaliYote Quiz Management System:")
        print(".....................................................\n")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit\n")
        print(".....................................................\n")

        choice = input("Please enter your choice (1,2 or 3): ")

        if choice == "1":
            admin_module.admin_menu(database)
        elif choice == "2":
            student_module.student_menu(database)
        elif choice == "3":
            database.save_data()
            print("\n\t You have exited MaswaliYote Quiz Management System. Goodbye!\n")
            break
        else:
            print("\n\t Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
import encryption_module

def admin_menu(database):
    while True:
        print("\nMaswaliYote - Admin Menu:")
        print("............................\n")
        print("1. Login")
        print("2. Create Quiz")
        print("3. View Quiz")
        print("4. Update Quiz")
        print("5. Delete Quiz")
        print("6. Logout")
        print("............................\n")

        choice = input("Please enter your choice (1-6): ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            create_quiz(database)
        elif choice == "3":
            view_quiz(database)
        elif choice == "4":
            update_quiz(database)
        elif choice == "5":
            delete_quiz(database)
        elif choice == "6":
            print("You have logged out from admin account.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

def admin_login():
    # Creating a secure admin login 
    admin_username = input("Please enter admin username: ")
    admin_password = input("Please enter admin password: ")

    # Checking the credentials 
    if admin_username == "admin" and encryption_module.encrypt_password(admin_password) == "hashed_admin_password":
        print("Welcome to MaswaliYote Admin Account!.")
    else:
        print("Invalid credentials. Please try again!")
 
 # Creating a quiz
def create_quiz(database):   
    quiz_name = input("Please enter quiz name: ")   
    new_quiz = {"name": quiz_name, "questions": []}
    database.add_quiz(new_quiz)
    print(f"Quiz '{quiz_name}' created successfully.")
 
 # Creating the view quiz
def view_quiz(database):   
    quizzes = database.get_quizzes()
    print("\nMaswaliYote - Available Quizzes:")
    print("..................................\n")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    quiz_index = int(input("\nPlease enter the quiz number to view details: ")) - 1

    try:
        selected_quiz = quizzes[quiz_index]
        print(f"\nQuiz: {selected_quiz['name']}")       
    except IndexError:
        print("Invalid quiz number. Please try again.")

# Updating the quiz
def update_quiz(database):    
    quizzes = database.get_quizzes()
    print("\nMaswaliYote - Available Quizzes:")
    print("..................................\n")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    quiz_index = int(input("Please enter the quiz number to update: ")) - 1

    try:
        selected_quiz = quizzes[quiz_index]
        print(f"\nUpdating Quiz: {selected_quiz['name']}")
        # Modifying quiz
        database.save_data()
        print("The Quiz has updated successfully.")
    except IndexError:
        print("Invalid quiz number. Please try again.")

# Deleting the quiz
def delete_quiz(database):
    quizzes = database.get_quizzes()
    print("\nMaswaliYote - Available Quizzes:")
    print("..................................\n")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    quiz_index = int(input("Please enter the quiz number to delete: ")) - 1

    try:
        deleted_quiz = quizzes.pop(quiz_index)
        database.save_data()
        print(f"Quiz '{deleted_quiz['name']}' deleted successfully.")
    except IndexError:
        print("Invalid quiz number. Please try again.")

import encryption_module

def student_menu(database):
    while True:
        print("\nMaswaliYote - Student Menu:")
        print(".............................\n")
        print("1. Login")
        print("2. Take Quiz")
        print("3. View Results")
        print("4. Logout")
        print(".............................\n")

        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            student_login()
        elif choice == "2":
            take_quiz(database)
        elif choice == "3":
            view_results(database)
        elif choice == "4":
            print("\n \t You have logged out from student account.")
            break
        else:
            print("\n \t Invalid choice. Please enter a valid option. (1-4)")

# Creating a secure student login 
def student_login():   
    student_username = input("Please enter your student username: ")
    student_password = input("Please enter your student password: ")

    # Checking the login 
    if student_username == "student" and encryption_module.encrypt_password(student_password) == "hashed_student_password":
        print("Welcome to MaswaliYote Student Account!")
    else:
        print("Invalid credentials. Please try again.")

def take_quiz(database):
    quizzes = database.get_quizzes()
    print("\n MaswaliYote - Available Quizzes:")
    print("...................................\n")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    quiz_index = int(input("Please enter the quiz number to take: ")) - 1

    try:
        selected_quiz = quizzes[quiz_index]
        print(f"\nTaking Quiz: {selected_quiz['name']}")
        
        # Storing the results in the student_results 
        database.save_data()
        print("The Quiz has been submitted successfully.")
    except IndexError:
        print("Invalid quiz number. Please try again.")
 
 # Students to view quiz results
def view_results(database):
    student_results = database.get_student_results()
    print("\nMaswaliYote - Your Quiz Results:")
    print("..................................\n")
    for result in student_results:
        print(f"Quiz: {result['quiz_name']}, Score: {result['score']}")

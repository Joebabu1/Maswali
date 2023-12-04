import json

class Database:
    # Data for quizzes and student results
    def __init__(self):        
        self.quizzes = []
        self.student_results = []

# Save quizzes and student results to JSON files
    def save_data(self):        
        with open("quizzes.json", "w") as quizzes_file:
            json.dump(self.quizzes, quizzes_file, indent=2)

        with open("student_results.json", "w") as results_file:
            json.dump(self.student_results, results_file, indent=2)
    
    # Load quizzes and student results from JSON files
    def load_data(self):        
        try:
            with open("quizzes.json", "r") as quizzes_file:
                self.quizzes = json.load(quizzes_file)
        except FileNotFoundError:
            self.quizzes = []

        try:
            with open("student_results.json", "r") as results_file:
                self.student_results = json.load(results_file)
        except FileNotFoundError:
            self.student_results = []

    def get_quizzes(self):
        return self.quizzes

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)
        self.save_data()

    def get_student_results(self):
        return self.student_results

    def add_student_result(self, result):
        self.student_results.append(result)
        self.save_data()

import unittest
from unittest.mock import patch
from quiz_system import main  # Assuming the main function is in quiz_system.py

class TestQuizManagementSystem(unittest.TestCase):

    def setUp(self):
        # Initialize any necessary setup before each test case
        self.database_path = 'test_database.json'  # Use a separate database for testing

    def tearDown(self):
        # Clean up after each test case
        pass

    def test_admin_login_successful(self):
        with patch('builtins.input', side_effect=['1', 'admin', 'admin_password', '7']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Admin login successful.", output)

    def test_admin_login_unsuccessful(self):
        with patch('builtins.input', side_effect=['1', 'invalid_admin', 'invalid_password', '3']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Invalid credentials. Please try again.", output)

    def test_student_login_successful(self):
        with patch('builtins.input', side_effect=['2', 'student', 'student_password', '3']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Student login successful.", output)

    def test_student_login_unsuccessful(self):
        with patch('builtins.input', side_effect=['2', 'invalid_student', 'invalid_password', '3']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Invalid credentials. Please try again.", output)

    def test_create_quiz(self):
        with patch('builtins.input', side_effect=['1', 'admin', 'admin_password', '2', 'MyQuiz', 'done', '7']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Quiz 'MyQuiz' created successfully.", output)

    def test_answer_quiz(self):
        with patch('builtins.input', side_effect=['2', 'student', 'student_password', '4']):
            with patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
                main(database_path=self.database_path)
                output = mock_stdout.getvalue().strip()
                self.assertIn("Available Quizzes:", output)

                # Choose the first quiz (assuming there is at least one quiz in the database)
                with patch('builtins.input', side_effect=['1', '1', '3']):
                    main(database_path=self.database_path)
                    output = mock_stdout.getvalue().strip()
                    self.assertIn("Quiz Title: MyQuiz", output)

                    # Answer the quiz
                    with patch('builtins.input', side_effect=['1', '2', '3', '4', '3']):
                        main(database_path=self.database_path)
                        output = mock_stdout.getvalue().strip()
                        self.assertIn("Quiz submitted successfully.", output)
if __name__ == '__main__':
    unittest.main()

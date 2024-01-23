# **MaswaliYote Quiz Management System (MQMS)**

### Description

This MaswaliYote Quiz System (CLI) is a command-line simple system designed to create, manage, and take quizzes. It provides a straightforward way to define quiz questions, organize them into categories, and take quizzes with instant feedback on your performance. This is done in fulfillment of my Software Development course project.

### 1. Git
Git and GitHub has been used throughout this project. 

[Find Commit history here:](https://github.com/Joebabu1/Maswali/commits)

### 2. Installation Prerequisites

+ Python 3.x

+ Virtual Environment (Optional)

2.1 [Optional] Create and activate a virtual environment:

          python3 -m venv venv
          source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'

2.2 Running the Application

Use the provided run_quiz_system.py script to run the MaswaliYote Quiz Management System:

          python3 run_quiz_system.py

Follow the on-screen instructions to navigate the system.

### 3. UML Diagrams
  
--> [Class Diagram](https://github.com/Joebabu1/Maswali/assets/143649670/334aba21-a5c9-4684-8398-a613a46e2ec1)

--> [Activity Diagram](https://github.com/Joebabu1/Maswali/assets/143649670/905ace15-94f7-4c2d-b424-43104d52f7cb)
 
--> [Component Diagram](https://github.com/Joebabu1/Maswali/assets/143649670/a4f38899-b326-4edb-b968-b5692b23cfce)

### 4. Requirements Engineering

Requirements specification was done with the help of Airtable. [Click here to view](https://airtable.com/appVk1hPphTm997MN/shrhSsRi2hW5Xz6Qx)

### 5. Analysis of the Quiz System

 This analysis report provides a snapshot of MaswaliYote Quiz System's current state and suggests areas for future consideration and enhancement.
[Click here to read ](https://github.com/Joebabu1/Maswali/blob/master/Docs/Analysis%20Report%20-%20MQMS.pdf)

### 6. Domain-Driven Design (DDD)

Developers own creation of event storming and DDD. [Click here](https://github.com/Joebabu1/Maswali/blob/master/Docs/DDD%20-%20MaswaliYote%20Quiz%20Management%20System.pdf) for the .pdf


### 7. Metrics

SonarQube was used to do metrics and testing for this project. It was integrated to jenkins and excuted after project loads from GitHub to Jenkins. Here are some of the [screenshoots from SonarQube Dashboard](https://github.com/Joebabu1/Maswali/blob/master/Docs/SonarQube%20Screenshots%20for%20MaswaliYote%20Quiz%20Management%20System.pdf)


### 8. Clean Code Development

--> [Single Responsibility Principle](https://github.com/Joebabu1/Maswali/blob/fc79e03861d61abd36ee15cc94e7312779058b3e/database.py#L48)
 
--> [Parameters and return types](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/database.py#L44)

--> [Meaniful Variable Name](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/database.py#L51)

--> [Consitent code formatting](https://github.com/Joebabu1/Maswali/blob/fc79e03861d61abd36ee15cc94e7312779058b3e/admin_module.py#L104C1-L105C37)

--> [More on Clean Code......](https://github.com/Joebabu1/Maswali/blob/master/Docs/Clean%20Code%20Development%20Report.pdf)


++++ [Click here for Clean Code Cheatsheet:](https://github.com/Joebabu1/Maswali/blob/master/Docs/Clean%20Code%20Cheatsheet.pdf)

### 9. Build Management and CI/CD

Jenkins was used for Continuous Integration and Continuous Development (CICD). You can view [some screenshots here](https://github.com/Joebabu1/Maswali/blob/master/Docs/Jenkins%20-%20MaswaliYote%20Quiz%20Management%20System.pdf)

### 10. Testing

Unit Tests will be executed automatically with every push to respository with Jenkins actions. Find [test file here:](https://github.com/Joebabu1/Maswali/blob/master/unittest.py)

You can run tests manually with: 

          python3 -m unittest -v src/unittest.py

### 11. Functional Programming

-> [Immutability](https://github.com/Joebabu1/Maswali/blob/f8205ef709650a06341ebd036a54a8ff87eb7b84/quiz_system.py#L37C1-L38C1)

-> [List Comprehensions](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/admin_module.py#L112C1-L112C50)

-> [Higher-order Functions](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/student_module.py#L30)

-> [Using itertools](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/admin_module.py#L76)

-> [Only final data structures](https://github.com/Joebabu1/Maswali/blob/c1b7b00cff33888b47d783fb5b5a4362ad90a22b/database.py#L6)

### 12. Contribution

Please check the 'Contribute.md' file for guidelines on how to contribute to the project.

  ##### Developed by Joebabu1 Consultants

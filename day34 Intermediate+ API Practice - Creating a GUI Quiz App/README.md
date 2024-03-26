# Quiz App

This project implements a quiz application that retrieves questions from an external API, presents them to the user, and evaluates their answers. Below is a summary of the project components:

- `main.py`: Orchestrates the quiz application by importing question data, creating question objects, initializing the quiz brain, and setting up the user interface.
- `data.py`: Contains code to fetch questions from an API using the requests library and parse the JSON response.
- `question_model.py`: Defines the Question class to represent individual quiz questions with text and correct answers.
- `quiz_brain.py`: Implements the QuizBrain class responsible for managing the quiz state, including tracking the current question, user score, and checking answers.
- `ui.py`: Constructs the graphical user interface (GUI) using Tkinter, including components such as labels, buttons, and canvas for displaying questions and feedback.

## Features

- Fetches questions from an external API.
- Presents questions to the user and evaluates their answers.
- Provides feedback on user responses.
- Tracks user score and progress throughout the quiz.

## Dependencies

- Python 3.x
- Tkinter (standard GUI toolkit for Python)
- requests library (for making HTTP requests)

## Acknowledgments

- The Open Trivia Database (opentdb.com) for providing the trivia questions used in this project.

## Contacts

For questions or feedback regarding this project, feel free to contact:

- [Shivam Kumar](shivamkumar819991@gmail.com) - Project Developer

This documentation provides an overview of the project's structure, features, dependencies, acknowledgments, and contact information, facilitating understanding and collaboration for developers interested in the project.

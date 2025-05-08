# Nunyie
# Quiz Giver
# Reads the text file created by the quiz creator and quizzes the user

import random
# Reads the text file created by the quiz creator and quizzes the user
def load_quiz_data(filename='question_bank.txt'):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

        
# Nunyie
# Quiz Giver
# Reads the text file created by the quiz creator and quizzes the user

import random
# Reads the text file created by the quiz creator and quizzes the user
def load_quiz_data(filename='question_bank.txt'):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    quiz_data = []
    # Reads txt file in groups of 6 lines (1 question, 4 answers, and 1 correct answer)
    for i in range(0, len(lines), 6):
        block = lines[i:i+6]
        if len(block) == 6 and block[0].startswith("Question:"):
            quiz_data.append(block)

    return quiz_data
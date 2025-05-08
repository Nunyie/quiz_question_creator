# Nunyie
# Quiz Giver
# Reads the text file created by the quiz creator and quizzes the user

import random
# Reads the text file created by the quiz creator and quizzes the user
def load_quiz_data(file_name='question_bank.txt'):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    quiz_data = []
    # Reads txt file in groups of 6 lines (1 question, 4 answers, and 1 correct answer)
    for i in range(0, len(lines), 6):
        block = lines[i:i+6]
        if len(block) == 6 and block[0].startswith("Question:"):
            quiz_data.append(block)

    return quiz_data

def run_quiz():
    file_name = 'question_bank.txt'
    # Checks if file exists, if not display error message
    try:
        quiz_data = load_quiz_data(file_name)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return
    
    # Checks if file is empty, if so display error message
    if not quiz_data:
        print("No questions found in txt file.")
        return
    
    # Shuffles the quiz data to randomize the order of questions
    random.shuffle(quiz_data)
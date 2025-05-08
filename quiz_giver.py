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

    score = 0 # Initialize score to 0
    total = len(quiz_data) # Total number of questions

    # Reads each block of data (question, answers, correct answer)
    for block in quiz_data:
        question = block[0]
        options = block[1:5]
        correct_answer = block[5]

        # Display question and options to user
        print("\n" + question)
        for option in options:
            print(option)
        
        # Get user's input
        valid_input = ['A', 'B', 'C', 'D']
        while True:
            user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if user_answer in valid_input:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        # Extracts correct answer from data block
        correct_answer = correct_answer.split(": ")[1].strip().upper()

        # Compares user's answer with the correct answer
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

        # Asks user if they want to continue after each question
        continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_quiz != 'yes':
            print("Thank you for playing!!")
            break
    
    # Final score display
    print("\nQuiz completed!")
    print(f"\nYour final score is {score} out of {total}.")

if __name__ == "__main__":
    run_quiz()
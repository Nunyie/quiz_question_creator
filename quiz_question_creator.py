# Nunyie
# Quiz Creator
# Stores questions inputed by the user and converts it into a text file

def main():
    while True:
        # Ask user for a question
        question = input("Enter a question (or type 'exit' to finish): ")
        if question.lower() == 'exit':
            print("Exiting the quiz creator.")
            break

        # Ask user for 4 possible answers
        answers = {}
        for option in ['A', 'B', 'C', 'D']:
            answer = input(f"Enter answer option {option}: ")
            answers[option] = answer
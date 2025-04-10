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
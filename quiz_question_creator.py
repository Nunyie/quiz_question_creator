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
        for option in ['a', 'b', 'c', 'd']:
            answer = input(f"Enter answer option {option}: ")
            answers[option] = answer

        # Ask user for the correct answer
        correct_answer = input("Enter the correct answer option (a, b, c, or d): ").lower()
        while correct_answer not in answers:
            print("Invalid option. Please enter a, b, c, or d.")
            correct_answer = input("Enter the correct answer option (a, b, c, or d): ").lower()

        # Converts data obtained into a text file in the same folder as the code
        with open('question_bank.txt', 'a') as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"{option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer.upper()}\n\n")

        print("Question and answers saved to question_bank.txt.")

if __name__ == "__main__":
    main()
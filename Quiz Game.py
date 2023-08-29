#  Author - Abhiraj  Singh
#  Task - Quiz Game



import random

questions = [
    {
        "question": "What is the capital of India?",
        "type": "multiple_choice",
        "choices": ["UP", "Goa", "Delhi", "Mumbai"],
        "correct_answer": "Delhi",
    },
    {
        "question": "What is the full form of ISRO?",
        "type": "multiple_choice",
        "choices": ["Indian Scholar Research Organization", "Indian Space Research Organization", " Indian Station Research Organization", "None"],
        "correct_answer": "Indian Space Research Organization",
    },
{
        "question": "The chemical symbol for water is _?",
        "type": "fill_in_the_blank",
        "correct_answer": "H2O",
    },
{
        "question": "Where is the headquarters of ISRO?",
        "type": "multiple_choice",
        "choices": ["Chennai", "Bengaluru", "Delhi", "Mumbai"],
        "correct_answer": "Bengaluru",
    },
]


def shuffle_questions(questions):
    random.shuffle(questions)


def ask_fill_in_the_blank_question(question):
    print(question["question"])
    user_answer = input("Your answer: ")
    return user_answer.strip()


def ask_multiple_choice_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"], start=1):
        print(f"{i}. {choice}")
    user_answer = input("Enter the number of your answer: ")
    return question["choices"][int(user_answer) - 1]


def is_correct(answer, correct_answer):
    return answer.lower() == correct_answer.lower()  # Case-insensitive comparison


def run_quiz(questions):
    shuffle_questions(questions)
    score = 0
    for question in questions:
        if question["type"] == "multiple_choice":
            user_answer = ask_multiple_choice_question(question)
        elif question["type"] == "fill_in_the_blank":
            user_answer = ask_fill_in_the_blank_question(question)

        if is_correct(user_answer, question["correct_answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question['correct_answer']}.\n")

    print(f"Quiz completed! You got {score}/{len(questions)} correct answers.")
    return score

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

       
if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    while True:
        score = run_quiz(questions)
        print(f"Your final score: {score}/{len(questions)}\n")
        if not play_again():
            break
    print("Thank you for playing!")

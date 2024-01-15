#!/usr/bin/python3
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, (question, correct_answer) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"\nQuiz completed! Your score: {score}/{total_questions}")

# Example questions (format: (question, correct_answer))
quiz_questions = [
    ("What is the keyword used to define a function?", "def"),
    ("How do you comment out a single line in python?", "#"),
    ("Which loop is used for iterating over a sequence of items in python?", "for"),
    # Add more questions as needed
]

# Run the quiz
run_quiz(quiz_questions)

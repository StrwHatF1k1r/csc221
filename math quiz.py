import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operator} {num2}?"
    answer = eval(str(num1) + operator + str(num2))
    return question, answer

def check_answer(question, user_answer):
    _, correct_answer = question
    return int(user_answer) == correct_answer

def run_quiz():
    score = 0
    for i in range(10):
        question = generate_question()
        print(question[0])
        user_answer = input("Your answer: ")
        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question[1]}\n")
    print(f"Quiz completed! Your score: {score}/10")
    
    if score >= 8:
        print("Great job! You did well.")
    elif score >= 6:
        print("Not bad, but you can do better. Give it another try.")
    else:
        print("Try again. You can improve!")


run_quiz()

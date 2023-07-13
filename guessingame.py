import random

def guess_number():
    target_number = random.randint(0, 1000000)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a random number between 0 and 1000000. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts!")
            return attempts

def play_game():
    leaderboard = []
    
    while True:
        attempts = guess_number()
        leaderboard.append(attempts)
        leaderboard.sort()
        
        print("Leaderboard:")
        for i, score in enumerate(leaderboard):
            print(f"{i+1}. Attempts: {score}")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()

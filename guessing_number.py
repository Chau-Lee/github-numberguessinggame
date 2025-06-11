import random

def main_menu():
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number from 1 to 100
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
        """)
    while True:
        difficulty_chose = input("Please select a mode: ").lower()
        if difficulty_chose == "easy" or 1:
            main_game(10)
            break
        elif difficulty_chose == "medium" or 2:
            main_game(5)
            break
        elif difficulty_chose == "hard" or 3:
            main_game(3)
            break
        else:
            print("Invalid choice! Please type 1 of 3 hardness")

def main_game(max_attempts):
    random_number = random.randint(1,100)
    attempts = 0

    while attempts < max_attempts:
        try:
            user_guess = int(input("Please enter your guess number: "))
        except ValueError:
            print("Not invalid, please enter a number: ")
            attempts += 1

        attempts += 1

        if user_guess == random_number:
            print("Congrats! You've guessed the correct number!")
        elif user_guess < random_number:
            print("Higher!")
        else:
            print("Lower!")

        print(f"Attempts left: {max_attempts - attempts}")

    print(f"Game over! The number was {random_number}")

main_menu()
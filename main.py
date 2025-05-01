import random

print("🎯 Welcome to the Number Guessing Game!")

# Main game loop
while True:
    print("\nI'm thinking of a number between 1 and 100.")

    # Choose difficulty level
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty == 'easy':
            max_attempts = 10
            break
        elif difficulty == 'medium':
            max_attempts = 5
            break
        elif difficulty == 'hard':
            max_attempts = 3
            break
        else:
            print("Invalid choice. Please type easy, medium, or hard.")

    secretNumber = random.randint(1, 100)
    print(f"You have {max_attempts} chances to guess the correct number.")

    # Guessing loop
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f'Attempt {attempt} - Take a guess: '))
                break
            except ValueError:
                print("Please enter a valid number.")

        if guess < secretNumber:
            print(f"Too low! Try a higher number than {guess}.")
        elif guess > secretNumber:
            print(f"Too high! Try a lower number than {guess}.")
        else:
            break  # correct guess

    # End result
    if guess == secretNumber:
        print(f'Good job! You guessed my number in {attempt} guesses.')
    else:
        print(f'Nope, the number I was thinking of was {secretNumber}.')
        if guess < secretNumber:
            print("Your last guess was too low.")
        else:
            print("Your last guess was too high.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! 👋")
        break

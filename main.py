import random

print("Welcome to the ShuaLyons Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choose difficulty level
while True:
    difficulty = input("Please select the difficulty level: \n1.Easy (10 Chances) \n2.Medium (5 Chances) \n3.Hard (3 Chances)\nEnter your choice: ").lower()
    if difficulty == '1':
        max_attempts = 10
        break
    elif difficulty == '2':
        max_attempts = 5
        break
    elif difficulty == '3':
        max_attempts = 3
        break
    else:
        print("Invalid choice. Please type 1, 2, or 3.")

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
        print(f'The number is higher than {guess}')
    elif guess > secretNumber:
        print(f'The number is lower than {guess}')
    else:
        break  # correct guess

# End result
if guess == secretNumber:
    print(f'Good job! You guessed my number in {attempt} guesses.')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))

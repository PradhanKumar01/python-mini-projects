import random

secret_number = random.randint(1, 20)
max_attempts = 5
attempt = 1

print("Guess the number between 1 and 20")
print("You have only 5 attempts")

while attempt <= max_attempts:
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print(" Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Hint: Number is higher")
    else:
        print("Hint: Number is lower")

    attempt += 1

if attempt > max_attempts:
    print("cross Game Over!")
    print("The correct number was:", secret_number)

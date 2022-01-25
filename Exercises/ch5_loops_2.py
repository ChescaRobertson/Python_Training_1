import random

magic_number = random.randint(1,10)

for i in range(3):
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == magic_number:
        print("Correct, you win!")
        break
    elif user_guess > magic_number:
        print(f"You guessed {user_guess}. Too high")
    elif user_guess < magic_number:
        print(f"You guessed {user_guess}. Too low")
else:
    print(f"You lose the number was: {magic_number}")
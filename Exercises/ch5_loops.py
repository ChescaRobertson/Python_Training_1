import random

magic_number = random.randint(1,10)
guesses_left = 3

while guesses_left > 0:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == magic_number:
        print("Correct, you win!")
        break
    elif guesses_left > 1 and user_guess > magic_number:
        print(f"You guessed {user_guess}. Too high")
        guesses_left -= 1
    elif guesses_left > 1 and user_guess < magic_number:
        print(f"You guessed {user_guess}. Too low")
        guesses_left -= 1
    else:
        print(f"You lose the number was: {magic_number}")
        break
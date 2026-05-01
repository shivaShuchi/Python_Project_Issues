import random

def generate_number():
    return random.randint(1, 100)

def get_guess():
    try:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        return guess
    except ValueError:
        print("Invalid input, Please enter a number.\n")
        return None

def check_guess(guess, secret_number):
    # Check if the guess is correct
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        return True
    elif guess < secret_number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")
    return False

def play_game():
    # Introduction
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.")

    secret_number = generate_number()
    # Set the number of allowed attempts
    attempts = 7

    # Game loop
    while attempts > 0:
        guess = get_guess()

        if guess is None:
            continue

        if check_guess(guess, secret_number):
            return

        attempts -= 1
        print(f"Attempts left: {attempts}\n")
    print(f"❌ Game over! The number was {secret_number}.")

if __name__ == "__main__":
    # Run the game
    play_game()

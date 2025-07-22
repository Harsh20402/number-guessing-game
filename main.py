from random import randint
import time
import os

class NumberGuess:
    def __init__(self, param1):
        # Initialize the game with the user's name.
        self.user_name = param1
        self.random_number = None
        self.attempts = 0

    def run(self):
        # Start the game: generate a random number and begin taking guesses.
        self.generate_random_no()
        self.take_user_input()

    def generate_random_no(self):
        # Generate a random number between 1 and 100 and inform the user.
        print(f"Just wait {self.user_name}! I'm thinking of a number between 1 and 100.")
        time.sleep(1)
        self.random_number = randint(1, 100)

    def take_user_input(self):
        # Continuously prompt the user for guesses until the correct number is guessed.
        while True:
            user_input = input("Enter your guess: ").strip()
            print("Please wait for a while to check the input...")
            time.sleep(1)

            # Check if input is a digit
            if user_input.isdigit():
                user_choice = int(user_input)
                # Validate input range and process guess
                if self.check_user_input(user_choice):
                    self.attempts += 1
                    if self.compare_number(user_choice):
                        break  # Correct guess, end loop
            else:
                print("⚠️  Invalid input. Please enter a number between 1 and 100.")

    def check_user_input(self, param1):
        # Check if the user's guess is within the valid range (1-100).        
        if 1 <= param1 <= 100:
            return True
        else:
            print(f"⚠️  {self.user_name}, {param1} is out of range. Please enter a number between 1 and 100.")
            return False

    def compare_number(self, guess):
        # Compare user's guess with the random number and provide feedback.
        if guess < self.random_number:
            print("Too low! Try a higher number.")
            return False
        elif guess > self.random_number:
            print("Too high! Try a lower number.")
            return False
        else:
            print(f"🎉  Congratulations {self.user_name}, you guessed it right in {self.attempts} attempt(s)!")
            self.check_number_of_attempts(self.attempts)
            return True
      
    def check_number_of_attempts(self, attempts):
        # Check and update the record for the lowest number of attempts.
        # Saves to 'low_attemps.txt' in the same directory.
        filename = "low_attempts.txt"

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read().strip()
                previous_low = int(content) if content.isdigit() else None
        else:
            previous_low = None
            
        if previous_low is None or attempts < previous_low:
            print(f"🏆 New record! {self.user_name} set a new low score of {attempts} attempts.")
            with open(filename, 'w') as f:
                f.write(str(attempts))
        else:
            print(f"📉 Best score so far is {previous_low} attempts.")

def main():
    # Entry point of the game.
    time.sleep(1)
    print("\033[1;95m🎉 Welcome to the Number Guessing Game!\033[0m")
    user_name = input("Enter Your Name: ").strip()
    while not user_name:
        user_name = input("Please enter a valid name: ").strip()
    app = NumberGuess(user_name)
    while True:
        app.run()
        user_reply = input(f"{user_name}! Do you want to play again? (Y/N): ").strip().lower()
        if user_reply != "y":
            print("👋 Thanks for playing! See you next time.")
            break

# Run the game with graceful Ctrl+C exit
try:
    main()
except KeyboardInterrupt:
    print("\n👋 Game exited by user. Goodbye!")
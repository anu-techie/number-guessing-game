import random
import time
from game.utils import get_difficulty_level, update_high_scores

def play_game():
    computer_guess = random.randint(1, 100)
    level, attempts = get_difficulty_level()
    tries = 0
    start_time = time.time()
    low, high = 1, 100

    while attempts > 0:
        try:
            user_guess = int(input("Enter your guess: "))
            tries += 1
            if user_guess == computer_guess:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"🎉 Correct! You guessed it in {tries} attempts within {total_time} seconds.")
                update_high_scores(level, tries)
                break
            elif user_guess > computer_guess:
                print(f"❌ Too high! The number is less than {user_guess}.")
                high = user_guess - 1
            else:
                print(f"❌ Too low! The number is greater than {user_guess}.")
                low = user_guess + 1

            if attempts == 2:
                mid_point = (low + high) // 2
                print(f"🔎 Hint: Try around {mid_point}")

            attempts -= 1

        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

    if attempts == 0 and user_guess != computer_guess:
        print(f"😢 Out of attempts! The correct number was {computer_guess}.")

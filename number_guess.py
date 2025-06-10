import random
import time

difficulty_level = {
    "1" : ('easy',10),
    "2" : ('medium',5),
    "3" : ("hard", 3)
}
high_scores = {
    "easy" : None,
    "medium" : None,
    "hard" : None
}

def show_welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Guess the correct in few attempts as much as possible.")

def get_difficulty_level():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = input("Enter Your Choice 1/2/3 : ")
    if choice in difficulty_level:
        level, chances = difficulty_level[choice]
        print(f"Great! You have selected the difficulty level as {level} and you have {chances} chances.")
        return level, chances
    print("Invalid Input. Please chooose 1,2 or 3")
def play_game():
    computer_guess = random.randint(1,100)
    level, attempts = get_difficulty_level()
    tries = 0
    start_time = time.time()
    low, high = 1, 100
    while attempts > 0:
        try:
            user_guess = int(input("Enter your guess : "))
            tries += 1
            if user_guess == computer_guess:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"Congratulations! You guessed the correct number in {tries} attempts within {total_time}.")
                update_high_scores(level, tries)
                break
            elif computer_guess < user_guess :
                print(f"Incorrect! The number is less than {user_guess}.")
                high = user_guess-1
            else:
                print(f"Incorrect! The number is greater than {user_guess}.")
                low = user_guess+1

            if attempts is 2:    
                mid_point = (low + high) // 2
                print(f"Hint: Try around {mid_point}")  
            attempts -= 1 

        except ValueError:
            print("Invalid Input. Please enter a valid number")
    if attempts == 0 and  user_guess != computer_guess:
        print(f"Sorry, You have run out of attempts and the correct number was {computer_guess}")

def update_high_scores(level, attempts):
    current_score = high_scores[level]
    if current_score is None or attempts < current_score:
        high_scores[level] = attempts
        print(f"New high score for {level} difficulty : {attempts} attempts")
    else:
        print(f"Your best for {level} difficulty is still {current_score} attempts")

def show_high_score():
    print("\n =======High Scores=======")
    for level, score in high_scores.items():
        print(f"{level} : {score if score else "No score yet"}")
    print("\n =========================")

def main():
    show_welcome()
    while True:
        play_game()
        show_high_score()
        play_again = input("Do you want to play again? (Y/N) : ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! See you next time")
            break

if __name__ == "__main__":
    main()
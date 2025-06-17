difficulty_level = {
    "1": ("easy", 10),
    "2": ("medium", 5),
    "3": ("hard", 3)
}

high_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}

def show_welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Guess the correct number in as few attempts as possible.\n")

def get_difficulty_level():
    while True:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        choice = input("Enter Your Choice 1/2/3 : ")
        if choice in difficulty_level:
            level, chances = difficulty_level[choice]
            print(f"\n✅ Great! You've selected '{level}' difficulty with {chances} chances.\n")
            return level, chances
        print("❗ Invalid Input. Please choose 1, 2, or 3.\n")

def update_high_scores(level, attempts):
    current_score = high_scores[level]
    if current_score is None or attempts < current_score:
        high_scores[level] = attempts
        print(f"🏆 New high score for {level} difficulty: {attempts} attempts")
    else:
        print(f"👍 Your best for {level} difficulty is still {current_score} attempts")

def show_high_score():
    print("\n======= High Scores =======")
    for level, score in high_scores.items():
        print(f"{level.capitalize()} : {score if score else 'No score yet'}")
    print("===========================\n")

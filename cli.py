from game.utils import show_welcome, show_high_score
from game.core import play_game

def main():
    show_welcome()
    while True:
        play_game()
        show_high_score()
        play_again = input("Do you want to play again? (Y/N) : ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()

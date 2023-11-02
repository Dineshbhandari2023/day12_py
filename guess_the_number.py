import random
from art import logo

# Global Constant
EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, turns):
        """checks the answer against guess and return the number of turns remaining."""
        if guess > answer:
            print("To High!!")
            return turns - 1
        elif guess < answer:
            print("To low!!")
            return turns - 1
        else:
            print(f"You got it! The answer is {answer}.")
            
def set_difficulty():
    level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


            
def game():
    print(logo)
    print("WelCome to tme Numer Guessing Game!")
    print("I am thinking the number between 1-100. Now Guess the number.")
    answer = random.randint(1,100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print(f"You have run out of the game, you loose!!")
            return
        elif guess != answer:
            print("Guess again!")
        
game()















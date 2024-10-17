"""
A simple memory GUESSING game 
Promps the user to input a value to guess then loops till guess is found or quit
"""
import random
import sys
print('Hello welcome to a simple GUESSING game')
PLAYING = True
def is_integer(variable):
    """
    Returns true if num is a valid number
    """
    return isinstance(variable,int)
class MaxTooSmallError(Exception):
    """
    An error for if max is smaller than min
    """
    def __init__(self, message):
        self.message = message
while PLAYING is True:
    guessMax = input('Select a max number to guess: ')
    guessMin = input('Select a minimum number to guess: ')
    try:
        if int(guessMax) < int(guessMin):
            raise MaxTooSmallError("Max is too small")
        guessMin = int(guessMin)
        guessMax = int(guessMax)
        number_to_guess = random.randint(int(guessMin),int(guessMax))
        print(f"\nNumber to guess {number_to_guess}")
        GUESSING = True
        while GUESSING is True:
            guess = input("Take a guess: ")
            try:
                guess = int(guess)
                match guess:
                    case guess if guess > guessMax:
                        print("\nGuess is too high")
                    case guess if guess < guessMin:
                        print("\nGuess is too low")

                if is_integer(guess) is False:
                    raise ValueError("Error! guess failed number check")
                GUESS = int(guess)
                if GUESS == number_to_guess:
                    print('\nYay u win!\n')
                    CONTINUE = True
                    while CONTINUE is True:
                        again = input("Wanna play again? (y/n) ")
                        if again == 'y':
                            GUESSING = False
                            CONTINUE = False
                        elif again =='n':
                            PLAYING = False
                            GUESSING = False
                            CONTINUE = False
                else:
                    print('\nWrong. Please try again\n')
            except ValueError:
                print('\nYour guess needs to be a number')
    except ValueError:
        if is_integer(guessMax) is False:
            print('\nmax not a num')
        elif is_integer(guessMin) is False:
            print('\nmin not a num')
    except MaxTooSmallError:
        print(f"\nCan\'t work with a max({guessMax}) that is smaller than the min({guessMin})")
print("Thanks for playing :)")
sys.exit()

"""
A simple memory GUESSING game 
Promps the user to input a value to guess then loops till guess is found or quit
"""
import random
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

        number_to_guess = random.randint(int(guessMin),int(guessMax))
        print(f"\nNumber to guess {number_to_guess}")
        GUESSING = True
        while GUESSING is True:
            guess = input("Take a guess: ")
            try:
                if is_integer(guess) is False:
                    raise ValueError("Error! guess failed number check")

                guess = int(guess)
                print(guess)
                if guess == number_to_guess:
                    print('yay u win')
                    GUESSING = False
                else:
                    print('Wrong. Please try again')
            except ValueError:
                print('\nError with guess')
    except ValueError:
        if is_integer(guessMax) is False:
            print('\nmax not a num')
        elif is_integer(guessMin) is False:
            print('\nmin not a num')
    except MaxTooSmallError:
        print(f"Can\'t work with a max({guessMax}) that is smaller than the min({guessMin})")
    finally:
        print("\nLet\'s try that again")

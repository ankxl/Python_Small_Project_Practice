"""
Bagels, A deductive logic game where you must guess a number based on clues.
Tags: game, puzzle
"""

import random


NUM_DIGITS = 3 # Num_DIGITS define the number of digits in number being guessed and guesses
MAX_GUESSES = 10 # MAX_GUESSES define the total chances available to guess the number

def get_secret_num():
    """ Finds a 3 digit number (string) randomly without any repeating digits.
        The approach allows 0 as a leading digit thus strings are used instead of numbers
        as numbers will truncate the leading zero to a two-digit number.
    """
    numbers = list('0123456789')
    random.shuffle(numbers) # randomly shuffle the order of the list
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return(secret_num)

def get_clues(guess,secret_num):
    """ Checks if the user has guessed the correct number. If the guess is not the
        number, the computer provides clues to the user to improve the accuracy of
        their guess.
        When user says:         That means:
            Pico                One digit is correct but in the wrong position
            Fermi               One digit is correct and in the right position
            Bagels              No digit is correct
    """
    if guess == secret_num:
        return('You got it!')
    
    clues = []

    # run through the sequence to identify matches in the right or wrong position and add clues to the list 
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    
    # Empty clue string means all the numbers were incorrect and thus should return Bagel
    if len(clues) == 0:
        return('Bagels')
    
    #Clues are sorted to increase difficulty level 
    clues.sort()
    return( ' '.join(clues))
    


def main():
    print(f"""Bagels, a deductive logic game.
        
I am thinking of a {NUM_DIGITS}-number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:         That means:
    Pico            One digit is correct but in the wrong position
    Fermi           One digit is correct and in the right position
    Bagels          No digit is correct

For example, if the secret number was 736 and your guess was 176, 
the clues would be Fermi Pico.
""")
    
    while True:
        secret_num = get_secret_num()
        print('I have thought up a number')
        print(f'You have {MAX_GUESSES} guesses to get it')
        
        num_of_guess = 1
        while num_of_guess <= MAX_GUESSES:
            print(f'Guess #{num_of_guess}:')
            guess = input("> ")

            if (len(guess) != NUM_DIGITS) or (not guess.isdecimal()):
                print("Invalid Guess")
            else:
                clues = get_clues(guess,secret_num)
                print(clues)
            
            num_of_guess += 1

            if guess == secret_num:
                break

            if num_of_guess > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")
            
        print('Do you want to play again? (Yes(y)/ No(n))')
        if not input("> ").lower().startswith('y'):
            break
    print('Thanks for playing!')


if __name__ == '__main__':
    main()
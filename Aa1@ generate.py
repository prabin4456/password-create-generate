import random
import itertools

Range_1 = int(input("enter password range: "))
Range_2 = Range_1 + 1

lower="abc"
upper="ABC"
numbers="0123456789"
symbols="&!@%?."

def guess_password(real):
    chars =  lower+upper+numbers+symbols
    attempts = 0

    for password_length in range(Range_1 , Range_2):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess)

print(guess_password('>>>>>>>>>>>'))

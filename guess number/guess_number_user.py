# Computer generates a secret number & user tries to guess that number

import random


def guess_number_user(n):
    secret_num = random.randint(1, n)
    guess = 0
    while guess != secret_num:
        guess = int(input(f"Guess a number a between 1-{n}: "))
        if guess > secret_num:
            print(f"Your guess is too high.")
        elif guess < secret_num:
            print("Your guess is too low.")
    print(f"Congrats, your guessed it right - {secret_num}.")


# guess_number_user(10)

# Computer tries to guess the secret number

def guess_number_computer(x):
    lbound = 1
    hbound = x
    response = ''
    guess = 0
    while response.lower() != 'c':
        guess = (lbound + hbound) // 2
        response = input(f"Is {guess} is too High (H), too low (L) or correct (C) ? ")
        if response.lower() == 'h':
            hbound = guess - 1
        elif response.lower() == 'l':
            lbound = guess + 1
    print(f"Yay! {guess} it is..")


guess_number_computer(1000)

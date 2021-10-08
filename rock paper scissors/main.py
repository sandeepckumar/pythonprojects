# r > s, s > p, p > r

import random


def game():
    computer = random.choice(['r', 'p', 's'])
    user = input("Pick 'r' for rock, 'p' for paper or 's' for scissors: ").lower()
    if user == computer:
        return "It's a tie."
    if user_won(user, computer):
        return "You won!"
    return "You lost!"


def user_won(user, computer):
    if user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
        return True


print(game())

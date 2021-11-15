#!/usr/bin/env python3
from brain_games.scripts.script_games import random_generate as rg


def even(name):

    print('Answer "yes" if number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_number = rg()
        print(f'Question: {random_number}')
        guess = input('Your answer: ').lower()

        if random_number % 2 == 0 and guess == 'yes':
            count += 1
            print('Correct!')

        elif random_number % 2 == 0 and guess == 'no':
            return print(f'"{guess}" is wrong answer ;(. '
                         f'Correct answer was "yes"\n'
                         f'Let\'s try again, {name}!')

        elif random_number % 2 != 0 and guess == 'no':
            count += 1
            print('Correct!')

        else:
            return print(f'"{guess}" is wrong answer ;(. '
                         f'Correct answer was "no"\n'
                         f'Let\'s try again, {name}!')

    if count == 3:
        return print(f'Congratulations, {name}!')


def main():
    even(input())


if __name__ == '__main__':
    main()

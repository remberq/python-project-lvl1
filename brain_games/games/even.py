#!/usr/bin/env python3
import random


def even(name):
    count = 0

    while count < 3:
        random_number = random.randrange(1, 100)
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

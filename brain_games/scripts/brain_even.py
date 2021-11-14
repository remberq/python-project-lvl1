#!/usr/bin/env python
import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    def even():
        count = 0
        print('Answer "yes" if number is even, otherwise answer "no".')

        while count < 3:
            random_number = random.randrange(1, 100)
            print(f'Question: {random_number}')
            guess = input('Your answer: ')

            if random_number % 2 == 0 and guess.lower() == 'yes':
                count += 1
                print('Correct!')

            elif random_number % 2 == 0 and guess.lower() == 'no':
                return print(f'"{guess.lower()}" is wrong answer ;(. '
                             f'Correct answer was "yes"\n'
                             f'Let\'s try again, {name}!')

            elif random_number % 2 != 0 and guess.lower() == 'no':
                count += 1
                print('Correct!')

            else:
                return print(f'"{guess.lower()}" is wrong answer ;(. '
                             f'Correct answer was "no"\n'
                             f'Let\'s try again, {name}!')

        if count == 3:
            return print(f'Congratulations, {name}!')

    even()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import random


def calc(name):
    score = 0
    i = 0
    while i < 3:

        num_1 = random.randrange(50, 100)
        num_2 = random.randrange(1, 49)
        symbol = random.randrange(1, 4)

        if symbol == 1:
            print(f'Question: {num_1} + {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 + num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
                i += 1
            else:
                return print(f'"{answer}" is wrong answer ;(. '
                             f'Correct answer was {right_answer}\n'
                             f'Let\'s try again, {name}!')

        if symbol == 2:
            print(f'Question: {num_1} - {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 - num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
                i += 1
            else:
                return print(f'"{answer}" is wrong answer ;(. '
                             f'Correct answer was {right_answer}\n'
                             f'Let\'s try again, {name}!')

        if symbol == 3:
            print(f'Question: {num_1} * {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 * num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
                i += 1
            else:
                return print(f'"{answer}" is wrong answer ;(. '
                             f'Correct answer was {right_answer}\n'
                             f'Let\'s try again, {name}!')

    if score == 3:
        print(f'Congratulations, {name}!')


def main():
    calc('test')


if __name__ == '__main__':
    main()

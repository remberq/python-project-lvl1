#!/usr/bin/env python3
from brain_games.scripts.script_games import random_generate as rg
from brain_games.scripts.script_games import wrong_result as wr
from brain_games.scripts.script_games import gcd_game


def brain_gcd(name):

    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count < 3:
        num_1 = rg()
        num_2 = rg()

        print(f'Question: {num_1} {num_2}')
        answer = input('Your answer: ')
        right_answer = str(gcd_game(num_1, num_2))
        print(right_answer)

        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wr(answer, right_answer, name)

    print(f'Congratulations, {name}!')


def main():
    brain_gcd('test')


if __name__ == '__main__':
    main()

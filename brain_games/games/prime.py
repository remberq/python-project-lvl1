#!/usr/bin/env python3
import random
from brain_games.scripts.script_games import wrong_result as wr


def is_prime(num):

    if num < 2:
        return True

    elif num % 2 == 0:
        return False

    else:
        for i in range(3, num):
            if num % i == 0:
                return False

        return True


def yes_no(num):

    if is_prime(num):
        right_answer = 'yes'
        return right_answer

    else:
        right_answer = 'no'
        return right_answer


def prime_logic(name):

    score = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while score < 3:

        num = random.randrange(1, 100)
        right_answer = yes_no(num)

        print(f'Question: {num}')
        answer = input('Your answer: ').lower()

        if answer == right_answer:
            print('Correct!')
            score += 1

        else:
            return wr(answer, right_answer, name)

    return print(f'Congratulations, {name}!')


def main():
    prime_logic('vasya')


if __name__ == '__main__':
    main()

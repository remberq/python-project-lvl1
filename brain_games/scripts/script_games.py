#!/usr/bin/env python3
import prompt
import random


def greetings():
    print('Welcome to the Brain Games!')

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print(f'Hello, {name}!')
        return name

    return welcome_user()


def gcd_game(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2

        else:
            num_2 = num_2 % num_1
    return num_2 + num_1


def random_generate(start=1, stop=100):
    num = random.randrange(start, stop)
    return num


def list_numbers(num1, num2, num3):
    list_of_num = []
    i = 0

    for el in range(num1, num2, num3):
        if i < 11:
            i += 1
            list_of_num.append(el)
    return list_of_num


def wrong_result(answer, right_answer, name):
    print(f'"{answer}" is wrong answer ;(. '
          f'Correct answer was {right_answer}\n'
          f'Let\'s try again, {name}!')


def main():
    greetings()


if __name__ == '__main__':
    main()

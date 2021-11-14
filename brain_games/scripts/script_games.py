#!/usr/bin/env python3
import prompt


def greetings():
    print('Welcome to the Brain Games!')

    def welcome_user():
        name = prompt.string('May I have your name? ')
        print(f'Hello, {name}!')
        return name

    return welcome_user()


def questions():
    print('Answer "yes" if number is even, otherwise answer "no".')


def main():
    greetings()
    questions()


if __name__ == '__main__':
    main()

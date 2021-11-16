#!/usr/bin/env python3
from operator import add, mul, sub
import prompt
import random


def start_calc():
    token = {1: "+", 2: "*", 3: "-"}
    d = {1: add, 2: mul, 3: sub}
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    for i in range(3):
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        action = random.randint(1, 3)
        print(f"Question: {num1} {token[action]} {num2}")
        ans = int(input("Your answer: "))
        if d[action](num1, num2) == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.", end="")
            print(f"Correct answer was '{d[action](num1, num2)}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


def main():
    start_calc()


if __name__ == '__main__':
    main()

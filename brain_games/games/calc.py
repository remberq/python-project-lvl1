
from brain_games.scripts.script_games import wrong_result, random_generate
import random


def calc(name):
    print('What is the result of the expression?')
    score = 0

    while score < 3:

        num_1 = random_generate(50, 100)
        num_2 = random_generate(1, 50)
        symbol = ['-', '*', '+']
        i = random.randrange(len(symbol))
        print(symbol[i])

        if i == 0:
            print(f'Question: {num_1} {symbol[i]} {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 - num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
            else:
                return wrong_result(answer, right_answer, name)

        elif i == 1:
            print(f'Question: {num_1} {symbol[i]} {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 * num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
            else:
                return wrong_result(answer, right_answer, name)

        else:
            print(f'Question: {num_1} {symbol[i]} {num_2}')
            answer = input('Your answer: ')
            right_answer = str(num_1 + num_2)
            if answer == right_answer:
                print('Correct!')
                score += 1
            else:
                return wrong_result(answer, right_answer, name)

    if score == 3:
        print(f'Congratulations, {name}!')


def main():
    calc('test')


if __name__ == '__main__':
    main()

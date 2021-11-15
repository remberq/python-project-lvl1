#!/usr/bin/env python3
from brain_games.scripts.script_games import random_generate as rg
from brain_games.scripts.script_games import list_numbers as ln
from brain_games.scripts.script_games import wrong_result as wr


def game_progression(name):
    score = 0
    print('What number is missing in the progression?')

    while score < 3:

        n1 = rg(1, 100)
        n2 = rg(200, 400)
        n3 = rg(2, 10)
        n4 = rg(1, 9)

        list_num = ln(n1, n2, n3)
        right_answer = str(list_num.pop(n4))
        list_num.insert(n4, '..')

        print(f'Question: {list_num}')
        answer = input('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            score += 1
        else:
            return wr(answer, right_answer, name)

    if score == 3:
        print(f'Congratulations, {name}!')


def main():
    game_progression('ssa')


if __name__ == '__main__':
    main()

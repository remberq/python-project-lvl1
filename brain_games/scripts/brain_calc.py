#!/usr/bin/env python3
from brain_games.scripts.script_games import greetings
from brain_games.games.calc import calc


def calculated_game():
    name = greetings()
    calc(name)


def main():
    calculated_game()


if __name__ == '__main__':
    main()

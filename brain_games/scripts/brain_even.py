#!/usr/bin/env python3
from brain_games.scripts.script_games import greetings, questions
from brain_games.games.even import even


def even_game():
    name = greetings()
    questions()
    even(name)


def main():
    even_game()


if __name__ == '__main__':
    main()

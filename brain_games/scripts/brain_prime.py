#!/usr/bin/env python3
from brain_games.scripts.script_games import greetings
from brain_games.games.prime import prime_logic


def game_prime():
    name = greetings()
    prime_logic(name)


def main():
    game_prime()


if __name__ == '__main__':
    main()

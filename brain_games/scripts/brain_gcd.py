#!/usr/bin/env python3
from brain_games.scripts.script_games import greetings
from brain_games.games.gcd import brain_gcd


def brain_gcd_game():
    name = greetings()
    brain_gcd(name)


def main():
    brain_gcd_game()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from brain_games.scripts.script_games import greetings
from brain_games.games.progression import game_progression


def brain_game_progression():
    name = greetings()
    game_progression(name)


def main():
    brain_game_progression()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from brain_games.cli import welcome_user as wu

def greet():
    print('Welcome to the Brain Games!')
    wu()

def main():
    greet()


if __name__ == '__main__':
    main()

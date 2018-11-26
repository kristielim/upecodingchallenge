#!/usr/local/bin/python3
from req import *

def play_maze():
    

def main():
    token = get_token()
    game = get_game(token)
    total_levels = game['total_levels']
    for i in range(total_levels):
        play_maze(token)

if __name__ == '__main__':
    main()
#!/usr/local/bin/python3
from req import *

# helper function to find solution of the maze
def find_solution(token, curr_pos, prev_moves, visited):
    curr_x, curr_y = curr_pos
    directions_dict = {
        'RIGHT': (curr_x + 1, curr_y),
        'DOWN': (curr_x, curr_y + 1),
        'LEFT': (curr_x - 1, curr_y),
        'UP': (curr_x, curr_y - 1)
    }

    for direction in directions_dict:
        next_pos = directions_dict[direction]
        # if the next move is not visited
        if next_pos not in visited:
            # move in given direction
            result = move(token, direction)
            if result == 'END':
                print('Solution found!')
                return
            elif result == 'SUCCESS':
                prev_moves.append(direction)
                print(prev_moves)
                visited.add(next_pos)
                find_solution(token, next_pos, prev_moves, visited)
        
    # if no moves are possible
    backwards_move = prev_moves.pop()
    move(token, backwards_move)
    find_solution(token, get_game(token)['current_location'], prev_moves, visited)
        


def play_maze(token, game):
    # initialize state of maze
    start = tuple(game['current_location'])
    prev_moves = []
    visited = set()

    # run the helper function
    find_solution(token, start, prev_moves, visited)


def main():
    token = get_token()
    game = get_game(token)
    total_levels = game['total_levels']
    for i in range(total_levels):
        print(game)
        print(f'Playing maze {i + 1} out of {total_levels}')
        play_maze(token, game)

if __name__ == '__main__':
    main()
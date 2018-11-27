#!/usr/local/bin/python3
import requests

# returns result of a move
def move(token, direction):
    action = {'action': direction}
    return requests.post(f'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token={token}', data=action).json()['result']

# returns a token
def get_token():
    uid = {'uid': '804939731'}
    return requests.post('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session', data=uid).json()['token']

# returns state of the game
def get_game(token):
    return requests.get(f'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token={token}').json()

# helper function to find solution of the maze
def find_solution(token, curr_pos, visited):
    curr_x, curr_y = curr_pos
    directions_dict = {
        'RIGHT': (curr_x + 1, curr_y),
        'DOWN': (curr_x, curr_y + 1),
        'LEFT': (curr_x - 1, curr_y),
        'UP': (curr_x, curr_y - 1)
    }
    opposite = {
        'RIGHT': 'LEFT',
        'LEFT': 'RIGHT',
        'UP': 'DOWN',
        'DOWN': 'UP'
    }

    for direction in directions_dict:
        next_pos = directions_dict[direction]
        # if the next move is not visited
        if next_pos not in visited:
            # move in given direction
            result = move(token, direction)
            if result == 'END':
                print('Solution found!')
                return 1
            elif result == 'SUCCESS':
                visited.add(next_pos)
                if find_solution(token, next_pos, visited) == 1:
                    return 1
                move(token, opposite[direction])
    return 0
        


def play_maze(token, game):
    # initialize state of maze
    start = tuple(game['current_location'])
    visited = set()

    # run the helper function
    find_solution(token, start, visited)


def main():
    token = get_token()
    game = get_game(token)
    status = game['status']
    while status == 'PLAYING':
        game = get_game(token)
        print('Playing the game: ', game)
        play_maze(token, game)
        status = get_game(token)['status']
    if status == 'FINISHED':
        print('Finished!')

if __name__ == '__main__':
    main()
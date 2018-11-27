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
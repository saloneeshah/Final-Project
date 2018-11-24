from random import choice, randint, shuffle
from collections import Counter, defaultdict
import typing
import os
import numpy as np
import pandas as pd
import csv
import random
# import os
# print(os.getcwd())



class Player:
    player_count=0
    all_players = []

    def __init__(self, name=None, tendency=None, adaptive_ai=False):
        Player.player_count += 1
        Player.all_players.append(self)


    def player_1(self):
        global row
        for index, row in enumerate(reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
        kick_direction=(row[10])
        print(kick_direction)

    def goalie(self):

        # direction=['L','R','C']
        # random.shuffle(direction)
        # for i in direction:
        #     print(direction[0])

            num = random.randint(0,30)
            for num in range(1,10):
                direction='L'
            for num in range(10,20):
                direction='R'
            for num in range(20,30):
                direction='C'
            print(direction)

    # def save_penalty(keeper_d:str)-> str:
    #     """Goalie jumps in direction opponent most frequently shoots in
    #         :param keeper_d: 'L', 'R', or 'C'
    #         :return: the goalie's jump in direction to protect the ball from player's goal.
    #             >>> keeper_d('L')
    #             'L'
    #             >>> keeper_d('R')
    #             'R'
    #             >>> keeper_d('C')
    #             'C'
    #             """
    #     goalie_win = {'L': 'L',
    #               'R': 'R',
    #               'C': 'C'}
    #
    #     if keeper_d not in goalie_win.keys():
    #         raise ValueError('')
    #     return goalie_win[keeper_d]

    # def select_player(self):
    #     for row in reader:
    #         shuffle(row[1])
    #         print(row[1])

if __name__ == '__main__':
    with open('C:/Users/Shailesh/Documents/UIUC Assignments/PR/Project/penalty_data.csv') as f:
        reader=csv.reader(f)

        for match in range(10):
            player_1 = Player.player_1(Player)
            goalie = Player.goalie(Player)

        #print(f[1])
        #chosen_row=(list(reader))
        #print(chosen_row)
        # for match in range(10):
        #     player=choice(Player.select_player())

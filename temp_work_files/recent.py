from random import choice, randint
import numpy as np
import math


class Player:
    # player_count = 0
    team = []
    keeper = None
    (team_count_r_total, team_count_l_total, team_count_m_total) = (0, 0, 0)
    team_tendency = [1,1,1]
    team_dir=[]

    def __init__(self, name=None):
        # Player.player_count += 1
        if name != 'Goalie':
                Player.team.append(self)
        else:
            Player.keeper = self
        self.name = name
        (self.wins_case1, self.wins_case2, self.wins_case3) = (0, 0, 0)
        (self.losses_case1, self.losses_case2, self.losses_case3) = (0, 0, 0)
        (self.count_r_total, self.count_l_total, self.count_m_total) = (0, 0, 0)
        self.tendency = [1, 1, 1]


    @staticmethod
    def choose_direction_goalie(team, consider_direction, striker):
        if not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            return jump_dir
        else:
            if not team:
                '''n = randint(1, sum(striker.tendency))
                if n <= striker.tendency[0]:
                    direction = 'Right'
                elif n <= striker.tendency[0] + striker.tendency[1]:
                    direction = 'Left'
                else:
                    direction = 'Middle'
                '''

                cnt = [striker.count_r_total, striker.count_l_total, striker.count_m_total]


                direction_index = [i for i, e in enumerate(cnt) if e == max(cnt)]
                if len(direction_index) == 1:
                    if direction_index == [0]:
                        direction = 'Right'
                    elif direction_index == [1]:
                        direction = 'Left'
                    else:
                        direction = 'Middle'
                elif len(direction_index) == 2:
                    if direction_index == [0, 1]:
                        directions = ['Right', 'Left']
                    elif direction_index == [0, 2]:
                        directions = ['Right', 'Middle']
                    elif direction_index == [1, 2]:
                        directions = ['Left', 'Middle']
                    direction = choice(directions)
                elif len(direction_index) > 2:
                    directions = ['Right', 'Left', 'Middle']
                    direction = choice(directions)
                return direction
            else:
                # '''n = randint(1, sum(Player.team_tendency))
                # if n <= Player.team_tendency[0]:
                #     direction = 'Right'
                # elif n <= Player.team_tendency[0] + Player.team_tendency[1]:
                #     direction = 'Left'
                # else:
                #     direction = 'Middle'
                # '''
                # #cnt = [Player.team_count_r_total, Player.team_count_l_total, Player.team_count_m_total]
                direction_index = [i for i, e in enumerate(Player.team_dir) if e == max(Player.team_dir)]
                if len(direction_index) == 1:
                    if direction_index == [0]:
                        direction = 'Right'
                    elif direction_index == [1]:
                        direction = 'Left'
                    else:
                        direction = 'Middle'
                elif len(direction_index) == 2:
                    if direction_index == [0, 1]:
                        directions = ['Right', 'Left']
                    elif direction_index == [0, 2]:
                        directions = ['Right', 'Middle']
                    elif direction_index == [1, 2]:
                        directions = ['Left', 'Middle']
                    direction = choice(directions)
                elif len(direction_index) > 2:
                    directions = ['Right', 'Left', 'Middle']
                    direction = choice(directions)
                return direction

    def choose_direction_striker(self, team, consider_direction,team_dir):
        if team or not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            return jump_dir
        else:
            n = randint(1, sum(self.tendency))
            if n <= self.tendency[0]:
                #self.tendency[0] += 1
                Player.team_count_r_total += 1
                #Player.team_tendency[0] += 1
                #return 'Right'
                jump_dir='Right'
            elif n <= self.tendency[0] + self.tendency[1]:
                #self.tendency[1] += 1
                Player.team_count_l_total += 1
                #Player.team_tendency[1] += 1
                #return 'Left'
                jump_dir='Left'
            else:
                #self.tendency[2] += 1
                Player.team_count_m_total += 1
                #Player.team_tendency[2] += 1
                #return 'Middle'
                jump_dir='Middle'
        if len(team_dir)==10:
            team_dir.pop(0)
        team_dir.append(jump_dir)
        return jump_dir

    @staticmethod
    def record_play(gk: 'Player', opponent: 'Player', opp_dir: str, winner: 'Player', consider_direction, team):
        # record goalies wins and losses
        if winner == gk:
            if not consider_direction:
                winner.wins_case1 += 1
            else:
                if team:
                    winner.wins_case2 += 1
                else:
                    winner.wins_case3 += 1
        else:
            if not consider_direction:
                Player.keeper.losses_case1 += 1
            else:
                if team:
                    Player.keeper.losses_case2 += 1
                else:
                    Player.keeper.losses_case3 += 1

        # record players selected direction
        if consider_direction:
            if opp_dir == 'Right':
                opponent.count_r_total += 1
                #Player.team_count_r_total += 1
            elif opp_dir == 'Left':
                opponent.count_l_total += 1
                #Player.team_count_l_total += 1
            elif opp_dir == 'Middle':
                opponent.count_m_total += 1
                #Player.team_count_m_total += 1



    def penalty_sim(self,striker, tests, print_result=False, team=False, consider_direction=False):
        # self = goalie, opponent = striker
        goalie_direction = self.choose_direction_goalie(team, consider_direction, striker)
        striker_direction = striker.choose_direction_striker(team, consider_direction,team)
        if goalie_direction == striker_direction:
            different = False
            result = fail_or_succeed(striker_direction, different)
            if result == "Miss" or result == "Save":
                winner = self
            else:
                winner = striker
        else:
            different = True
            result = fail_or_succeed(striker_direction, different)
            if result == "Miss":
                winner = self
            else:
                winner = striker

        Player.record_play(self, striker, striker_direction, winner, consider_direction, team)
        if print_result:
            if result == "Miss":
                print(match, "Player", striker.name, "missed the goal entirely. The winner is the the Goalie")
            else:
                print(match, "Player", striker.name, "kicked to the ", striker_direction,
                      ", goal keeper jumped to the ", goalie_direction, ", the winner is ", winner.name)
        if not consider_direction:
            return (self.wins_case1 / tests) * 100
        else:
            if team:
                return (self.wins_case2 / tests) * 100
            else:
                return (self.wins_case3 / tests) * 100


# outside class Player
def fail_or_succeed(strike_dir, different):
    """

        :param strike_dir: Striker's direction either left right or middle
        :param different: different is just true or false where if both direction are same it is true
        or if both direction are different it is false
        :return: 'Save' or 'Goal'

        >>> fail_or_succeed('Left','True')
        'Save'
        >>> fail_or_succeed('Left','False')
        'Goal'
        >>> fail_or_succeed('Right','True')
        'Save'
        >>> fail_or_succeed('Right','False')
        'Goal'
        >>> fail_or_succeed('Middle','True')
        'Save'
        >>> fail_or_succeed('Middle','False')
        'Goal'
    """
    # create 1 out of 10 chance for player to miss the goal entirely
    n = randint(1, 10)
    if n == 1:
        return "Miss"
    # if player misses, function ends here and returns 'Miss' for both cases, goalie jumps in same/opposite direction
    # if goalie had jumped in opposite direction and player did not miss, function skips the else and returns 'Goal'
    # if goalie jumped in the same direction and player did not miss, program moves to else
    else:
        if not different:
            if strike_dir == "Left" or strike_dir == "Right":
                striker_difficulty = [0, 0, 1, 1, 1, 2]
                goalie_difficulty = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2]
            else:
                striker_difficulty = [0, 0, 0, 0, 1, 1]
                goalie_difficulty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

            select_difficulty = choice(striker_difficulty)
            goalie_choice = choice(goalie_difficulty)
            if select_difficulty == goalie_choice:
                return "Save"
            else:
                return "Goal"
    return "Goal"


if __name__ == '__main__':

    # define the number of tests cases per scenario
    input_check = 1
    while input_check == 1:
        try:
            tests = int(input("Enter the number of test cases per scenario: "))
            input_check = 0
        except ValueError:
            print('\nYou did not enter a valid integer')

    # SCENARIO 1: goal keeper jumps in random direction
    # step 1: create 5 striker and 1 goalie
    print("\n\nBeginning Scenario 1 - Goalie jumps in Random Direction")
    print("-------------------------------------------------------")
    Player(name='Player A')
    Player(name='Player B')
    Player(name='Player C')
    Player(name='Player D')
    Player(name='Player E')
    Player(name='Goalie')

    # step 2: run n scenarios where each player kicks in a random direction and goalie jumps in random direction
    for match in range(tests):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        win_perc = goal_keeper.penalty_sim(kick_taker, tests, print_result=False, team=False, consider_direction=False)

    print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case1, "\nSaves: ", goal_keeper.wins_case1,
          "\nGoalkeeper Success Rate: ", win_perc,"%")
    print("Scenario 1 done\n\nStarting scenario 2 - Goalie jumps in Team's frequent kick direction")
    print("-------------------------------------------------------")

    # SCENARIO 2: goal keeper jumps in the direction of team's frequent shot direction
    (Player.keeper.wins_case1, Player.keeper.wins_case2, Player.keeper.wins_case3) = (0, 0, 0)
    (Player.keeper.losses_case1, Player.keeper.losses_case2, Player.keeper.losses_case3) = (0, 0, 0)
    (Player.keeper.count_r_total, Player.keeper.count_l_total, Player.keeper.count_m_total) = (0, 0, 0)
    Player.keeper.tendency = [0, 0, 0]
    # for match in range(tests):
    kick_taker = choice(Player.team)
    goal_keeper = Player.keeper
    #     if match < 1000:
    #         train = goal_keeper.penalty_sim(match, kick_taker, tests, print_result=False, team=True, consider_direction=True)
    #     else:
    win_perc = goal_keeper.penalty_sim(kick_taker, tests, print_result=False, team=True, consider_direction=True)
    print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case2, "\nSaves: ", goal_keeper.wins_case2,
          "\nGoalkeeper Success Rate: ", win_perc,"%")
    print("Scenario 2 done\n\nStarting scenario 3 - Goalie jumps in Player's frequent kick direction")
    print("-------------------------------------------------------")

    # SCENARIO 3: goal keeper jumps in the direction the individual players' frequent shot direction
    # clear goalie stats from case 2
    (Player.keeper.wins_case1, Player.keeper.wins_case2, Player.keeper.wins_case3) = (0, 0, 0)
    (Player.keeper.losses_case1, Player.keeper.losses_case2, Player.keeper.losses_case3) = (0, 0, 0)
    (Player.keeper.count_r_total, Player.keeper.count_l_total, Player.keeper.count_m_total) = (0, 0, 0)
    Player.keeper.tendency = [0, 0, 0]
    # for match in range(tests):
    kick_taker = choice(Player.team)
    goal_keeper = Player.keeper
    win_perc = goal_keeper.penalty_sim(kick_taker, tests, print_result=False, team=False, consider_direction=True)
    print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case3, "\nSaves: ", goal_keeper.wins_case3,
          "\nGoalkeeper Success Rate: ", win_perc,"%")
    print("Scenario 3 done")
    # ------------------------------------------------------------------------------------------------------------------

from random import choice, randint
import numpy as np
import math


class Player:
    # player_count = 0
    team = []
    keeper = None
    (team_count_r_total, team_count_l_total, team_count_m_total) = (0, 0, 0)

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
                cnt = [Player.team_count_r_total, Player.team_count_l_total, Player.team_count_m_total]
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

    def choose_direction_striker(self, consider_direction):
        if not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            if jump_dir == 'Right':
                self.tendency[0] += 1
            elif jump_dir == 'Left':
                self.tendency[1] += 1
            else:
                self.tendency[2] += 1
            return jump_dir
        else:
            n = randint(1, sum(self.tendency))
            if n <= self.tendency[0]:
                self.tendency[0] += 1
                return 'Right'
            elif n <= self.tendency[0] + self.tendency[1]:
                self.tendency[1] += 1
                return 'Left'
            else:
                self.tendency[2] += 1
                return 'Middle'

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
        if opp_dir == 'Right':
            if not team:
                opponent.count_r_total += 1
            Player.team_count_r_total += 1
        elif opp_dir == 'Left':
            if not team:
                opponent.count_l_total += 1
            Player.team_count_l_total += 1
        elif opp_dir == 'Middle':
            if not team:
                opponent.count_m_total += 1
            Player.team_count_m_total += 1


    def penalty_sim(self, striker, tests, print_result=False, team=False, consider_direction=False):
        # self = goalie, opponent = striker
        goalie_direction = self.choose_direction_goalie(team, consider_direction, striker)
        striker_direction = striker.choose_direction_striker(consider_direction)
        result=''
        if goalie_direction == striker_direction:
            result = fail_or_succeed()
            if result == "Miss" or result == "Save":
                winner = self
            else:
                winner = striker
        else:
            '''kick_angle = np.random.normal(60, 30)
            if kick_angle < 45:
                result = "Miss"
                winner = self
            else:'''
            winner = striker

        Player.record_play(self, striker, striker_direction, winner, consider_direction, team)
        if print_result:
            if result == "Miss":
                print("Player", striker.name, "missed the goal entirely. The winner is the the Goalie")
            else:
                print("Player", striker.name, "kicked to the ", striker_direction, ", goal keeper jumped to the ",
                  goalie_direction, ", the winner is ", winner.name)
        if not consider_direction:
            return (self.wins_case1 / tests) * 100
        else:
            if team:
                return (self.wins_case2 / tests) * 100
            else:
                return (self.wins_case3 / tests) * 100


# outside class Player
def fail_or_succeed():
    # generate random goalie reaction time and jump speed
    goalie_reaction_time = np.random.normal(0.02, 0.002)
    goalie_jump_speed = np.random.normal(15, 2)
    # generate random kick speed and angle
    ball_speed = np.random.normal(65, 5)
    kick_angle = np.random.normal(60, 30)
    # 0.00681818 mile = 12 yards - distance between penalty spot and goal
    # time = distance/speed
    kicking_duration = 0.00681818 / (ball_speed * math.sin(kick_angle * math.pi / 180))
    # distance = time * speed
    goalie_saving_distance = (kicking_duration - goalie_reaction_time / 3600) * goalie_jump_speed
    target_saving_distance = 0.00681818 / (math.tan(kick_angle * math.pi / 180))
    distance_diff = abs(goalie_saving_distance - target_saving_distance)
    if kick_angle < 45:
        return "Miss"
    else:
        if distance_diff > 0.0005:
            return "Goal"
        else:
            return "Save"


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
    Player(name='Team 1 - A')
    Player(name='Team 1 - B')
    Player(name='Team 1 - C')
    Player(name='Team 1 - D')
    Player(name='Team 1 - E')
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
    for match in range(tests):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        win_perc = goal_keeper.penalty_sim(kick_taker, tests, print_result=True, team=True, consider_direction=True)
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
    for match in range(tests):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        win_perc = goal_keeper.penalty_sim(kick_taker, tests, print_result=True, team=False, consider_direction=True)
    print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case3, "\nSaves: ", goal_keeper.wins_case3,
          "\nGoalkeeper Success Rate: ", win_perc,"%")
    print("Scenario 3 done")
    # ------------------------------------------------------------------------------------------------------------------

from random import choice, randint
from collections import Counter
import numpy as np
import math
import matplotlib.pyplot as plt


class Player:
    """
        The player contains two players where can be either the striker who kicks for the goal
        or goal keeper who saves the goal.
        However, this goalie can be trained to use adaptive training techniques by recording striker's kick direction
        or team's kick direction and calculates the win percentage of saving the goal
        """

    # player_count = 0
    team = []
    keeper = None
    (team_count_r_total, team_count_l_total, team_count_m_total) = (0, 0, 0)
    team_tendency = [1, 1, 1]
    team_jump_dir = []

    def __init__(self, name=None):
        """
            To check whether the player is a striker or a goal keeper
            and if it's a striker then appends to the list of players
            :param:name:Name of the player either 'striker' or 'goalie'
            :return:
        """

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
        self.jump_dir_history = []

    @staticmethod
    def choose_direction_goalie(team, consider_direction, striker):
        """
            To choose goal keeper's direction randomly from the list of direction when consider_directon is false,
            chooses from team tendency if it is team when consider_direction is true else chooses from striker's tendency
            :param team: team of strikers
            :param consider_direction: direction of the strikers either true or false
            :param striker: player who kicks the ball
            :return: jump_dir,direction: direction in which goalie should jump randomly or the direction left,right or middle
        """

        if not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            return jump_dir
        else:
            if team:
                counter = Counter(Player.team_jump_dir)
            else:
                counter = Counter(striker.jump_dir_history)
            max_count = max(counter.values())
            mode = [i for i, j in counter.items() if j == max_count]
            direction = choice(mode)
            return direction

    def choose_direction_striker(self, consider_direction):
        """To choose striker's direction randomly from the list of direction when consider_directionis false
            or based on striker's tendency when consider_direction is true
            :param self:Striker
            :param consider_direction: direction of the strikers either true or false
            :return: jump_dir,left,right,middle: direction in which goalie should jump randomly
            or the direction left,right or middle
        """

        if not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            return jump_dir
        else:
            n = randint(1, sum(self.tendency))
            if n <= self.tendency[0]:
                self.tendency[0] += 1
                jump_dir = 'Right'
            elif n <= self.tendency[0] + self.tendency[1]:
                self.tendency[1] += 1
                jump_dir = 'Left'
            else:
                self.tendency[2] += 1
                jump_dir = 'Middle'
            if len(Player.team_jump_dir) == 5:
                Player.team_jump_dir.pop(0)
            if len(self.jump_dir_history) == 5:
                self.jump_dir_history.pop(0)
            Player.team_jump_dir.append(jump_dir)
            self.jump_dir_history.append(jump_dir)
            return jump_dir

    @staticmethod
    def record_play(gk: 'Player', opponent: 'Player', opp_dir: str, winner: 'Player', consider_direction, team):
        """To record goalie's win or losses for when the goalie jumps in random direction to save the goal
            or jumps in the team's frequent direction or striker's frequent direction
            by calculating team's tendency or striker's tendency respectively
            :param gk: Player
            :param opponent: Player
            :param opp_dir: opponent's direction
            :param winner: Player who can be either striker or a goalie
            :param consider_direction: direction of strikers either true or false
            :param team: team of strikers
            :return:
        """

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

    def penalty_sim(self, match, striker, tests, print_result=False, team=False, consider_direction=False):
        """To calculate penalty simulation by considering the striker's and goalie's direction,
            when both same direction, results in goalie's win for maximum cases else striker wins
                :param self: Goalie
                :param match: n scenarios for range in tests
                :param striker: opponent player
                :param tests: number of cases for which simulation should work
                :param print_result: prints saved or missed, it's either true or false
                :param team: team of strikers, true only for team else false
                :param consider_direction: direction of strikers, either true or false
                :return: wins_case1,wins_case2,wins_case3: Goalie's win % for case 1,case 2 or case 3
        """

        # self = goalie, opponent = striker
        if team and match < 5:
            striker_direction = striker.choose_direction_striker(consider_direction)
            return 0
        goalie_direction = self.choose_direction_goalie(team, consider_direction, striker)
        striker_direction = striker.choose_direction_striker(consider_direction)
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
def fail_or_succeed(strike_dir, different, n=None, sc=None, gc = None):
    """
        :param strike_dir: Striker's direction either left right or middle
        :param different: different is just true or false where if both direction are same it is true
        or if both direction are different it is false
        :param n: an parameter added for doctest, passing 1 will return miss, passing anything else will run the next codes
        :param sc: an parameter added for doctest in order to have a SET select_difficulty value for doctest
        :param gc: an parameter added for doctest in order to have a SET goalie_difficulty value for doctest
        :return: 'Save' or 'Goal' or 'Miss'
        >>> fail_or_succeed('Left', True, 3, 1, 1)
        'Goal'
        >>> fail_or_succeed('Left', True, 1)
        'Miss'
        >>> fail_or_succeed('Left', False, 3, 2, 2)
        'Save'
        >>> fail_or_succeed('Right', True, 3, 2, 1)
        'Goal'
        >>> fail_or_succeed('Right', False, 3, 0, 0)
        'Save'
        >>> fail_or_succeed('Middle', True, 3)
        'Goal'
        >>> fail_or_succeed('Middle', False, 3, 2, 0)
        'Goal'
    """

    # create 1 out of 10 chance for player to miss the goal entirely
    if n is None:
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

            if sc is None:
                select_difficulty = choice(striker_difficulty)
            else:
                select_difficulty = sc #added for doc test
            if gc is None:
                goalie_choice = choice(goalie_difficulty)
            else:
                goalie_choice = gc #added for doc test
            if select_difficulty == goalie_choice:
                return "Save"
            else:
                return "Goal"
    return "Goal"


if __name__ == '__main__':
    # define number of runs
    input_check = 1
    while input_check == 1:
        try:
            program_run = int(input("Enter the number of times to repeat the entire program: "))
            input_check = 0
        except ValueError:
            print('\nYou did not enter a valid integer')

    # define the number of tests cases per scenario
    input_check = 1
    while input_check == 1:
        try:
            tests = int(input("Enter the number of test cases per scenario: "))
            input_check = 0
        except ValueError:
            print('\nYou did not enter a valid integer')

    final_results = [['', 'Total', 'Win', 'Percentages'], ['Run No.', 'Scenario 1', 'Scenario 2', 'Scenario 3']]
    sum_wins = ['Sum:', 0, 0, 0]

    for i in range(0, program_run):
        temp_result = [(i + 1)]
        print("Beginning Run ", (i + 1))
        # SCENARIO 1: goal keeper jumps in random direction
        # step 1: create 5 striker and 1 goalie
        print("\nBeginning Scenario 1 - Goalie jumps in Random Direction")
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
            win_perc = goal_keeper.penalty_sim(match, kick_taker, tests, print_result=False, team=False,
                                               consider_direction=False)

        print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case1, "\nSaves: ",
              goal_keeper.wins_case1,
              "\nGoalkeeper Success Rate: ", win_perc, "%")
        temp_result.append(win_perc)
        sum_wins[1] += win_perc
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
            if match < 5:
                train = goal_keeper.penalty_sim(match, kick_taker, tests, print_result=False, team=True,
                                                consider_direction=True)
            else:
                win_perc = goal_keeper.penalty_sim(match, kick_taker, tests, print_result=False, team=True,
                                                   consider_direction=True)
        print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case2, "\nSaves: ",
              goal_keeper.wins_case2,
              "\nGoalkeeper Success Rate: ", win_perc, "%")
        temp_result.append(win_perc)
        sum_wins[2] += win_perc
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
            win_perc = goal_keeper.penalty_sim(match, kick_taker, tests, print_result=False, team=False,
                                               consider_direction=True)
        print("Number of penalties: ", tests, "\nGoals: ", goal_keeper.losses_case3, "\nSaves: ",
              goal_keeper.wins_case3,
              "\nGoalkeeper Success Rate: ", win_perc, "%")
        temp_result.append(win_perc)
        sum_wins[3] += win_perc
        print("Scenario 3 done")
        print("-------------------------------------------------------\n\n")
        final_results.append(temp_result)
    final_results.append(sum_wins)

    # print()
    for i in final_results:
        print(i[0], i[1], i[2], i[3])

    # plt.xlim([0, 100])
    avg = [x / program_run for x in final_results[-1][1:]]  # get average value
    print("Avg:", avg)
    # plt.bar(win_perc, bins=3, normed=1, histtype='bar', color='blue')
    objects = ('Scenario1', 'Scenario2', 'Scenario3')

    plt.bar(objects, avg, align='center', alpha=0.5)
    # plt.yticks(y_pos, objects)

    plt.legend(loc='upper right')

    # Add labels
    plt.xlabel('Scenarios')
    plt.ylabel('Win percentage of a Goalie')
    plt.title("Plot visualizing the comparison between the all win % for all the 3 scenarios")

    plt.show()

    import doctest
    doctest.testmod()

import csv
from random import choice, randint
from collections import Counter, defaultdict


class Player:
    # player_count = 0
    team = []
    keeper = None

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
        self.tendency = [0, 0, 0]
        self.choices = Counter()

    @staticmethod
    def choose_direction_goalie(consider_direction, striker):
        if not consider_direction:
            directions = ['Right', 'Left', 'Middle']
            jump_dir = choice(directions)
            return jump_dir
        else:
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
            n = randint(1, max(self.tendency))
            if n <= self.tendency[0]:
                return 'Right'
            elif n <= self.tendency[0] + self.tendency[1]:
                return 'Left'
            else:
                return 'Middle'

    @staticmethod
    def record_play(gk: 'Player', opponent: 'Player', opp_dir: str, winner: 'Player', consider_direction):
        # record goalies wins and losses
        if winner == gk:
            if not consider_direction:
                winner.wins_case1 += 1
            else:
                winner.wins_case2 += 1
        else:
            if not consider_direction:
                winner.losses_case1 += 1
            else:
                winner.losses_case2 += 1

        # record players selected direction
        if opp_dir == 'Right':
            opponent.count_r_total += 1
        elif opp_dir == 'Left':
            opponent.count_l_total += 1
        elif opp_dir == 'Middle':
            opponent.count_m_total += 1

    def penalty_sim(self, striker, print_result=False, consider_direction=False):
        # self = goalie, opponent = striker
        goalie_direction = self.choose_direction_goalie(consider_direction, striker)
        striker_direction = striker.choose_direction_striker(consider_direction)
        if goalie_direction == striker_direction:
            winner = self
        else:
            winner = striker

        Player.record_play(self, striker, striker_direction, winner, consider_direction)
        if print_result:
            print("Player",striker.name, "kicked to the ", striker_direction, ", goal keeper jumped to the ",
                  goalie_direction, ", the winner is ", winner.name)
        if not consider_direction:
            return (self.wins_case1/100)*100
        else:
            return (self.wins_case2/100)*100


# outside class Player
def training():
    # Create a list of player details from the csv
    players = []
    (count_right_leg, count_left_leg) = ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])  # [R, L, M, R%, L%, M%]
    (r_count, l_count) = (0, 0)

    with open("penalty_data.csv") as f:
        reader = csv.reader(f)
        for a in reader:
            if '' not in a[9:12]:
                players.append([a[9], a[10]])  # foot, kick_direction

    for leg_test in range(10000):
        # select a random striker
        leg_test_striker = choice(players)

        # right foot count
        if leg_test_striker[0] == 'R':
            r_count += 1
            # shoot right/left/middle count
            if leg_test_striker[1] == 'R':
                count_right_leg[0] += 1
            elif leg_test_striker[1] == 'L':
                count_right_leg[1] += 1
            else:
                count_right_leg[2] += 1
        # left foot count
        else:
            l_count += 1
            if leg_test_striker[1] == 'R':
                count_left_leg[0] += 1
            elif leg_test_striker[1] == 'L':
                count_left_leg[1] += 1
            else:
                count_left_leg[2] += 1

        for i in range(3, 6):
            if count_right_leg[i - 3] != 0: count_right_leg[i] = (count_right_leg[i - 3] / r_count) * 100
            if count_left_leg[i - 3] != 0: count_left_leg[i] = (count_left_leg[i - 3] / l_count) * 100

    # print(count_right_leg, count_left_leg)


if __name__ == '__main__':

    # SCENARIO 1: goal keeper jumps in random direction
    # step 1: create 5 striker and 1 goalie
    Player(name='A')
    Player(name='B')
    Player(name='C')
    Player(name='D')
    Player(name='E')
    Player(name='Goalie')

    # step 2: run n scenarios where each player kicks in a random direction and goalie jumps in random direction
    for match in range(100):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        win_perc = goal_keeper.penalty_sim(kick_taker, print_result=True, consider_direction=False)
    print("Win %:", win_perc)
    print("Scenario 1 done\n\nStarting scenario 2\n\n")

    # SCENARIO 2: goal keeper jumps in the direction the opponents most frequently shoot in
    for match in range(100):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        win_perc = goal_keeper.penalty_sim(kick_taker, print_result=True, consider_direction=True)
    print("Win %:", win_perc)
    # SCENARIO 3: goal keeper considers striking foot
    # Step 1 (Pre-Monte Carlo step): Find a correlation between foot used and kick direction
    training()

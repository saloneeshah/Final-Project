import csv
from random import choice
from collections import Counter, defaultdict


class Player:
    player_count = 0
    team = []
    keeper = None

    def __init__(self, name=None):
        Player.player_count += 1
        if name != 'Goalie':
            Player.team.append(self)
        else:
            Player.keeper = self
        self.name = name
        self.wins = 0
        self.losses = 0
        self.choices = Counter()

    def choose_direction(self):
        # current code is only for scenario 1, will use self later
        directions = ['Right', 'Left', 'Middle']
        kick_dir = choice(directions)
        return kick_dir

    @staticmethod
    def record_play(gk: 'Player', gk_dir: str, opp_dir: str, winner: 'Player'):
        if winner == gk:
            winner.wins += 1
        else:
            winner.losses += 1
        # have to add logic to record goalie and player dir for next scenario

    def penalty_sim(self, striker, print_result=False):
        # self = goalie, opponent = striker
        goalie_direction = self.choose_direction()
        striker_direction = striker.choose_direction()
        if goalie_direction == striker_direction:
            winner = self
        else:
            winner = striker

        Player.record_play(self, goalie_direction, striker_direction, winner)
        if print_result:
            print("Player kicked to the ", striker_direction, ", goal keeper jumped to the ",
                  goalie_direction, ", the winner is ", winner.name)
        # return winner


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

    #print(count_right_leg, count_left_leg)


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
        goal_keeper.penalty_sim(kick_taker, print_result=True)

    # SCENARIO 2: goal keeper jumps in the direction the opponents most frequently shoot in

    # SCENARIO 3: goal keeper considers striking foot
    # Step 1 (Pre-Monte Carlo step): Find a correlation between foot used and kick direction
    training()

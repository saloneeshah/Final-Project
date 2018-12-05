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
        # Added for Case 2
        self.count_r_total = 0
        self.count_l_total = 0
        self.count_m_total = 0

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
        # Added for Case 2, Record Striker direction
        if opp_dir == 'Right':
            gk.count_r_total +=1
        elif opp_dir == 'Left':
            gk.count_l_total +=1
        elif opp_dir == 'Middle':
            gk.count_m_total +=1
        return winner
    
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
        
    # Added for Case 2, get Goalie direction
    def keeper_direction(self):
        # Compare the three directions and find the highest one
        cnt = [self.count_r_total, self.count_l_total, self.count_m_total]

        direction_index = [i for i, e in enumerate(cnt) if e == max(cnt)]
        if len(direction_index) == 1:
            if direction_index == [0]:
                direction = 'Right'
            elif direction_index == [1]:
                direction = 'Left'
            else:
                direction = 'Middle'
        # If there're more than one highest count, we randomly select the direction from the highest directions
        elif len(direction_index) == 2:
            if direction_index == [0,1]:
                directions = ['Right', 'Left']
                direction = choice(directions)
            elif direction_index == [0,2]:
                directions = ['Right', 'Middle']
                direction = choice(directions)
            elif direction_index == [1,2]:
                directions = ['Left', 'Middle']
                direction = choice(directions)
        elif len(direction) > 2:
            directions = ['Right', 'Left', 'Middle']
            direction = choice(directions)
        return direction
    
    # Added for Case 2, get Striker direction based on Case 1
    def choose_direction2(self):
        # current code is only for scenario 1, will use self later
        directions = ['Right', 'Left', 'Middle']
        total = self.count_r_total + self.count_l_total + self.count_m_total
        weights = [self.count_r_total/total, self.count_l_total/total, self.count_m_total/total]
        kick_dir = choice(directions, weights)
        return kick_dir
    
    # Added for Case 2, penalty simulation for Case 2
    def penalty_sim2(self, striker, print_result=False):
        # self = goalie, opponent = striker
        goalie_direction = self.keeper_direction()
        striker_direction = striker.choose_direction2()
        if goalie_direction == striker_direction:
            winner = self
        else:
            winner = striker

        Player.record_play(self, goalie_direction, striker_direction, winner)
        if print_result:
            print("S2: Player kicked to the ", striker_direction, ", goal keeper jumped to the ",
                  goalie_direction, ", the winner is ", winner.name)
        return winner
            

# outside class Player
def training():
    # Create a list of player details from the csv
    players = []
    (count_right_leg, count_left_leg) = ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])  # [R, L, M, R%, L%, M%]
    (r_count, l_count) = (0, 0)

    with open("penalty_data.csv", encoding="utf8", errors='ignore') as f:
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
    # Added for Case 2
    for match in range(100):
        kick_taker = choice(Player.team)
        goal_keeper = Player.keeper
        goal_keeper.penalty_sim2(kick_taker, print_result=True)
        
    # SCENARIO 3: goal keeper considers striking foot
    # Step 1 (Pre-Monte Carlo step): Find a correlation between foot used and kick direction
    training()

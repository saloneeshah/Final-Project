#The program calculates the probabiliy that the goalie actually save the ball when he/she gets the direction right
#the variables and threshold are subject to change
#We can multiply the result(the percentage) to the percentage of the three scenarios

import numpy as np
import math

goalie_reaction_time = np.random.normal(0.02, 0.002, 5)  # assume the average reaction time is 0.02 second
goalie_jump_speed = np.random.normal(15, 2)  # assume the average jump speed for goalie is 15 miles per hour
ball_speed = np.random.normal(80, 5)  # assume the average speed is 80 miles per hour
kick_angle = np.random.normal(25, 5)  # assume the angle will be 20°-30°(this is said to be an ideal angle)


def fail_or_succeed(goalie_reaction_time, ball_speed, kick_angle):
    goalie_reaction_time = np.random.normal(0.02, 0.002)  # assume the average reaction time is 0.02 second
    goalie_jump_speed = np.random.normal(15, 2)  # assume the average jump speed for goalie is 15 miles per hour
    ball_speed = np.random.normal(65, 5)  # assume the average speed is 80 miles per hour
    kick_angle = np.random.normal(60, 30)  # assume the angle will be 0° - 60°, so the comlimentary angle is 30° - 90°,
    # we are using the complimentary angle to calculate the following sin/tan calculation
    kicking_duration = 0.00681818 / (ball_speed * math.sin(
        kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards, which is the distance from kicking point to center goal
    goalie_saving_distance = (kicking_duration - goalie_reaction_time / 3600) * goalie_jump_speed
    target_saving_distance = 0.00681818 / (math.tan(kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards
    distance_diff = abs(goalie_saving_distance - target_saving_distance)

    # print("kicking_duration is:", kicking_duration)
    # print("goalie_saving_distance_is: ", goalie_saving_distance)
    # print("target_saving_distance_is:", target_saving_distance)
    # print("the distance_diff is:", distance_diff)
    if distance_diff > 0.0015: #0.0015 mile = 2.64 yard #subject to change
    #  assume if the distance difference is larger than a given value, then the goalie cannot save the ball
        return "Goalie Fail"
    else:
        return "Goalie Win"

answer = []
for i in range (1,10001):
    temp = fail_or_succeed(goalie_reaction_time, ball_speed, kick_angle)
    answer.append(temp)

count_win_percentage = answer.count("Goalie Win")/len(answer)
print(count_win_percentage)

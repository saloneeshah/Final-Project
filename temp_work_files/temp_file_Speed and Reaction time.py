#The program calculates the probabiliy that the goalie actually save the ball when he/she gets the direction right
#the variables and threshold are subject to change

import numpy as np
import math

def fail_or_succeed(goalie_reaction_time, ball_speed, kick_angle):
    goalie_reaction_time = np.random.normal(0.02, 0.002)  # assume the average reaction time is 0.02 second
    goalie_jump_speed = np.random.normal(15, 2)  # assume the average jump speed for goalie is 15 miles per hour
    ball_speed = np.random.normal(65, 5)  # assume the average speed is 65 miles per hour
    kick_angle = np.random.normal(60, 30)  # assume the angle will be 0° - 60°, so the comlimentary angle is 30° - 90°,
    # we are using the complimentary angle to calculate the following sin/tan calculation
    kicking_duration = 0.00681818 / (ball_speed * math.sin(
        kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards, which is the distance from kicking point to center goal
    goalie_saving_distance = (kicking_duration - goalie_reaction_time / 3600) * goalie_jump_speed
    target_saving_distance = 0.00681818 / (math.tan(kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards
    distance_diff = abs(goalie_saving_distance - target_saving_distance)
    if kick_angle < 45: #when the complimentary angle < 45°, which is equal to when the actual kick angle is > 45°, the striker kicks to outside the goalpost
        return "Goalie Win"
    else:
        if distance_diff > 0.0005: #0.0005 mile = 0.88 yard #subject to change
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

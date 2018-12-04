import numpy as np
import math

goalie_reaction_time = np.random.normal(0.02, 0.002)  # assume the average reaction time is 0.02 second
goalie_jump_speed = np.random.normal(15, 2)  # assume the average jump speed for goalie is 15 miles per hour
ball_speed = np.random.normal(65, 5)  # assume the average speed is 80 miles per hour
print(goalie_reaction_time)
print(goalie_jump_speed)
print(ball_speed)


def fail_or_succeed(goalie_reaction_time, ball_speed, kick_angle):
    kicking_duration = 0.00681818 / (ball_speed * math.sin(
        kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards, which is the distance from kicking point to center goal
    goalie_saving_distance = (kicking_duration - goalie_reaction_time / 3600) * goalie_jump_speed
    target_saving_distance = 0.00681818 / (math.tan(kick_angle * math.pi / 180))  # 0.00681818 mile = 12 yards
    distance_diff = abs(goalie_saving_distance - target_saving_distance)

    print("kicking_duration is:", kicking_duration)
    print("goalie_saving_distance_is: ", goalie_saving_distance)
    print("target_saving_distance_is:", target_saving_distance)
    print("the distance_diff is:", distance_diff)
    if distance_diff > 0.011:  # assume if the distance difference is larger than xx, then the goalie cannot save the ball
        return "Goalie Fail"
    else:
        return "Goalie Win"


fail_or_succeed(goalie_reaction_time, ball_speed, 25)  # assume the angle is 25° right now

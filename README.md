# 590PR Final_Project

# Title: Goalkeeper Success Rate Simulation

## Team Member(s): Claire Wu|Salonee Shah|Samuel John

# Monte Carlo Simulation Scenario & Purpose:
The program would simulate the success percentage of a goalkeeper and the purpose would be checking if using different strategies can improve the success percentage or not.  

The simulation conditions we are considering are: 

•	Goalie jumps in a random direction for each opponent over a set number of runs 

•	Goalie jumps in the direction of the opponent team's most frequently kicking direction for a set number of runs

•	Goalie jumps in the direction of each opponent's most frequently kicking direction for a set number of runs

Assumptions we are using are as follows:

•	Striker has 3 kicking directions and Goalie has 3 saving directions

•	If goalie's direction is not the same as striker's direction, the goalie fails and the striker wins

•	There is a saving tendency based on the area the ball hits, we have divided the whole area into 18 sub-areas and there are 6 areas for each direction. For each area the saving difficulty varies from 0, 1, 2 based on the possibility for the goalie to save the ball in that area

•	Striker’s kicking direction will not be changed based on Goalie's behavior(In Scenario 2&3, If Goalie found a team’s or a player’s frequent direction, and always save the ball in that direction, striker’s kick will not be affected or changed)

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

Variable 1：striker's kicking direction

Variable 2: goalie's saving direction

Variable 3: striker kicking area

Variable 4: goalie saving difficulty 

The range of both kicking direction and saving direction is either left, middle and right 

The Goalie's saving difficulty and the striker kicking area is as below: 
![Alt text](http://funkyimg.com/i/2Pcoj.png)

## Hypothesis or hypotheses before running the simulation:
Saving the ball based on team’s most frequent kicking direction/each striker’s most frequent kicking direction can increase the success percentage of a goalie

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
In the beginning, we have set the second scenario as considering player's frequent kicking direction and the third scenario as considering player's foot uses and kicking direction; However, we realized that it doesn't make a lot of sense to consider which foot the player uses, because most players will do the penalty strike with their dominant leg. Thus, we added the team's frequent kicking direction to our program. 

Also, in our early versions, we didn't consider the chance that the striker totally misses the goal, and we assumed every time when the goalie goes to the same direction as the striker, the goalie will win -- which is not accurate. Thus, we added the chances that the striker may miss the goal completely and added tendency to evaluate goalie's difficulty in saving the ball 
 
Based on a sample of 20 runs, we have the following findings:

Conclusion 1: 
There is an increase of 0.73 % if the goalie knows the team's last 5 directions compared to the goalie choosing random directions.

Conclusion 2:
There is an increase of  9.36 % if the goalie knows the player's last 5 directions compared to the goalie choosing random directions.


## Instructions on how to use the program:
Please download and run the code

## All Sources Used:
https://en.wikipedia.org/wiki/Penalty_shot

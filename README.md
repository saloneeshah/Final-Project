# 590PR Final_Project

# Title: Goalkeeper Success Rate Simulation

## Team Member(s): Claire Wu|Salonee Shah|Samuel John

# Monte Carlo Simulation Scenario & Purpose:
The program would simulate the success percentage of a goalkeeper and the purpose would be checking if using different strategies can improve the success percentage or not.  

The simulation conditions we are considering are: 

•	Goalie jumps in a random direction for each opponent over a set number of runs 

•	Goalie jumps in the direction of the opponent team's most frequently kicking direction for a set number of runs

•	Goalie jumps in the direction of each oppenent's most frequently kicking direction for a set number of runs

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

The range of both kicking direction and saving directoin is either left, middle and right 
The striker kicking area is as below: 
![Optional Text](../Final-Project/temp_work_files/Goalie Save Tendency Areas.png)

## Hypothesis or hypotheses before running the simulation:
Saving the ball based on team’s most frequent kicking direction/each striker’s most frequent kicking direction can increase the success percentage of a goalie

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
In the beginning, we assumed 3 kicking directions based on a dataset and we got very high results for scenerio 2&3. To make it more realistic-meaningful and yield more accurate results, we adjusted the assumption for striker kick direction from 3 directions to 9 directions. 
Result TO BE ADDED

## Instructions on how to use the program:
Download and run the code.

## All Sources Used:
https://en.wikipedia.org/wiki/Penalty_shot

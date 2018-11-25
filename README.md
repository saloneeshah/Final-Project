# 590PR Final_Project

# Title: Goalkeeper Success Rate Simulation

## Team Member(s): Claire Wu|Salonee Shah|Samuel John

# Monte Carlo Simulation Scenario & Purpose:
The program would simulate the success percentage of a goalkeeper and the purpose would be checking if using different strategies can improve the success percentage or not.  
The game would be simulated based on various methods while using a penalty dataset here: https://www.kaggle.com/apopov41/exploring-penalty-kick-variables/data

Each kick simulated would be a random row picked from the dataset and the direction of kick and leg used would be used in the program. The simulation conditions we are considering are: 
•	Goalie jumps in a random direction for each opponent over a set number of runs 
•	Goalie jumps in the direction the opponents most frequently shoot in for a set number of runs 
•	Goalie considers the opponents' shot direction as well as the foot used for the shot (data obtained from the previous scenario) to determine which direction to jump in a set number of runs

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

• Variable 1：kick_dir - this variable stands for the direction a striker kicks
The range of the kicking direction is either left, middle or right. 


• Variable 2: leg_test_striker - this variable stands for a list of a striker's foot used and kicking direction
The range of this variable is either [left, left], [left, middle], [left, right], [right, left], [right, middle] or [right, right].

As the range of the variable is based on real dataset, we believe it's a good representation of reality. We'd assume a normal distribution(to be added)

## Hypothesis or hypotheses before running the simulation:
• If goalie's direction is the same as striker's direction, then the goalie wins

• Strategic moves can increase the success percentage of a goalie

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
To be added later when the code is finalized

## Instructions on how to use the program:
First download the dataset, then download and run the code.

## All Sources Used:
https://www.kaggle.com/apopov41/exploring-penalty-kick-variables/data

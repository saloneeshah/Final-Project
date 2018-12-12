import numpy as np
import matplotlib.pyplot as plt

plt.xlim([0, 100])
    plt.hist(win_perc, bins=3, normed=1, histtype='bar', color='blue')

    plt.legend(loc='upper right')

    # Add labels
    plt.xlabel('Scenarios')
    plt.ylabel('Win percentage of a Goalie')
    plt.title("Plot visualizing the comparison between the all win % for all the 3 scenarios")

    plt.show()

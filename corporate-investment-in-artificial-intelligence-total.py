# In this problem you are going to produce a plot for annual global corporate investments on artificial 
#intelligence. Use the data given in “corporate-investment-in-artificial-intelligence-total.csv” file.
#While producing this graph be careful about the following points.
#• Format y-tick labels as shown
#• Locate y-tick labels separated by 20billion
#• Remove spines (left,right,top)
#• Use grid lines for y-axis


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Load csv file into x, y co-ordinates
investment = pd.read_csv('corporate-investment-in-artificial-intelligence-total.csv', delimiter=',')
# Create plot
fig, ax = plt.subplots()
x = investment['Year']
y = investment['total_corporate_investment_inflation_adjusted']
ax.plot(x, y, marker="*", markersize=8, color='blue')

# Set the y-tick labels to be separated by 20 billion dollars
y_ticks = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180]) * 1e9
y_ticklabels = ['$' + str(int(tick/1e9)) + ' billion' for tick in y_ticks]
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticklabels)

# Remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add grid lines for y-axis
ax.yaxis.grid(linestyle='--')

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Global Corporate Investments (in billions)')
ax.set_title('Annual Global Corporate Investments')

# Display plot
plt.show()
#You are given “annual-number-of-births-by-world-region.csv" file which contains yearly number of 
#births for each contry and region. Using this file reproduce the figure given below. Produce a 
#stackplot for the following regions.
#Africa (UN)
#Asia (UN)
#Europe (UN)
#Latin America and the Caribbean (UN)
#Northern America (UN)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('annual-number-of-births-by-world-region.csv')

europe = df[df['Entity'] == 'Europe (UN)']
asia = df[df['Entity'] == 'Asia (UN)']
north_america = df[df['Entity'] == 'Northern America (UN)']
latin_america = df[df['Entity'] == 'Latin America and the Caribbean (UN)']
africa = df[df['Entity'] == 'Africa (UN)']

years = europe['Year']
births_europe = europe['Births - Sex: all - Age: all - Variant: estimates']
births_asia = asia['Births - Sex: all - Age: all - Variant: estimates']
births_north_america = north_america['Births - Sex: all - Age: all - Variant: estimates']
births_latin_america = latin_america['Births - Sex: all - Age: all - Variant: estimates']
births_africa = africa['Births - Sex: all - Age: all - Variant: estimates']

colors = ['blue', 'orange', 'green', 'red', 'purple']
labels = ['Asia (UN) ', 'Africa (UN)', 'Latin America and the Caribbean (UN)', 'Europe (UN)', 'Northern America (UN)']

plt.stackplot(years, births_asia, births_africa, births_latin_america, births_europe, births_north_america,
              labels=labels, colors=colors)
# Set the y-tick labels to be separated by 20 million
y_ticks = np.array([0, 20, 40, 60, 80, 100, 120, 140]) * 1e8
y_ticklabels = [str(int(tick/1e8)) + ' million' for tick in y_ticks]
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticklabels)

plt.xlabel('Year')
plt.ylabel('Births (millions)')
plt.title('Annual number of births by world region')
plt.legend(loc='upper right')
plt.show()

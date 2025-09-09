import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#-----------------------------------------------------------------------
penguins = sns.load_dataset('penguins')
penguins_grouped = penguins[['species', 'bill_length_mm']].groupby('species').mean().reset_index()

flights = sns.load_dataset('flights')
flights_grouped = flights[['year', 'passengers']].astype({'year':'string'}).groupby('year').sum().reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(penguins_grouped['species'], penguins_grouped['bill_length_mm'])
ax1.set_title('Avarage penguin bill length by species')
ax1.set_xlabel('Species')
ax1.set_ylabel('Bill length (mm)')

ax2.plot(flights_grouped['year'], flights_grouped['passengers'])
ax2.set_title('Total number of passengers by year')
ax2.set_xlabel('Year')
ax2.set_ylabel('Passengers')


titanic = sns.load_dataset('titanic')
car_crashes = sns.load_dataset('car_crashes')
fmri = sns.load_dataset('fmri')
diamonds = sns.load_dataset('diamonds')

plt.tight_layout()
plt.show()
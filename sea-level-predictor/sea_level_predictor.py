import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    sea_level = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(sea_level['Year'], sea_level['CSIRO Adjusted Sea Level'], s=5)

    # Create first line of best fit
    line_1 = linregress(sea_level['Year'],
                        sea_level['CSIRO Adjusted Sea Level'])
    x_1 = np.arange(1880, 2051, 1)
    y_1 = line_1.slope * x_1 + line_1.intercept
    plt.plot(x_1, y_1, 'r')

    # Create second line of best fit
    recent_sea_level = sea_level[sea_level['Year'] >= 2000]
    line_2 = linregress(recent_sea_level['Year'],
                        recent_sea_level['CSIRO Adjusted Sea Level'])
    x_2 = np.arange(2000, 2051, 1)
    y_2 = line_2.slope * x_2 + line_2.intercept
    plt.plot(x_2, y_2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

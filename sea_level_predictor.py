import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', parse_dates=True, index_col=[0])

    # Create scatter plot
    x = time = df.reset_index()['Year'].dt.year
    x_2050 = pd.DataFrame(np.arange(2014,2051), columns=['Year'])
    x_for = pd.concat([x,x_2050]).reset_index().drop(columns='index')
    y = df.iloc[:,0]
    fig, ax = plt.subplots()
    ax.scatter(x, y)    

    # Create first line of best fit
    regr1 = linregress(x, y)
    m1, c1 = (regr1.slope, regr1.intercept)
    ax.plot(x_for, m1*x_for+c1, color='yellow', label='line1')

    # Create second line of best fit
    x_rec = (x[-14:].reset_index(drop=True))#['Year']
    y_rec = (y[-14:])
    regr2 = linregress(x_rec, y_rec)
    m2, c2 = (regr2.slope, regr2.intercept)
    x_for2 = pd.concat([x_rec,x_2050]).reset_index().drop(columns='index')['Year']
    ax.plot(x_for2, m2*x_for2+c2, color='green', label='line2')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

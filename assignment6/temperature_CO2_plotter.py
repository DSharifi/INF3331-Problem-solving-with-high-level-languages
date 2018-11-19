import pandas as pd
import numpy as np
import argparse
import os
import matplotlib.pyplot as plt


co2_by_country = pd.read_csv('dataset\CO2_by_country.csv', sep=',' )
co2 = pd.read_csv('dataset\co2.csv', sep=',')
temp = pd.read_csv('dataset\\temperature.csv', sep=',')

# Can give a false positive by default, as adressed here:
# http://pandas-docs.github.io/pandas-docs-travis/#returning-a-view-versus-a-copy
pd.options.mode.chained_assignment = None

def plot_temperature(month, year_start, year_end, y_min, y_max):
    """plots temperatue for a month over range of years
    
    Arguments:
        month {str} -- name of month
        month2 {str} -- name of other month

        year_start {int} -- starting year
        year_end {int} -- end year

        y_min {float} -- y-axis minimum
        y_max {float} -- y-axis maximum
    
    Returns:
        pyplot -- plot of the temperature, according to input arguments.
    """

    temp_month = temp[["Year", month]]
    temp_month = temp_month[(temp_month['Year'] >= year_start) &
                            (temp_month['Year'] <= year_end)]

    plt.close()
    
    ax = temp_month.plot(y = month, x = 'Year')
    ax.set(xlabel="Year", ylabel="Temperature (C)")

    plt.ylim(y_min, y_max)

    return plt    


def plot_CO2(year_start, year_end, y_min, y_max):
    """plots CO2 levels over a range of years
    
    Arguments:
        year_start {int} -- starting year
        year_end {int} -- end year

        y_min {float} -- y-axis minimum
        y_max {float} -- y-axis maximum
    
    Returns:
        pyplot -- plot of the CO2 levels, according to input arguments.
    """

    co2_plot = co2[(co2['Year'] >= year_start) &
                     (co2['Year'] <= year_end)]
    plt.close()
    
    #change date to year
    co2_plot['Year'] = pd.to_datetime(
        co2_plot['Year'].astype(str), format="%Y")


    ax = co2_plot.plot(y='Carbon', x='Year', title="Increase of carbon levels")
    ax.set(xlabel="Year", ylabel="CO2 Level")
    plt.ylim(y_min, y_max)
    

    return plt


def plot_CO2_by_Country(lower_threshold, upper_threshold, year):
    """Plots every country between given threshold on a bar chart
    
    Arguments:
        lower_threshold {float} -- lower threshold
        upper_threshold {float} -- upper threshold
        year {int} -- year to check for average CO2 emmission
    
    Returns:
        pyplot -- plot of every country inbetween the threshold.
    """
    plt.close()
    year_str = str(year)

    countries = co2_by_country[["Country Code", year_str]]
    
    # parse strings to numbers
    countries.loc[year_str] = pd.to_numeric(countries[year_str])

    countries = countries[(countries[year_str] >= lower_threshold) &
    (countries[year_str] <= upper_threshold)]
        
    ax = countries.plot.bar(x="Country Code", label='Normal', title="Emissions in {}:".format(year_str))
    ax.set(xlabel="Country code", ylabel="Emission per capita")

    # adjust the plot, so the axis labels are visible
    plt.gcf().subplots_adjust(bottom=0.15)

    return plt

# def is_file(filename):
#     """Checks if a path is an actual directory"""
#     if not os.path.isfile(filename):
#         msg = "{0} is not a directory".format(filename)
#         raise argparse.ArgumentTypeError(msg)
#     else:
#         return filename


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description='Plots time vs. CO2, time vs. temperature, or CO2 levels by countries')
 
#     parser.add_argument('time', help='''A csv file of time''')
#     parser.add_argument('compare_val', help='''A csv file of either CO2 levels or temperature''')

#     args = parser.parse_args()

#     is_file(args.time)

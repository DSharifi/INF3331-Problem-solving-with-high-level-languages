import pandas as pd
import numpy as np
import argparse
import os





def plot(time_file, compare_file, compare_t):
    co2_by_country = pd.read_csv('CO2_by_country.csv')
    co2 = pd.read_csv('co2.csv')
    temp = pd.read_csv('temperature.csv')

    print (temp)





def is_file(filename):
    """Checks if a path is an actual directory"""
    if not os.path.isfile(filename):
        msg = "{0} is not a directory".format(filename)
        raise argparse.ArgumentTypeError(msg)
    else:
        return filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Plots time vs. CO2 or time vs. temperature')
 
    parser.add_argument('time', help='''A csv file of time''')
    parser.add_argument('compare_val', help='''A csv file of either CO2 levels or temperature''')

    args = parser.parse_args()

    is_file(args.time)

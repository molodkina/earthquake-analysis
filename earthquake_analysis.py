import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import argparse
from earthquake_analysis_functions import *

parser = argparse.ArgumentParser(description='Earthquake Analysis')
parser.add_argument('file_path', type=str, help='Path to the earthquake data CSV file')
args = parser.parse_args()
file_path = args.file_path

eq_data = read_data(file_path)
eq_filtered_data = filter_alaska(eq_data)
split_place(eq_filtered_data)

most_eq = get_most_earthquakes(eq_filtered_data, 1)
print("\nCountry/territory with the most earthquakes in the last 30 days:\n", most_eq)

top_magnitudes = get_top_magnitudes(eq_filtered_data, 3)
print("\nTop three locations with the highest magnitude earthquakes in the last 30 days, sorted by timestamp:\n", top_magnitudes)

riskiest_locations = calculate_risk_metric(eq_filtered_data, 3)
print("\nThree countries/territories that would be the highest risk to insure EQ within:\n", riskiest_locations)
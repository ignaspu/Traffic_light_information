import pandas

data = pandas.read_csv('data.csv')

# 1. Find the number of red, yellow & green occurrences.
red_numbers = data.Red.sum()
yellow_numbers = data.Yellow.sum()
green_numbers = data.Green.sum()
print(f"Red: {red_numbers}, yellow: {yellow_numbers}, green: {green_numbers}")
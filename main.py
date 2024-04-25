import pandas

data = pandas.read_csv('data.csv')

# 1. Find the number of red, yellow & green occurrences.
red_numbers = data.Red.sum()
yellow_numbers = data.Yellow.sum()
green_numbers = data.Green.sum()
print("Numbers of each colors occurrences:")
print(f"Red: {red_numbers}, yellow: {yellow_numbers}, green: {green_numbers}\n")

# 2. Find how long each colour was active for.
active = data[["Red", "Yellow", "Green"]].multiply(data.TimeActive, 0).sum()
print(f"Each color was active for:")
for color, time in active.items():
    print(f"{color}={time} seconds")


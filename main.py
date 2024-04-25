import pandas

data = pandas.read_csv('data.csv')

# 1. Find the number of red, yellow & green occurrences.
red_numbers = data.Red.sum()  # sudeda visas raudonas spalvas
yellow_numbers = data.Yellow.sum()  # sudeda visas geltonas spalvas
green_numbers = data.Green.sum()  # sudeda visas žalias spalvas
print("Numbers of each colors occurrences:")
print(f"Red: {red_numbers}, yellow: {yellow_numbers}, green: {green_numbers}\n")

# 2. Find how long each colour was active for.
active = data[["Red", "Yellow", "Green"]].multiply(data.TimeActive, 0).sum()  # pasirenka iš duomenų kiekvienos spalvos
# reikšmę (1) ir padaugina iš esamo laiko ir sudeda.
print("Each color was active for:")
for color, time in active.items():
    print(f"{color}={time} seconds")

# 3. Find all times when Green was active (by time)
green_active_time = data[data.Green == 1].Time.tolist()  # kai degė žalia, parenka tuos laikus ir prideda į list'ą
print("Green was active in these times:")
for each in green_active_time:  # sukasi ciklas per visą list'ą ir išspausdina kiekvieną reikšmę
    print(each)

# 4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
cycles = (
    (data.Red == 1) &  # sąlyga patikrina ar dabartinėje eilutėje dega raudona
    (data.Yellow.shift(-1) == 1) &  # ar antroje eilutėje dega geltona
    (data.Green.shift(-2) == 1) &
    (data.Yellow.shift(-3) == 1) &
    (data.Red.shift(-4) == 1)
).sum()  # susumuoja sąlygas atitinkančius variantus
print(f"Number of complete cycles: {cycles}\n")

# 5. Find number of lines with mistakes (multiple colours active at the same time or no colours active)
mistakes = ((data.Red + data.Yellow + data.Green) != 1).sum()  # sudedamos eilutės kiekvienos spalvos reikšmės
# (pvz.: 1,0,1 arba 1,0,0) ir jeigu suma yra nelygi 1 - fiksuojama klaida.
print(f"Number of lines with mistakes: {mistakes}")

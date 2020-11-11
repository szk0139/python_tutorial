#print("Hello, world!")
#Read the data file

data = []

f1 = "data/wxobs20170821.txt"
with open(f1, 'r') as df:
    for _ in range(3):
        df.readline()

    for line in df:
        datum = line.split()
        data.append(datum)


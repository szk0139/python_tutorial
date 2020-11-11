# Read the data file
f1 = "data/wxobs20170821.txt"
df = open(f1, 'r')

data = df.read()

df.close()

# DEBUG
print(data)
print('data')

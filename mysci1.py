#print("Hello, world!")
#Read the data file
f1 = "data/wxobs20170821.txt"
df1 = open(f1, 'r')
data = df1.read()
df1.close()
#DEBUG
print(type(data))


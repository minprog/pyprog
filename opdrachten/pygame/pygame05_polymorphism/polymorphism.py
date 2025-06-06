
data = [1, 2, "one", "two"]
for index in range(len(data)):
    data[index] += data[index]
print(data) # [2, 4, 'oneone', 'twotwo']

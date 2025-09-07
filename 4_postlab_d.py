list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
freq = {}
for item in list:
    freq[item] = freq.get(item, 0) + 1
print(freq)
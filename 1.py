dict = {}
arr = []
c = 0
with open("data/1-data.txt") as file:
    data = file.read()
    for line in data.split('\n'):
        if line.strip():
          arr.append(line)
        else:
          dict[c] = sum(int(i) for i in arr)
          arr.clear()
          c += 1

print(max(dict.values()))
print(sum(sorted(dict.values())[-3:]))





           







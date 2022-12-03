sum1 = 0
sum2 = 0
rucksacks = []
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("data/3-data.txt") as file:
  data = file.read()
  for line in data.split('\n'):
    rucksacks.append(line)

  # task 1
  for sack in rucksacks:
    first_half = sack[:len(sack)//2]
    second_half = sack[len(sack)//2:]
    for item in first_half:
      if item in second_half:
        sum2 += chars.index(item) + 1
        break

  print(sum2)

  # task 2
  for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    for item in group[0]:
      if item in group[1] and item in group[2]:
        sum1 += chars.index(item) + 1
        break
  print(sum1)









  

  







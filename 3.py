sum_1 = 0
sum_2 = 0
data = []
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('data/3.txt') as file:
  for line in file:
    data.append(line)

  # task 1: find sum of priorities for the common element in both halves of each rucksack
  for rucksack in data:
    half = len(rucksack) // 2
    for item in rucksack[:half]:
      if item in rucksack[half:]:
        sum_1 += priorities.index(item) + 1
        break

  # task 2: find sum of priorities for the common element in groups of there rucksacks 
  for i in range(0, len(data), 3):
    group = data[i:i+3]
    for item in group[0]:
      if item in group[1] and item in group[2]:
        sum_2 += priorities.index(item) + 1
        break


  print('Task 1:', sum_1)
  print('Task 2:', sum_2)









  

  







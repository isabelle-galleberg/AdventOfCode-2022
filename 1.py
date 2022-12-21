elves = []
calories = 0

with open("data/1.txt") as file:
  for line in file:
      # line not empty
      if line.strip():
        calories += int(line)
      else:
        elves.append(calories)
        calories = 0


print("Task 1:", max(elves))
print("Task 2:", sum(sorted(elves)[-3:]))





           







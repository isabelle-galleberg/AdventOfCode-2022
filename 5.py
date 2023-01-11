tmpStore = []
stacks_1 = []
stacks_2 = []

with open('data/5.txt') as file:
  for line in file:
    # get number of stacks from file
    if line[1] == '1':
      numCrates = int(line.split()[-1])
      for stack in range(numCrates):
        stacks_1.append([])
        stacks_2.append([])

      # each stack is a list with crates
      for elem in tmpStore:
        for stack in range(1, len(elem), 4):
          if elem[stack].strip():
            stacks_1[stack//4].append(elem[stack])
            stacks_2[stack//4].append(elem[stack])
      break

    else:
      # temporary storage for the stacks read from file 
      tmpStore.append(line.replace("\n", ""))

  # move crates according to instructions
  for line in file:
    if line.strip():
      line = line.split()
      numCrates = int(line[1])
      fromStack = int(line[3]) - 1
      toStack = int(line[5]) - 1

      # task 1
      for stack in range(numCrates):
        crate = stacks_1[fromStack].pop(0)
        stacks_1[toStack].insert(0, crate)

      # task 2
      stacks_2[toStack] = stacks_2[fromStack][:numCrates] + stacks_2[toStack]
      stacks_2[fromStack] = stacks_2[fromStack][numCrates:]

  task1 = ""
  task2 = ""
  for stack in zip(stacks_1, stacks_2):
    task1 += stack[0][0]
    task2 += stack[1][0]
  print('Task 1:', task1)
  print('Task 2:', task2)

      

    

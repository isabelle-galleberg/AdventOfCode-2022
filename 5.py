tmpStore = []
stacks = []

with open('data/5.txt') as file:
  for line in file:
    # get number of stacks from file
    if line[1] == '1':
      numStacks = int(line.split()[-1])
      for stack in range(numStacks):
        stacks.append([])

      # each stack is a list with crates
      for elem in tmpStore:
        for stack in range(1, len(elem), 4):
          if elem[stack].strip():
            stacks[stack//4].append(elem[stack])
      break

    else:
      # temporary storage for the stacks read from file 
      tmpStore.append(line.replace("\n", ""))

  # move crates according to instructions
  for line in file:
    if line.strip():
      line = line.split()
      numStacks = int(line[1])
      fromStack = stacks[int(line[3]) - 1]
      toStack = stacks[int(line[5]) - 1]

      for stack in range(numStacks):
        crate = fromStack.pop(0)
        toStack.insert(0, crate)

  print('Task 1:')
  for stack in stacks:
    print(stack[0])

      

    

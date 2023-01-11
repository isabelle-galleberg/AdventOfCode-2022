class Directory:
  def __init__(self, name):
    self.name = name
    self.size = 0
    self.children = {}
    self.parent = None

class File:
  def __init__(self, name):
    self.name = name
    self.size = 0

root = Directory("root")
currentDir = root

with open("data/7.txt") as file:
  for command in file:
    if command[0:4] == "$ cd":
      if command[5:7] == "..":
        # moves current directory out one level 
        if currentDir.parent:
          currentDir = currentDir.parent
      else:
        # adds directory to file system 
        dir = command[5:].strip()
        currentDir.children[dir] = Directory(dir)
        currentDir.children[dir].parent = currentDir
        # moves current directory in one level 
        currentDir = currentDir.children[dir]
    elif command[0:3] == "dir":
      # creates new directory
      currentDir.children[command[4:].strip()] = Directory(command[4:].strip())
    elif command[0].isnumeric():
      # add file size to current directory and all parent directories
      currentDir.size += int(command.split(" ")[0])
      parent = currentDir.parent
      while parent:
        parent.size += int(command.split(" ")[0])
        parent = parent.parent


def sum_directories_under_threshold(rootDir, threshold):
    sum = 0
    for childDir in rootDir.children.values():
        sum += sum_directories_under_threshold(childDir, threshold)
    if rootDir.size < threshold:
        return sum + rootDir.size
    return sum
 
print('Task 1:', sum_directories_under_threshold(root, 100000))




# prints the three as a graph 
def print_tree(rootDir, level):
    print('\t' * level, end='')
    
    if isinstance(rootDir, File):
        print(rootDir.name, f"(file, size={rootDir.size})")
        return
    print(rootDir.name, f'(dir, size={rootDir.size})')
    for child in rootDir.children.values():
        print_tree(child, level + 1)

print_tree(root, 0)



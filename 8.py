forest = []
visibleTrees = 0
maxScore = 0

def getViewingDistance(trees, currTree):
  score = 0
  if len(trees) > 0:
    for x in trees:
      if x < currTree:
        score += 1
      else: 
        score +=  1
        break
  return score


with open('data/8.txt') as file:
  for line in file:
    line = [int(x) for x in str(line.strip())]
    forest.append(line)

# ignore edge trees as they will not have the highest scenic score (* 0)
for i in range(1, len(forest)-1):
  for j in range(1, len(forest[i])-1):
    tree = forest[i][j]
    col = [row[j] for row in forest]
    # reverse list of left and up trees to get neighbors
    left= forest[i][:j][::-1]
    right = forest[i][j+1:]
    up = col[:i][::-1]
    down = col[i+1:]
    shortestTree = min(max(left), max(right), max(up), max(down))
    # check if tree is visible 
    if tree >  shortestTree:
      visibleTrees += 1

    # calculate scenic score
    scenicScore = getViewingDistance(left, tree) * getViewingDistance(right, tree) * getViewingDistance(up, tree) * getViewingDistance(down, tree)
    if scenicScore > maxScore:
      maxScore = scenicScore

edgeTrees= 2 * len(forest) + 2 * len(forest[0]) - 4
visibleTrees += edgeTrees

print('Task 1:', visibleTrees)
print('Task 2:', maxScore)

  
    



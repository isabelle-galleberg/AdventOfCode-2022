score_1 = 0
score_2 = 0

shape = {'X': 1, 'Y': 2, 'Z': 3}

# Task 1: X: rock, Y: paper, Z: scissors
points_1 = {
  'A': {'X': 3, 'Y': 6, 'Z': 0},
  'B': {'X': 0, 'Y': 3, 'Z': 6},
  'C': {'X': 6, 'Y': 0, 'Z': 3}
}

# Task 2: X: loose, Y: draw, Z: win
points_2 = {
  'X': 0,
  'Y': 3,
  'Z': 6, 
  'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
  'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
  'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
}

with open('data/2.txt') as file:
  for line in file:
    score_1 += shape[line[2]] + points_1[line[0]][line[2]]
    score_2 += points_2[line[2]] + shape[points_2[line[0]][line[2]]]
 
print('Task 1:', score_1)
print('Task 2', score_2)



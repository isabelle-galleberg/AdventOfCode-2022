sum_1 = 0
sum_2 = 0

with open('data/4.txt') as file:
  for line in file:
    pairs = line.split(',')
    # intervals: [a-b] and [c-d]
    a = int(pairs[0].split('-')[0])
    b = int(pairs[0].split('-')[1])
    c = int(pairs[1].split('-')[0])
    d = int(pairs[1].split('-')[1])

    # task 1: one range fully contains the other
    if a <= c and b >= d or c <= a and d >= b:
      sum_1 += 1
    # task 2: overlapping ranges
    if min(b, d) - max(a, c) >= 0:
      sum_2 += 1


  print('Task 1:', sum_1)
  print('Task 2:', sum_2)




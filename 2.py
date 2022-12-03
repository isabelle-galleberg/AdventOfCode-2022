
sum = 0
sum2 = 0
values = []


dict = {"X": 1, "Y": 2, "Z": 3}
task1 = {
  "X": {"A": 3, "B": 0, "C": 6}, 
  "Y":{"A": 6, "B": 3, "C": 0}, 
  "Z":{"A": 0, "B": 6, "C": 3}}


task2 = {
  "X": {"A": 3, "B": 1, "C":2}, 
  "Y":{"A": 4, "B":5, "C": 6 }, 
  "Z":{"A":8, "B": 9, "C": 7}}


with open("data/2-data.txt") as file:
    data = file.read()
    for line in data.split('\n'):
      values.append(line.split())

    for i in values:
      sum += dict[i[1]]
      sum += task1[i[1]][i[0]]

    for i in values:
      sum2 +=  task2[i[1]][i[0]]

       
    print(sum)
    print(sum2)





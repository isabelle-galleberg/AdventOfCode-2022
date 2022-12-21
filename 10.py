cycles = 0
x = 1
signals = []
sprite = [x-1, x, x+1]
pixel = -1
image = ""

# image produced by CRT
def drawImage(img):
  if len(img)%41 == 0:
    img += "\n"
  if pixel%40 in sprite:
    img += "#"
  else:
    img += "."
  return img

with open("data/10.txt") as file:
  for line in file:
    cycles += 1
    pixel += 1
    image = drawImage(image)
    if (cycles - 20) % 40 == 0:
      signals.append(cycles * x)
    if line[0:4] == "addx":
      cycles += 1
      pixel += 1
      image = drawImage(image)
      if (cycles - 20) % 40 == 0:
        signals.append(cycles * x)
      x += int(line[5:])
      sprite = [x-1, x, x+1]

print("Task 1:",sum(signals))
print("Task 2:", image)

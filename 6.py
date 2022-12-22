# returns index of last character in first start-of-packet marker
def findStartMarker(data, num):
  chars = []
  for idx, elem in enumerate(data):
    if len(chars) == num:
      return idx
    if elem not in chars:
      chars.append(elem)
    else:
      # remove stream containing duplicate char and add elem
      duplicateIdx = chars.index(elem) + 1
      chars = chars[duplicateIdx:]
      chars.append(elem)

with open("data/6.txt") as file:
  data = file.read()
  print(findStartMarker(data, 4))
  print(findStartMarker(data, 14))




      

      
   


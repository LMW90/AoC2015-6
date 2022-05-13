import re


# create and populate a list
lights = [[False for i in range(1000)] for j in range(1000)]
# print(lights)
# print(len(lights))
# print(len(lights[0]))
# print(lights[5][300])
# load the input
filename = 'inputDay-6.txt'
fhand = open(filename, 'r')
coord = re.compile(r'\d{1,3},\d{1,3}')
for line in fhand:
    results = coord.findall(line)
    # print(results)
    startPoint = results[0]
    endPoint = results[1]
    # print(f'start point: {startPoint}')
    # print(f'end point: {endPoint}')
    startX = int(startPoint.split(",")[0])
    startY = int(startPoint.split(",")[1])
    endX = int(endPoint.split(",")[0]) + 1
    endY = int(endPoint.split(",")[1]) + 1
    # print(startX)
    # print(startY)
    # print(endX)
    # print(endY)
    if line.startswith("turn on"):
        for y in range(startX, endX):
            for x in range(startY, endY):
                lights[y][x] = True
    elif line.startswith("turn off"):
         for y in range(startX, endX):
            for x in range(startY, endY):       
                lights[y][x] = False
    elif line.startswith("toggle"):
           for y in range(startX, endX):
            for x in range(startY, endY):    
                if lights[y][x] == False:
                    lights[y][x] = True
                else:
                    lights[y][x] = False
fhand.close()
counter = 0
for y in range(0, 1000):
    for x in range(0, 1000):
        if lights[y][x] == True:
            counter += 1
print(counter)


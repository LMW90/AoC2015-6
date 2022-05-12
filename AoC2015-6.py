import re
class Light: 
    def __init__(self, x, y, val=False):
        self.x, self.y, self.status = x, y, val
    def turn_on(self):
        self.status = True
    def turn_off(self):
        self.status = False
    def toggle(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True
            
"""
TODO: read input for each line run startswith() 
to determine which function call
and for which lights
data structure could just be an array 
of dictionaries with "x", "y", "status" properties
"""
# load the input
filename = "inputDay-6.txt"
fhand = open(filename)
# print(fhand)
# create and populate a list
tmp = [False] * 1000
lights = [tmp] * 1000
# print(lights)
# print(len(lights))
# print(len(lights[0]))
# print(lights[5][300])
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
        for i in range(startX, endX):
            for j in range(startY, endY):
                lights[i][j] = True
    elif line.startswith("turn off"):
         for i in range(startX, endX):
            for j in range(startY, endY):       
                lights[i][j] = False
    elif line.startswith("toggle"):
           for i in range(startX, endX):
            for j in range(startY, endY):    
                if lights[i][j] == False:
                    lights[i][j] = True
                else:
                    lights[i][j] = False
fhand.close()
counter = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if lights[i][j] == True:
            counter += 1
print(counter)


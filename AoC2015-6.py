
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
print(fhand)
# create and populate a list
lights = []
for i in range(0, 1000):
    for j in range(0, 1000):
        lights.append([i, j , False])
print(lights[999999])
print(len(lights))
filename = 'inputDay-6.txt'
fhand = open(filename, 'r')
textInput = ''
for line in fhand:
    textInput += line
fhand.close()
# print(textInput)
# make it so first comma-separated pair of ints sets starting range for loops
# (^)(\d+,\d+)*(\d+,+d+)
# for line in textInput:
    # regex.findall(line)
    # if line.startswith('turn on'):
        #  turn_on(groups[1], groups[2])
    #  elif line.startswith('turn off'):
    #     turn_off(groups[1], groups[2])
    # else:
    #     toggle(groups[1], groups[2])

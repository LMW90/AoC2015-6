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
textInput = ''
for line in fhand:
    textInput += line
fhand.close()
# print(textInput)
coord = re.compile(r'''
                   (\d{1,3})(\d{1,3}) # start coordinates group 1
                   .*                  # anything in between
                   (\d{1,3},\d{1,3}) # end coordinates group 2
                   ''', re.VERBOSE)
coord2 = re.compile(r'''
                    .*(\d{,3})(.*)
                    ''',re.X)
result = coord2.match("toggle 916,242 through 926,786")
print(result)
print(result.group(1))
print(result.group(2))
# for line in textInput:
#     if line.startswith("turn on"):
#         lights[][2] = True
#     elif line.startswith("turn off"):
#         lights[][2] = False
#     elif line.startswith("toggle"):
#         if lights[][2] == False:
#             lights[][2] = True
#         else:
#             lights[][2] = False
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

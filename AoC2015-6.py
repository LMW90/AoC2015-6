
# class light():
#     # TODO: object holding it's coordinates and "on" True/False status
    
# def toggle ():
#     # TODO: function running bitwise NOT on lights status
    
# def turn_off ():
#     # function setting light status to false
    

# def turn_on ():
#     # function setting light status to true
    
"""
TODO: read input for each line run startswith() to determine which function call
and for which lights
data structure could just be an array 
of dictionaries with "x", "y", "status" properties
"""


filename = "inputDay-6.txt"
fhand = open(filename)
# print(fhand)
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
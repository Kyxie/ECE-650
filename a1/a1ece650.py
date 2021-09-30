#!/usr/bin/env python3
import sys

# YOUR CODE GOES HERE

class Street:
    def __init__(self, command, map):
        self.command = command
        self.map = map
    
    def getStreetName(self):
        length = len(self.command)
        index = []
        for i in range(length):
            if(self.command[i] == '"'): # If we found '"'
                index.append(i) # return the index of two '"' in line
        streetName = self.command[index[0]+1: index[1]] # Contents in the middle of two '"'
        return streetName

    def getNode(self):
        num = []    # Coordinate number
        node = []
        for i in range(len(self.command)):
            if(self.command[i] == '('): # If we found '('
                char = ''
                j = i
                while(self.command[j + 1] != ','):   # Until ','
                    char = char + self.command[j + 1]
                    j = j + 1
                char = int(char)
                num.append(char)
            if(self.command[i] == ','): # If we found ','
                char = ''
                j = i
                while(self.command[j + 1] != ')'):   # Until ')'
                    char = char + self.command[j + 1]
                    j = j + 1
                char = int(char)
                num.append(char)
        for i in range(0, len(num), 2):
            node.append((num[i], num[i + 1]))
        return node
    
    def capsulate(self, name, node):    # Capsulate data into dictionary
        street = {
            "Name": name,
            "Node": node
        }
        return street
        
def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # (x1, y1) and (x2, y2) is in a line
    # (x3, y3) and (x4, y4) is in a line
    if(((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) == 0): # Parallel
        return 0
    else:
        px= ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
        py= ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        return px, py   # Intersection

def decodeNode(dict):
    lengthNum = len(dict["Node"])
    point = []
    for i in range(0, lengthNum, 2):
        point.append((int(dict["Node"][i]), int(dict["Node"][i + 1])))
    return point

def checkFunc(line, map):
    cmd = line[:3]  # First 3 letters of input contents
    if(cmd == "add"):   # If the command is add
        street = Street(line, map)  # Create a new street dictionary
        Name = street.getStreetName()
        Node = street.getNode()
        alreadyIn = []  # Streets which have already added
        if(len(map) == 0):
            map.append(street.capsulate(name=Name, node=Node))  # Add this dictionary in map list
        else:
            for i in range(len(map)):
                alreadyIn.append(map[i]["Name"])
            if(Name in alreadyIn):
                print('Warning: The street "{}" has already been added!'.format(Name))
            else:
                map.append(street.capsulate(name=Name, node=Node))  # Add this dictionary in map list
        print(map)

    elif(cmd == "mod"):
        street = Street(line, map)
        Name = street.getStreetName()
        Node = street.getNode()
        alreadyIn = []
        for i in range(len(map)):
            alreadyIn.append(map[i]["Name"])
        if(Name in alreadyIn):
            map.remove(map[i])  # First delete
            map.append(street.capsulate(name=Name, node=Node))  # Then add
        else:
            print('Error: There is no such street called "{}"!'.format(Name))    
        print(map)

    elif(cmd == "rm "):
        index = []
        for i in range(len(line)):
            if(line[i] == '"'): # If we found "
                index.append(i) # return the index of two " in line
        Name = line[index[0]+1: index[1]] # Contents in the middle of two "
        alreadyIn = []
        for i in range(len(map)):
            alreadyIn.append(map[i]["Name"])
        if(Name in alreadyIn):
            map.remove(map[i])  # Delete
        else:
            print('Error: There is no such street called "{}"!'.format(Name)) 
        print(map)

    elif(cmd[:2] == "gg"):
        intersection = {}
        endpoint = {}
        V = {}
        E = {}
        if(len(map) == 1):
            print("V =", V)
            print("E =", E)
        else:
            for i in range(len(map)):
                chosenStreet = map[i]
                otherStreet = map[:i] + map[i + 1:]
                chosenPoint = decodeNode(chosenStreet)
                print(chosenPoint)
                # otherPoint = decodeNode(otherStreet)
                # print(chosenPoint)
                # print(otherPoint)


    elif(cmd[0] == ' '):    # Finish code
        print("Finished reading input")
        # return exit code 0 on successful termination
        sys.exit(0)
    else:
        command = ""
        for i in range(len(line)):
            command = command + line[i]
            if(line[i + 1] == ' '):
                break
        print('Error: There is no such command called "{}"!'.format(command))

def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
    map = []
    while True:
        line = sys.stdin.readline()
        checkFunc(line, map)

if __name__ == "__main__":
    main()

# add "A Street" (1,2) (3,4) (5,6)
# add "B Street" (11,2) (3,14) (15,6)
# add "C Street" (11,12) (13,14) (15,16) 
# [{'Name': 'A Street', 'Node': [(1, 2), (3, 4), (5, 6)]}, {'Name': 'B Street', 'Node': [(11, 2), (3, 14), (15, 6)]}]
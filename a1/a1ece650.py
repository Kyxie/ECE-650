#!/usr/bin/env python3
import sys

# YOUR CODE GOES HERE

class Street:
    def __init__(self, command, map):
        self.command = command
        self.map = map
    
    def getStreetName(self):
        index = []
        for i in range(len(self.command)):
            if(self.command[i] == '"' or self.command[i] == "'"): # If we found '"' or "'"
                index.append(i) # return the index of two '"' in line
        streetName = self.command[index[0] + 1: index[1]] # Contents in the middle of two '"'
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
    
class Map:
    def __init__(self, line, map):
        self.line = line
        self.map = map
    
    def checkFunc(self):
        if(self.line[:3] == "add"):  # If the command is add
            self.add()

        elif(self.line[:3] == "mod"):
            self.mod()

        elif(self.line[:2] == "rm"):
            self.rm()

        elif(self.line[:2] == "gg"):
            self.gg()

        elif(self.line[0] == ' '):    # Finish code
            print("Finished reading input")
            # return exit code 0 on successful termination
            sys.exit(0)

        else:
            command = ""
            for i in range(len(self.line) - 1):
                command = command + self.line[i]
            print('Error: There is no such command called "{}"!'.format(command))
    
    def add(self):
        if(self.line[3] == ' '):
            if(self.line[4] == '"' or self.line[4] == "'"):
                leftBracketIndex = []
                leftBracket = 0
                rightBracket = 0
                for i in range(len(self.line)):
                    if(self.line[i] == '('):
                        leftBracket = leftBracket + 1
                        leftBracketIndex.append(i)
                    if(self.line[i] == ')'):
                        rightBracket = rightBracket + 1
                if(leftBracket == 0 or rightBracket == 0 or leftBracket != rightBracket):
                    print("Error: Vertices assignment error!")
                elif(self.line[min(leftBracketIndex) - 1] != ' '):
                    print("Error: Expect a space between street name and vertice!")
                else:
                    street = Street(self.line, self.map)  # Create a new street dictionary
                    Name = street.getStreetName()
                    Node = street.getNode()
                    alreadyIn = []  # Streets which have already added
                    if(len(self.map) == 0):
                        self.map.append(street.capsulate(name=Name, node=Node))  # Add this dictionary in map list
                    else:
                        for i in range(len(self.map)):
                            alreadyIn.append(self.map[i]["Name"])
                        if(Name in alreadyIn):
                            print('Warning: The street "{}" has already been added!'.format(Name))
                        else:
                            self.map.append(street.capsulate(name=Name, node=Node))  # Add this dictionary in map list
            else:
                print("Error: Except a \" or \' around street name!")
        else:
            print("Error: Expect a space between the command and street name!")
        # print(self.map)
    
    def mod(self):
        if(self.line[3] == ' '):
            if(self.line[4] == '"' or self.line[4] == "'"):
                leftBracketIndex = []
                leftBracket = 0
                rightBracket = 0
                for i in range(len(self.line)):
                    if(self.line[i] == '('):
                        leftBracket = leftBracket + 1
                        leftBracketIndex.append(i)
                    if(self.line[i] == ')'):
                        rightBracket = rightBracket + 1
                if(leftBracket == 0 or rightBracket == 0 or leftBracket != rightBracket):
                    print("Error: Vertices assignment error!")
                elif(self.line[min(leftBracketIndex) - 1] != ' '):
                    print("Error: Expect a space between street name and vertice!")
                else:
                    street = Street(self.line, self.map)
                    Name = street.getStreetName()
                    Node = street.getNode()
                    alreadyIn = []
                    for i in range(len(self.map)):
                        alreadyIn.append(self.map[i]["Name"])
                    if(Name in alreadyIn):
                        self.map.remove(self.map[i])  # First delete
                        self.map.append(street.capsulate(name=Name, node=Node))  # Then add
                    else:
                        print('Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Except a \" or \' around street name!")
        else:
            print("Error: Expect a space between the command and street name!")
        # print(self.map)
    
    def rm(self):
        if(self.line[2] == ' '):
            if(self.line[3] == '"' or self.line[3] == "'"):
                index = []
                for i in range(len(self.line)):
                    if(self.line[i] == '"'): # If we found "
                        index.append(i) # return the index of two " in line
                Name = self.line[index[0]+1: index[1]] # Contents in the middle of two "
                alreadyIn = []
                for i in range(len(self.map)):
                    alreadyIn.append(self.map[i]["Name"])
                if(Name in alreadyIn):
                    map.remove(self.map[i])  # Delete
                else:
                    print('Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Expect a \" or \' around street name!")
        else:
            print("Error: Expect a space between command and street name!")
        # print(self.map)
    
    def gg(self):
        intersection = []
        endPoint = []
        V = {}
        E = []
        if(len(self.map) == 0 or len(self.map) == 1):
            print("V = {\n}")
            print("E = {\n}")
        else:
            for i in range(len(self.map)):
                chosenStreet = [self.map[i]] # Change to a list
                otherStreet = self.map[i + 1:]
                chosenPoint = decodeNode(chosenStreet)  # List of points
                otherPoint = decodeNode(otherStreet)
                for j in range(len(otherPoint)):
                    for k in range(len(chosenPoint[0]) - 1):
                        for l in range(len(otherPoint[j]) - 1):
                            x1 = chosenPoint[0][k][0]
                            y1 = chosenPoint[0][k][1]
                            x2 = chosenPoint[0][k + 1][0]
                            y2 = chosenPoint[0][k + 1][1]
                            x3 = otherPoint[j][l][0]
                            y3 = otherPoint[j][l][1]
                            x4 = otherPoint[j][l + 1][0]
                            y4 = otherPoint[j][l + 1][1]
                            (px, py) = findIntersection(x1, y1, x2, y2, x3, y3, x4, y4)
                            if((px, py) != ('F', 'F')):
                                intersection.append((px, py))   # Intersection
                                endPoint.append((x1, y1))
                                endPoint.append((x2, y2))
                                endPoint.append((x3, y3))
                                endPoint.append((x4, y4))   # The 4 points which form an intersection
            vertices = list(set(intersection + endPoint))    # Delete the duplication and turn to a list
            for i, vertice in enumerate(vertices):
                V[i] = vertice
            for i in range(0, len(endPoint), 4):
                leftPoint = endPoint[i]
                for j in range(len(V)):
                    if(V[j] == leftPoint):
                        E.append(j + 1)
                rightPoint = endPoint[i + 1]
                for j in range(len(V)):
                    if(V[j] == rightPoint):
                        E.append(j + 1)
                upPoint = endPoint[i + 2]
                for j in range(len(V)):
                    if(V[j] == upPoint):
                        E.append(j + 1)
                downPoint = endPoint[i + 3]
                for j in range(len(V)):
                    if(V[j] == downPoint):
                        E.append(j + 1)
        printResult(V, E)

def printResult(V, E):
    print("V = {")
    for i in range(len(V)):
        print("{}:  ({:.2f},{:.2f})".format(i + 1, V[i][0], V[i][1]))
    print("}")
    print("E = {")
    for i in range(0, len(E), 2):
        print("<{},{}>,".format(E[i], E[i + 1]))
    print("}")

def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # (x1, y1) and (x2, y2) is in a line
    # (x3, y3) and (x4, y4) is in a line
    if(((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) != 0): # Not Parallel
        px= ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
        py= ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        if(x1 >= x2 and y1 >= y2):
            if(px >= x2 and px <= x1 and py >= y2 and py <= y1):
                return px, py
            else:
                px = 'F'
                py = 'F'
                return px, py
        elif(x1 <= x2 and y1 >= y2):
            if(px >= x1 and px <= x2 and py >= y2 and py <= y1):
                return px, py
            else:
                px = 'F'
                py = 'F'
                return px, py
        elif(x1 >= x2 and y1 <= y2):
            if(px >= x2 and px <= x1 and py >= y1 and py <= y2):
                return px, py
            else:
                px = 'F'
                py = 'F'
                return px, py
        elif(x1 <= x2 and y1 <= y2):
            if(px >= x1 and px <= x2 and py >= y1 and py <= y2):
                return px, py
            else:
                px = 'F'
                py = 'F'
                return px, py
    else:
        px = 'F'
        py = 'F'
        return px, py

def decodeNode(list):
    point = []
    for i in range(len(list)):
        point.append((list[i]["Node"]))
    return point

def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
    map = []
    while True:
        line = sys.stdin.readline()
        world = Map(line, map)
        world.checkFunc()

if __name__ == "__main__":
    main()

# add "Weber Street" (2,-1)(2,2)(5,5)(5,6)(3,8)
# add "King Street" (4,2)(4,8)
# add "Davenport Road" (1,4)(5,8)
#!/usr/bin/env python3
import sys
import re

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
        cmd = re.search(r'\s', self.line)
        if(self.line[:3] == "add"):  # If the command is add
            self.add()

        elif(self.line[:3] == "mod"):
            self.mod()

        elif(self.line[:2] == "rm"):
            self.rm()

        elif(self.line[:2] == "gg"):
            self.gg()
        
        elif(self.line[:3] == "map"):
            print(self.map)

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
                    do = 1
                    street = Street(self.line, self.map)  # Create a new street dictionary
                    Name = street.getStreetName().lower()

                    if(Name[0] == ' ' or Name[-1] == ' '):
                        print("Error: No Leading or following white space!")
                        do = 0
                    
                    moreSpace = re.search(r'\s{2,10}', Name)
                    if(moreSpace):
                        print("Error: No more than 1 white space in street name!")
                        do = 0

                    plus = re.search(r'\+', self.line)
                    if(plus):
                        print("Error: Input positive number without '+' sign!")
                        do = 0

                    numOfBracket = 0
                    for i in range(len(self.line)):
                        if(self.line[i] == '('):
                            numOfBracket = numOfBracket + 1
                    if(numOfBracket == 1 or numOfBracket == 0):
                        print("Error: Not enough points for a line")
                        do = 0
                    
                    specialCharacter = "~!@#$%^&*()_+`1234567890-=\{\}|[]\\;:,./<>?"
                    for i in range(len(specialCharacter)):
                        if(specialCharacter[i] in Name):
                            print("Error: No special characters or numbers!")
                            do = 0
                            break
                    
                    cordinateRegex = re.search(r'\(.*\)', self.line)
                    cordinate = self.line[cordinateRegex.span()[0]:cordinateRegex.span()[1]]
                    if(' ' in cordinate):
                        print("Error: Invalid cordination assignment, no space!")
                        do = 0

                    Node = street.getNode()
                    alreadyIn = []  # Streets which have already added
                    if(do == 1):
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
                    do = 1

                    numOfBracket = 0
                    for i in range(len(self.line)):
                        if(self.line[i] == '('):
                            numOfBracket = numOfBracket + 1
                    if(numOfBracket == 1 or numOfBracket == 0):
                        print("Error: Not enough points for a line")
                        do = 0
    
                    if(do == 1):
                        street = Street(self.line, self.map)
                        Name = street.getStreetName().lower()
                        Node = street.getNode()
                        alreadyIn = []
                        for i in range(len(self.map)):
                            alreadyIn.append(self.map[i]["Name"])
                            if(alreadyIn[i] == Name):
                                self.map[i] = street.capsulate(name=Name, node=Node)
                                break
                        if(Name not in alreadyIn):
                            print('Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Except a \" or \' around street name!")
        else:
            print("Error: Expect a space between the command and street name!")
        # print(self.map)
    
    def rm(self):
        if(self.line[2] == ' '):
            if(self.line[3] == '"' or self.line[3] == "'"):
                do = 1
                
                rmCord = re.search(r'(\"|\')$', self.line)
                if(rmCord == None):
                    print("Error: No cordination in command 'rm'!")
                    do = 0

                if(do == 1):
                    index = []
                    for i in range(len(self.line)):
                        if(self.line[i] == '"'): # If we found "
                            index.append(i) # return the index of two " in line
                    Name = self.line[index[0]+1: index[1]] # Contents in the middle of two "
                    Name = Name.lower()
                    alreadyIn = []
                    for i in range(len(self.map)):
                        alreadyIn.append(self.map[i]["Name"])
                        if(Name in alreadyIn):
                            self.map.remove(self.map[i])  # Delete
                            break
                    if(Name not in alreadyIn):
                            print('Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Expect a \" or \' around street name!")
        else:
            print("Error: Expect a space between command and street name!")
        # print(self.map)
    
    def gg(self):
        do = 1
        checkgg = "gg\n"
        if(checkgg != self.line):
            print("Error: Wrong 'gg' command")
            do = 0
        if(do == 1):
            V = {}
            E = []
            intersection = []
            endPoint = []
            package = []
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
                                    endPoint.append((x4, y4))   # The 4 edges which form an intersection
                                    package.append(((px, py), (x1, y1), (x2, y2), (x3, y3), (x4, y4)))
                vertices = list(set(intersection + endPoint))   # Delete the duplication and turn to a list
                for i, vertice in enumerate(vertices):
                    V[i] = vertice
                for i in range(len(intersection)):
                    pi = intersection[i]    # The intersection
                    otherInter = intersection[:i] + intersection[i + 1:]
                    if(len(otherInter) == 0):
                        for j in range(1, 5):
                            pj = package[i][j]
                            isInE(E, pi, pj)
                    else:
                        for j in range(1, 5):  # An intersection is caused by 4 endpoints
                            pj = package[i][j]  # The end point
                            for k in range(len(otherInter)):
                                q = otherInter[k]   # The other intersection
                                if(isPointOnSeg(q, pi, pj) == True):
                                    isInE(E, pi, q)
                                else:
                                    isInE(E, pi, pj)
                for i in range(len(E)):
                    for j in range(2):
                        for k in range(len(V)):
                            if(E[i][j] == V[k]):
                                E[i][j] = k + 1
                printResult(V, E)

def printResult(V, E):
    print("V = {")
    for i in range(len(V)):
        print("   {}:  ({:.2f},{:.2f})".format(i + 1, V[i][0], V[i][1]))
    print("}")
    print("E = {")
    for i in range(len(E)):
        print("   <{},{}>,".format(E[i][0], E[i][1]))
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

def isPointOnSeg(q, pi, pj):
    # Point[0] means x
    # Point[1] means y
    qx = q[0]
    qy = q[1]
    pix = pi[0]
    piy = pi[1]
    pjx = pj[0]
    pjy = pj[1]
    if((qx - pix) * (pjy - piy) == (pjx - pix) * (qy - piy)
    and min(pix, pjx) <= qx and qx <= max(pix, pjx)
    and min(piy, pjy) <= qy and qy <= max(piy, pjy)):
        return True
    else:
        return False

def isInE(E, pi, pj):
    # E: [[(x1, y1), (x2, y2)], [(x3, y3), (x4, y4)], ...]
    # pi: (x1, y1)
    # pj: (x2, y2)
    if([pi, pj] not in E and [pj, pi] not in E and pi != pj):
        E.append([pi, pj])

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
        line = sys.stdin.readline().strip('\n')
        world = Map(line, map)
        world.checkFunc()

if __name__ == "__main__":
    main()

# Test
# add "Weber Street" (2,-1)(2,2)(5,5)(5,6)(3,8)
# add "King Street" (4,2)(4,8)
# add "Davenport Road" (1,4)(5,8)
# mod "Weber Street" (2,1)(2,2)
# rm "King Street"
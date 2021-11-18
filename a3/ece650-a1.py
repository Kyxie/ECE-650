'''
Date: 2021-11-10 15:09:38
LastEditors: Kunyang Xie
LastEditTime: 2021-11-18 14:48:05
FilePath: /a3/ece650-a1.py
'''

#!/usr/bin/env python3

# YOUR CODE GOES HERE


import sys
import re


class Street:
    def __init__(self, command, map):
        self.command = command
        self.map = map

    def getStreetName(self):
        index = []
        for i in range(len(self.command)):
            if(self.command[i] == '"' or self.command[i] == "'"):  # If we found '"' or "'"
                index.append(i)  # return the index of two '"' in line
        # Contents in the middle of two '"'
        streetName = self.command[index[0] + 1: index[1]]
        return streetName

    def getNode(self):
        num = []    # Coordinate number
        node = []
        for i in range(len(self.command)):
            if(self.command[i] == '('):  # If we found '('
                char = ''
                j = i
                while(self.command[j + 1] != ','):   # Until ','
                    char = char + self.command[j + 1]
                    j = j + 1
                char = int(char)
                num.append(char)
            if(self.command[i] == ','):  # If we found ','
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

        elif(self.line[:3] == "clr"):
            self.map.clear()

        elif(self.line == ''):
            ...

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
                    # Create a new street dictionary
                    street = Street(self.line, self.map)
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

                    specialCharacter = "~!@#$%^&*()_+`-=\{\}|[]\\;:,./<>?"
                    for i in range(len(specialCharacter)):
                        if(specialCharacter[i] in Name):
                            print("Error: No special characters!")
                            do = 0
                            break

                    Node = street.getNode()
                    alreadyIn = []  # Streets which have already added
                    if(do == 1):
                        if(len(self.map) == 0):
                            # Add this dictionary in map list
                            self.map.append(
                                street.capsulate(name=Name, node=Node))
                        else:
                            for i in range(len(self.map)):
                                alreadyIn.append(self.map[i]["Name"])
                            if(Name in alreadyIn):
                                print(
                                    'Error: The street "{}" has already been added!'.format(Name))
                            else:
                                # Add this dictionary in map list
                                self.map.append(
                                    street.capsulate(name=Name, node=Node))
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
                                self.map[i] = street.capsulate(
                                    name=Name, node=Node)
                                break
                        if(Name not in alreadyIn):
                            print(
                                'Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Except a \" or \' around street name!")
        else:
            print("Error: Expect a space between the command and street name!")
        # print(self.map)

    def rm(self):
        if(self.line[2] == ' '):
            if(self.line[3] == '"' or self.line[3] == "'"):
                do = 1

                if(do == 1):
                    index = []
                    for i in range(len(self.line)):
                        if(self.line[i] == '"'):  # If we found "
                            # return the index of two " in line
                            index.append(i)
                    # Contents in the middle of two "
                    Name = self.line[index[0]+1: index[1]]
                    Name = Name.lower()
                    alreadyIn = []
                    for i in range(len(self.map)):
                        alreadyIn.append(self.map[i]["Name"])
                        if(Name in alreadyIn):
                            self.map.remove(self.map[i])  # Delete
                            break
                    if(Name not in alreadyIn):
                        print(
                            'Error: There is no such street called "{}"!'.format(Name))
            else:
                print("Error: Expect a \" or \' around street name!")
        else:
            print("Error: Expect a space between command and street name!")
        # print(self.map)

    def gg(self):
        do = 1
        if(do == 1):
            V = {}
            E = []
            intersection = []
            endPoint = []
            package = []
            if(len(self.map) == 0 or len(self.map) == 1):
                print("V 0")
                print("E {}")
            else:
                for i in range(len(self.map)):
                    chosenStreet = [self.map[i]]  # Change to a list
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
                                (px, py) = findIntersection(
                                    x1, y1, x2, y2, x3, y3, x4, y4)
                                if((px, py) != ('F', 'F')):
                                    intersection.append(
                                        (px, py))   # Intersection
                                    endPoint.append((x1, y1))
                                    endPoint.append((x2, y2))
                                    endPoint.append((x3, y3))
                                    # The 4 edges which form an intersection
                                    endPoint.append((x4, y4))
                                    package.append(
                                        ((px, py), (x1, y1), (x2, y2), (x3, y3), (x4, y4)))
                # Delete the duplication and turn to a list
                vertices = list(set(intersection + endPoint))
                for i, vertice in enumerate(vertices):
                    V[i] = vertice
                if(len(V) == 0):
                    print("V 0")
                    print("E {}")
                else:
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
                                    # The other intersection
                                    q = otherInter[k]
                                    if(isPointOnSeg(q, pi, pj)):
                                        pj = q
                                        continue
                                isInE(E, pi, pj)
                    for i in range(len(E)):
                        for j in range(2):
                            for k in range(len(V)):
                                if(E[i][j] == V[k]):
                                    E[i][j] = k + 1
                    printResult(V, E)


def printResult(V, E):
    print("V ", end='')
    print(len(V))
    print("E {", end='')
    for i in range(len(E) - 1):
        print("<{},{}>,".format(E[i][0], E[i][1]), end='')
    print("<{},{}>".format(E[len(E) - 1][0], E[len(E) - 1][1]), end='')
    print("}")


def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # (x1, y1) and (x2, y2) is in a line
    # (x3, y3) and (x4, y4) is in a line
    if(((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)) != 0):  # Not Parallel
        px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
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
    # q: The other intersection
    # pi: The intersection
    # pj: The endpoints
    # Point[0] means x
    # Point[1] means y
    qx = q[0]
    qy = q[1]
    pix = pi[0]
    piy = pi[1]
    pjx = pj[0]
    pjy = pj[1]
    if(((qx - pix) * (pjy - piy) - (pjx - pix) * (qy - piy) < 0.01)
       and ((qx - pix) * (pjy - piy) - (pjx - pix) * (qy - piy) > -0.01)
       and min(pix, pjx) <= qx and qx <= max(pix, pjx)
       and min(piy, pjy) <= qy and qy <= max(piy, pjy)):    # In a line and between 2 points
        return True
    else:
        return False    # Not in a line


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
        line = sys.stdin.readline()
        world = Map(line, map)
        world.checkFunc()
        if line == "":
            break
    sys.exit(0)


if __name__ == "__main__":
    main()

# Test
# add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)
# add "King Street S" (3,2) (4,8)
# add "Davenport Road" (0,0) (5,8)
# mod "Weber Street" (2,1)(2,2)
# rm "King Street"

# add "Weber Street" (-1,0)(4,0)
# add "King Street" (0,-1)(0,4)
# add "Davenport Road" (0,3)(3,0)

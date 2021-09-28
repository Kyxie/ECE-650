#!/usr/bin/env python3
import sys

# YOUR CODE GOES HERE

class Map:
    def __init__(self, streetName, node):
        self.streeName = streetName
        self.node = node

def add(streetName, node, map):
    print("This is add")

def mod(streetName, node, map):
    print("This is mod")

def rm(streetName, node, map):
    print("This is rm")

def gg():
    print("This is gg")

def getStreetName(line):
    length = len(line)
    index = []
    for i in range(length):
        if(line[i] == '"'): # If we found "
            index.append(i) # return the index of two " in line
    streetName = line[index[0]+1: index[1]] # Contents in the middle of two "
    return streetName

def getNode(line):
    length = len(line)
    node = []
    for i in range(length):
        if(line[i] == ','): # If we found ,
            node.append(line[i - 1])  
            node.append(line[i + 1])    # add content before and after ,
    return node

def check_func(line):
    cmd = line[:3]
    streetName = getStreetName(line)
    node = getNode(line)
    map = Map()
    
    if(cmd == 'add'):
        add(streetName, node, map)
    elif(cmd == 'mod'):
        mod(streetName, node, map)
    elif(cmd == 'rm '):
        rm(streetName, node, map)
    elif(cmd == 'gg '):
        gg()
    else:
        print("Error")


def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        check_func(line)

    print("Finished reading input")
    # return exit code 0 on successful termination
    sys.exit(0)


if __name__ == "__main__":
    main()

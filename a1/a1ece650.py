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
            if(self.command[i] == '"'): # If we found "
                index.append(i) # return the index of two " in line
        streetName = self.command[index[0]+1: index[1]] # Contents in the middle of two "
        return streetName

    def getNode(self):
        length = len(self.command)
        node = []
        for i in range(length):
            if(self.command[i] == ','): # If we found ,
                node.append(self.command[i - 1])  
                node.append(self.command[i + 1])    # add content before and after ,
        return node
    
    def capsulate(self, name, node):    # Capsulate data into dictionary
        street = {
            "Name": name,
            "Node": node
        }
        return street
    
def checkFunc(line, map):
    cmd = line[:3]  # First 3 letters of input contents
    if(cmd == "add"):   # If the command is add
        street = Street(line, map)  # Create a new street dictionary
        Name = street.getStreetName()
        Node = street.getNode()
        map.append(street.capsulate(name=Name, node=Node))  # Add this dictionary in map list
        print(map)

    elif(cmd == "mod"):
        street = Street(line, map)
        Name = street.getStreetName()
        Node = street.getNode()
        streetQuantity = len(map)
        for i in range(streetQuantity):
            if(map[i]["Name"] == Name):
                map.remove(map[i])  # First delete
                map.append(street.capsulate(name=Name, node=Node))  # Then add
        print(map)

    elif(cmd == "rm "):
        length = len(line)
        index = []
        for i in range(length):
            if(line[i] == '"'): # If we found "
                index.append(i) # return the index of two " in line
        Name = line[index[0]+1: index[1]] # Contents in the middle of two "

        streetNum = len(map)
        for i in range(streetNum):
            if(map[i]["Name"] == Name): # Find we want to delete according to name
                map.remove(map[i])
                break
        print(map)
    elif(cmd == "gg "):
        ...
    
    else:
        print("Error")

def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
    map = []
    while True:
        line = sys.stdin.readline()
        if line == ' ':
            break
        checkFunc(line, map)

    print("Finished reading input")
    # return exit code 0 on successful termination
    sys.exit(0)


if __name__ == "__main__":
    main()

# add "A Street" (1,2) (3,4)
# [{'Name': 'A Street', 'Node': ['1', '2', '3', '4']}, {'Name': 'B Street', 'Node': ['1', '2', '3', '4']}]
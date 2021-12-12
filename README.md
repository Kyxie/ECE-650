## ECE650

### Introduction

The project is to help the local police department with their installation of security cameras at traffic intersections. We solved a particular kind of optimization problem, called the Vertex Cover problem, in this context. The idea is for the police to be able to minimize the number of cameras they need to install, and still be as effective as possible with their monitoring. This project has 4 parts, A1, A2, A3, and A4, while A3 is the combination of A1 and A2.

### Environment

Linux or MacOs

### Codes

1. A1:

   > Path: a1/ece650-a1.py
   >
   > Run:
   >
   > ```Shell
   > $ cd a1
   > $ python3 ece650-a1.py
   > ```

   In this file type the command and the code will generate a map and return an undirected graph. Here are the commands:

   - The command ***add*** is used to add a street. It is specified as:

     > add "Street Name" ($x_1$,$y_1$) ($x_2$, $y_2$) ... ($x_n$, $y_n$)

     Each ($x_i$, $y_i$) is a GPS coordinate. We interpret the coordinates as a poly-line segment.
     That is, we draw a line segment from ($x_i$, $y_i$) to ($x_i+1$, $y_i+1$). Assume that each $x_i$ and $y_i$ is an integer.

   - The command ***mod*** is used to modify the specification of a street. It is specified as:

     > mod "Street Name" ($x_1$,$y_1$) ($x_2$, $y_2$) ... ($x_n$, $y_n$)

     Its format is the same as for ***add***. It is a new specification for a street we have specified before.

   - The command ***rm*** is used to remove a street. It is specified as:

     > rm "Street Name"

   - The command ***gg*** causes the program to output the corresponding graph, it is specified as:

     > gg

   - The command ***map*** causes the program to output the map information, which contains every street's name and coordinates. it is specified as:

     > map

   - The command ***clr*** remove all the streets in the map. it is specified as:

     > clr

   Notes:

   - There is a space between command and left quotation mark, between right quotation mark and left bracket, and between each coordinate.
   - Street name cannot starts and ends with white space.
   - No two or more continuous white space in street name.
   - One street should have at least two points.
   - No special character in street name.
   - A street cannot cross with it self and two streets will not overlap.

   | Wrong Examples              | Reason                       |
   | --------------------------- | ---------------------------- |
   | ~~add"A Street"(1,2)(3,4)~~ | No space                     |
   | ~~" A Street"~~             | Have leading space           |
   | ~~"A   Street"~~            | Have three continuous spaces |
   | ~~add "A Street" (1,2)~~    | Only one point in a street   |
   | ~~"A @@@ Street"~~          | Contain special characters   |

   Here are examples:

   ```Shell
   # Inputs
   add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)
   add "King Street S" (4,2) (4,8)
   add "Davenport Road" (1,4) (5,8)
   gg
   # Outputs
   V = {
   	1: (2,2)
   	2: (4,2)
   	3: (4,4)
   	4: (5,5)
   	5: (1,4)
   	6: (4,7)
   	7: (5,6)
   	8: (5,8)
   	9: (3,8)
   	10: (4,8)
   }
   E = {
   	<1,3>,
   	<2,3>,
   	<3,4>,
   	<3,6>,
   	<7,6>,
   	<6,5>,
   	<9,6>,
   	<6,8>,
   	<6,10>
   }
   # Inputs
   mod "Weber Street" (2,1) (2,2)
   gg
   #Outputs
   V = {
   	2: (4,2)
   	5: (1,4)
   	6: (4,7)
   	8: (5,8)
   	10: (4,8)
   }
   E = {
   	<2,6>,
   	<6,5>,
   	<6,8>,
   	<6,10>
   }
   # Inputs
   rm "King Street S"
   gg
   # Outputs
   V = {
   }
   E = {
   }
   ```

2. A2:

   > Path: a2/ece650-a2.cpp
   >
   > Run:
   >
   > ```shell
   > # Linux/MacOs
   > $ cd a2
   > $ mkdir build
   > $ cd build
   > $ cmake ../
   > $ make
   > $ ./ece650-a2
   > 
   > # Windows
   > $ cd a2
   > $ g++ ece650-a3.cpp -o ece650-a3.exe
   > $ start ece650-a2.exe
   > ```

   In this file type the command and the code will generate a route. Here are the commands:

   - The command ***V*** specifies the total number of vertices, it is specified as:

     > V 15

   - The command ***E*** specifies the edges, it is specified as:

     > E {<1,2>,<3,4>,<5,6>}

   - The command ***s*** specifies the route, from point *a* to point *b* (*a* and *b* are numbers in ***E***), it is specified as:

     > s 1 2

   Notes:

   - The coordinates in ***E*** and ***s*** should smaller than the coordinates in ***V***.
   - No space in ***E*** except the only space after the letter *E*.

    Here is are examples:

   ```Shell
   # Inputs
   V 15
   E {<2,6>,<2,8>,<2,5>,<6,5>,<5,8>,<6,10>,<10,8>}
   s 2 10
   # Outputs
   2-8-10
   # Inputs
   V 5
   E {<1,3>,<3,2>,<3,4>,<4,5>,<5,2>}
   s 5 1
   # Outputs
   5-2-3-1
   ```

3. A3 - rgen.cpp:

   > Path: a3/rgen.cpp
   >
   > Run:
   >
   > ```Shell
   > # This file can only run in Linux/MacOs
   > $ cd a3
   > $ mkdir build
   > $ cd build
   > $ cmake ../
   > $ make
   > $ ./rgen -s ks -n kn -l kl -c kc
   > ```

   Note:

   - This file generate the input of A1.
   - ***ks*** is the upper bound of the number of street, which is an integer larger or equal to 2, the number of streets should be a random integer in $[2, ks]$. If this option is not sspecified, the default of ks is equal to 10; that is, the number of streets should be a random integer in $[2, 10]$.
   - ***kn*** is the upper bound of the number of line segment of a street, where ***kn*** is an integer larger of equal to 1. The number of line segments in each street should be a random integer in $[1, kn]$. Default: $kn = 5$.
   - ***kl*** is the upper bound of the wait time, where ***kl*** is an integer larger or equal to 5. The process should wait a random number *w* seconds, where *w* is in $[5, kl]$ before generating the next random input. Default: $kl = 5$.
   - ***kc*** is the upper bound of coordinate number, where ***kc*** is an integer larger or equal to 1. The process should generate ($x$, $y$) coordinates such that every $x$ and $y$ value is in the range $[-kc, kc]$. For example, if $kc = 15$, all of the coordinate values should be integers between -15 and 15. Default: $kc = 20$.
   - No same point in one street.
   - No self intersection in one street.
   - No over lap in one street and between different streets.
   - Three consecutive nodes on a street cannot be collinear.
   - If the computer fails to generate a point 25 times, the process stops.
   - If the inputs of ***ks***, ***kn***, ***kl*** is smaller than its minimum value, the process stops.

   Here are some examples:

   ```Shell
   # Input
   $./ece65 -s 2
   # Output
   clr
   add "Street1" (10,-3) (13,3) (-5,-16) (0,6) (-13,-13)
   add "Street2" (10,-5) (-4,-13)
   gg
   # Wait several seconds
   clr
   add "Street1" (0,16) (-20,20) (-2,-12) (3,18) (13,10) (10,-2)
   add "Street2" (2,18) (20,-19) (-9,16) (-16,-14)
   gg
   ```

4. A3 - ece650-a3.cpp:

   > Path: a3/ece650-a3.cpp
   >
   > Run:
   >
   > ```Shell
   > # This file can only run in Linux/MacOs
   > # If you have already cmaked rgen
   > $ cd build
   > $ ./ece650-a3 -s ks -n kn -l kl -c kc
   > # else
   > $ cd a3
   > $ mkdir build
   > $ cd build
   > $ cmake ../
   > $ make
   > $ ./ece650-a3 -s ks -n kn -l kl -c kc
   > ```

   This file is the driver file which connect rgen.cpp, ece650-a1.py, and ece650-a2.cpp. 

   Here are some examples:

   ```Shell
   # Input
   $ ./ece650-a3 -s 2
   # Output
   V 7
   E {<5,7>,<5,6>,<5,3>,<5,4>,<4,6>,<4,2>,<4,1>}
   # Input
   s 2 1
   # Output
   2-4-1
   # Output
   V 12
   E {<1,8>,<1,5>,<1,3>,<1,6>,<6,5>,<6,10>,<6,3>,<6,7>,<7,10>,<7,12>,<7,2>,<2,12>,<2,11>,<2,4>,<11,4>,<11,9>}
   # Input
   s 2 1
   # Output
   2-7-6-1
   # Output
   V 5
   E {<3,4>,<3,1>,<3,2>,<3,5>}
   # Input
   s 2 1
   # Output
   2-3-1
   ```

5. A4:

   > Path: a4/ece650-a4.cpp
   >
   > ```Shell
   > # This file can only run in Linux/MacOs
   > $ cd a4
   > $ mkdir build
   > $ cd build
   > $ cmake ../
   > $ make
   > $ ./ece650-a4
   > ```

   Notes:

   - This file's input is a map, we need to input the map just like what we did in A2.
   - The output of this file is to find the vertex cover. [What is a vertex cover problem?](https://en.wikipedia.org/wiki/Vertex_cover)
   - We used MiniSAT solver to solve this problem. [What is a MiniSAT?](http://minisat.se)
   - The MiniSAT solver code is here: https://github.com/agurfinkel/minisat

   Here is an example:

   ```Shell
   # Input
   $ ./ece650-a4
   V 5
   E {<1,5>,<5,2>,<1,4>,<4,5>,<4,3>,<2,4>}
   # Output
   4 5
   ```



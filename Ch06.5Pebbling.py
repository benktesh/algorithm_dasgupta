#Author: Benktesh
#benktesh1@gmail.com
#12/29/2017
#Dasgupta Solutions 6.5
'''
Pebbling a checkerboard. We are given a checkerboard which has 4 rows and n columns, and
has an integer written in each square. We are also given a set of 2n pebbles, and we want to
place some or all of these on the checkerboard (each pebble can be placed on exactly one square)
so as to maximize the sum of the integers in the squares that are covered by pebbles. There is
one constraint: for a placement of pebbles to be legal, no two of them can be on horizontally or
vertically adjacent squares (diagonal adjacency is ne).

    (a) Determine the number of legal patterns that can occur in any column (in isolation, ignoring
        the pebbles in adjacent columns) and describe these patterns.

Call two patterns compatible if they can be placed on adjacent columns to form a legal placement.
Let us consider subproblems consisting of the rst k columns 1  k  n. Each subproblem can
be assigned a type, which is the pattern occurring in the last column.
    (b) Using the notions of compatibility and type, give an O(n)-time dynamic programming algorithm
        for computing an optimal placement.
'''
'''
    Solution:
    (a) There are 8 patterns. The patterns are respectively:
        1. - - - -  i.e. empty
        2. X - - - i.e. first filled rest empty
        3. - X - - i.e. second filled
        4. - - X - i.e. third filled
        5. - - - X i.e. fourth filled
        6. X - X - i.e. first and third filled
        7. X - - X i.e. first and fourth filled
        8. - X - X i.e. second and fourth filled  
    (b)
'''

def pebbling():
    print "Done Pebbling"
    

def main():
    pebbling()

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

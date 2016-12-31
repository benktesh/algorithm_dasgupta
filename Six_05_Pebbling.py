#Author: Benktesh
#benktesh1@gmail.com
#12/29/2017
#Dasgupta Solutions 6.5

import numpy as np
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
        0. - - - -  i.e. empty
        1. X - - - i.e. first filled rest empty
        2. - X - - i.e. second filled
        3. - - X - i.e. third filled
        4. - - - X i.e. fourth filled
        5. X - X - i.e. first and third filled
        6. X - - X i.e. first and fourth filled
        7. - X - X i.e. second and fourth filled  
    (b)
        There are two solutions here. First a recustive solution and second Dynammic programmign solutions.
    

    Setup:
        For this solution, there are some basic setups requirements.
        numOfPatterns = integer number of patterns. 

        CheckerBoard: Currently a 4 by N board with integert numberts. Initialize accordiningly

        Patterns: Array where a column represents valid pattern. A value of 1 incates location of pebble.


'''
numOfPatterns = 8
CheckerBoard = np.array([ [1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],  [0, 0, 0, 0, 0] ],  dtype=int)

rowCount = CheckerBoard.shape[0]
patterns = np.array([[0 for c in range(numOfPatterns)] for x in range(rowCount)])
patterns[0,1] = 1
patterns[1,2] = 1
patterns[2,3] = 1
patterns[3,4] = 1

patterns[0,5] = 1
patterns[2,5] = 1

patterns[1,6] = 1
patterns[3,6] = 1

patterns[3,7] = 1


def pebbling():
    print "Done Pebbling"
    
def patternsCompatible(P1, P2):
    if (P1==P2):
        return False
    P1 = patterns[:, P1]
    P2 = patterns[:, P2]
    x = P1 + P2
    return max(x) <= 1

def getSum(col, pat):
    ''' 
        Returns the sum of a column for a given pattern
        Arguements:
            column : 0 based index for column in CheckerBoard
            pattern: Pattern type. Zero based integer value i.e., 0, 1, 2, 3....
    '''
    return np.sum(np.multiply(patterns[:,pat], CheckerBoard[:, col]))
    
    
def getBest(col, p, result, checkCompatibility = True):
    '''
        Returns the best value of nth column for each of the patterns
        Arguements:
            col - O based index of the result array
            p - type of pattern. Not used when checkCommpatibility flag is set to False
            result - nd array stores the values at each column for each pattern. For
            example, result[i,j] corersponds to the the sum of ith column when 
            pattern j was applied into original CheckerBoard.
        Returns - integer best value for col column. 
    '''
    best = sys.maxint * -1
    for q in range(numOfPatterns):
        if (checkCompatibility == False or patternsCompatible(p, q)): #if p is < 0 do not check compatibity
            best = max(best, result[col, q])

            if (checkCompatibility == False):
                print "For pattern ", q , "result is ", best
    return best  
    
def pebblingDP(n,pp, optimal=False):
    '''
        This provides a DP based soluion to pebbling checkboard. 

    '''
    result = np.zeros((CheckerBoard.shape[1],numOfPatterns), dtype=int);
    for p in range(numOfPatterns): #initialize
        temp = getSum(0,p) 
        result[0, p] = temp    
    
    #loop through n columns
    for i in range(1, n+1):
        for p in range(0,numOfPatterns):        
            result[i, p] = getSum(i,p) + getBest(i-1, p, result) #get the best pattern for previous column.
    if (optimal == True):
        return getBest (col = n, p=0, result = result, checkCompatibility = False) #direct access to the result i.e. to get the best factor for nth column.
    else:
        #print result
        return result[n,pp]
        

def pebblingRecursive(column, pattern):
    '''
        This is a recursive method to solve the same problem as done via DP.
        Here the process starts at nth column and goes back to 0th column to reachh the base case.
        For each column, it recusively estimates the best value for each pattern.

        For example, when this method is called for Col = 4, and Pattern = 1.
        we have two compatible patterns:
        2,3. Thus the method calls 
        col=3,pattern=3
            col=2, pattern=1
                col=1, pattern=2
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=3
                    col=0, pattern=4
                col=1, pattern=3
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=2

            col=2, pattern=2
                col=1, pattern=1
                    col=0, pattern=0
                    col=0, pattern=2
                    col=0, pattern=3
                col=1, pattern=3
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=2                    
                col=1, pattern=4
                    col=0, pattern=0
                    col=0, pattern=2

        col=3, pattern=2
            col=2, pattern=1
                col=1, pattern=0
                    col=0, pattern=1
                    col=0, pattern=2
                    col=0, pattern=3
                    col=0, pattern=4
                col=1, pattern=2
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=3
                    col=0, pattern=4
                col=1, pattern=3
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=2 
            col=2, pattern=3    
                col=1, pattern=0
                    col=0, pattern=1
                    col=0, pattern=2
                    col=0, pattern=3
                    col=0, pattern=4
                col=1, pattern=1
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=3
                    col=0, pattern=4
                col=1, pattern=2     
                    col=0, pattern=0
                    col=0, pattern=1
                    col=0, pattern=3
                    col=0, pattern=4                
            col=2, pattern=4
                col=1, pattern=0
                col=1, pattern=2
        col=3,pattern=0
        .
        .


        ....
        
    '''
    if (column == 0):
        return getSum(0, pattern) #this is the base case as we reached the first column
    max = sys.maxint * -1
    for q in range(numOfPatterns):
        if(patternsCompatible(pattern, q)):
            temp = pebblingRecursive(column-1, q)
            if(temp > max):
                max = temp
    return getSum(column, pattern) + max    


def TestCompatiblePatterns():
    compat = "**\nPattern: Compatible patterns\n"
    for i in range(numOfPatterns):
        compat = compat + str(i) + " : "
        for j in range(numOfPatterns):
            if(patternsCompatible(i,j) and i != j):
                compat = compat + str(j) + " "
        compat = compat + "\n"
    compat = compat + "**\n"
    return compat  

def main():    


    print TestCompatiblePatterns()
    
    
    print "--- Recursive----"
    for i in range(numOfPatterns):
        print "Pattern = ", i , " Rsult", pebblingRecursive(4,i)
    print "--- DP ----"
    for idx in range(numOfPatterns):
        print "Pattern = ", idx, " Result", pebblingDP(4,idx)
    
    
    #etPattern(1)
    #pebblingRecursive(2,4)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

##Author: Benktesh
#benktesh1@gmail.com
#12/31/2016

import numpy as np



#Dasgupta Solutions for 6.9
'''
#   A certain string-processing language offers a primitive operation which splits a string into two
#   pieces. Since this operation involves copying the original string, it takes n units of time for a
#   string of length n, regardless of the location of the cut. Suppose, now, that you want to break a
#   string into many pieces. The order in which the breaks are made can affect the total running
#   time. For example, if you want to cut a 20-character string at positions 3 and 10, then making
#   the rst cut at position 3 incurs a total cost of 20 + 17 = 37, while doing position 10 rst has a
#   better cost of 20 + 10 = 30.
#   Give a dynamic programming algorithm that, given the locations of m cuts in a string of length
#   n, nds the minimum cost of breaking the string into m+ 1 pieces.


    Solution Description:
https://www.ocf.berkeley.edu/~wwu/cgi-bin/yabb/YaBB.cgi?board=riddles_cs;action=print;num=1217915168

    cuts = [1,4,6,8,9,10,72,100]
m = len(cuts) - 2 #two artificial 'cuts' were added

@memoize
def c(i,j): return cuts[j] - cuts[i] + min((c(i,k) + c(k,j)) for k in xrange(i+1,j))

print c(0,m+1)
 
'''
def splitString_(n, M):
    '''
        Split the string at locations specified in M
        Arguements: 
            M = list of numbmers where cut shuld take place. Integer.
            X = Number of characers in string. Integer.
        Returns Minimum Cost CutList.
    
    '''
    m = len(M)

    
    if (len(M) == 0):
        return M
    
    minCost = sys.maxint
    cost = np.array([[sys.maxint for x in range(m+2)] for x in range (m+2)])
    new_M = [0 for x in range(m+2)]
    new_M[0] = -1

    print cost
    for i in range(m):
        cost[i,i] = 0 
        cost[i,i+1] = 0 
        new_M[i+1] = M[i]

    new_M[m+1]=n-1
    print new_M
    for i in range(0, m+1):
        for i in range(m+1 - incr):
            j = i + incr
            minCost = sys.maxint
            firstCut = new_M[j] - new_M[i]
            
            for l in range(i+1, j):
                c = cost[i,l] + cost[l,j]
                if(c < minCost):
                    minCost = c
            if (minCost == sys.maxint):
                minCost = firstCut
            else:
                minCost = firstCut + minCost
            cost[i,j] = minCost
    print cost
    print new_M
    print cost[0,m+1]
    pass

    
    
def splitString(Y, n):
    '''
       Split the string at locations specified in M
        Arguements: 
            Y = list of numbmers where cut shuld take place. Integer.
            n = Number of characers in string. Integer.
        Returns Minimum Cost CutList.   

        M stores the minimum cost of splitinng the string 
    '''
    m = len(Y)
    Y.sort()
    n = 20
    
    M = np.array([[sys.maxint for x in range(m+2)] for x in range (m+2)])
  
 
    newY = [-1 for x in range(m+2)]
    newY[0] = 0
    for i in range(m):
        newY[i+1] = Y[i]
    newY[m+1] = n

    for i in range(m+2):
        M[i,i] = 0
    
    for i in range(m+1):
        M[i,i+1] = 0
    
    for incr in range(2, m+2):
        for i in range(m+2-incr):
            j = i + incr
            minCost = sys.maxint
            firstCut = abs(newY[j] - newY[i])

            for l in range(i+1, j):
                print "(incr,i+1, j, l)=({},{},{},{}), newY[j]={}, newY[i]={}".format(incr, i+1, j, l, newY[j], newY[i+1])
                cost = M[i,l] + M[l,j] #+ abs(newY[j] - newY[i+1])
                if(cost < minCost):
                    minCost = cost 
            if(minCost == sys.maxint):
                minCost = firstCut
            else:
                minCost = minCost + firstCut
            M[i,j] = minCost
    
    print M
    print "Min cost is ",  M[0,m+1] 
    return

    

def main():
    
    n = 20
    T = [10, 3]
    #print "Orginal String: {} \n".format(X)
    print splitString(T,n)
    #pattern()
    pass

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
##Author: Benktesh
#benktesh1@gmail.com
#1/3/2017

import numpy as np

'''
DPV 6.11

Given two strings x = x1x2    xn and y = y1y2    ym, we wish to nd the length of their longest
common subsequence, that is, the largest k for which there are indices i1 < i2 <    < ik and
j1 < j2 <    < jk with xi1xi2    xik = yj1yj2    yjk . Show how to do this in time O(mn).


Solution Approach:
A subsequence is a sequence that appears in the same relative order, and the sequence may not necessarily be contiguous. 
For example, OBAMA and OMBAMT are two strings. The LCS in this case is OBAM. 


Optimal Substructure:
Let the input strings be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. 
Let LCS(X, Y) be a function that returns the LCS.  

If the last characters of both X, Y are same, then LCS(..) = 1 + LCS(X[0...m-2], Y[0..n-1])

If the last character do not match, then LCS(...) we can either compare the strinng by next X or next Y which ever is bigger. 
Thus, LCS(...) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])

'''

def LongestCommonSubsequence(X,Y):
    m = len(X)
    n = len(Y)
    M = np.array([[None for x in range(n+1)] for x in range(m+1)])

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or 0 == j):
                M[i,j] = 0
            elif(X[i-1] == Y[j-1]):
                M[i,j] = 1 + M[i-1, j-1]
            else:
                M[i,j] = max(M[i, j-1], M[i-1, j])
           #print "(i, j) = ({},{}) X[i-1], Y[j-1] = {}, {}\n{}".format(i,j, X[i-1], Y[j-1], M)
                
    #print M
    return M[m,n]    

def main():
    x = "OBAMA"
    y = "BATM"
    print LongestCommonSubsequence(x,y)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
    Referece:
    http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
    https://www.youtube.com/watch?v=RhpTF26LyEc


'''
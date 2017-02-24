#Author: Benktesh
#benktesh1@gmail.com
#01/06/2017

import numpy as np

#Six_18 Coin Change

'''
Consider the following variation on the change-making problem (Exercise 6.17): you are given
denominations x1; x2; : : : ; xn, and you want to make change for a value v, but you are allowed to
use each denomination at most once. For instance, if the denominations are 1; 5; 10; 20, then you
can make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 but not for 40 (because you can't use 20
twice).

Input: Positive integers x1; x2; : : : ; xn; another integer v.
Output: Can you make change for v, using each denomination xi at most once?
Show how to solve this problem in time O(nv).

Solution Approach:
    To make the change for u with denomications 1 through i,:
    We can either:
        a. Use i coin or not
    
    If we use the ith coin, then we have to make change for u - xi
    using denomications 1 through i -1. 

    If we do not use the ith coin, then we have to make change for u 
    using denomication 1 throuuggh i -1. 

    Thus for i > 0, and j > 0,
    M[i,j] =    M[i-1, j] or M[i-1, j-xi]   if xi <= u 
                M[i-1, u]                   otherwise

'''   
def coin(X,V):
    n = len(X)
    M = np.array([[0 for j in range(V+1)] for i in range(n+1)])
    M[0,0] = 0
    for i in range(n):
        for j in range(V):
            if (X[i] == j):
                M[i,j] = 1
    for i in range(1,n+1):
        for j in range(V+1):
            if(X[i-1] <= j):
                M[i,j] = 1 if (M[i-1, j] == 1 or M[i-1, j-X[i]] == 1) else 0
            else: 
                M[i,j] = M[i-1, j]
                pass

    print M
    print np.max(M[:,V])
    
def main():
    x = [1, 5, 10, 20]
    V = 10
    coin(x, V)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
Reference:
    http://www.cis.syr.edu/~royer/09cis675/ans09.pdf

'''
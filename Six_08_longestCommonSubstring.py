##Author: Benktesh
#benktesh1@gmail.com
#12/29/2017

import numpy as np


#Dasgupta Solutions for 6.8


#    Given two strings x = x1x2    xn and y = y1y2    ym, we wish to nd the length of their longest
#    common substring, that is, the largest k for which there are indices i and j with xixi+1    xi+k-1 =
#    yjyj+1    yj+k-1. Show how to do this in time O(mn).

'''
    Solution Description:
    This problem has optimal substructure property.

    LCSSub(X_m, Y_n) = LCSSub(X_m-1, Y_n-1) + 1 if (X[m-1] == Y[n-1]) o Otherwise.

    The max length substring is 
    LCSSub(X_m, Y_n) = Max(LCSSub(X_i, Y_j) where 1 <= i,j <=m,n.  


'''
def LCS(X, Y):
    '''
        Table result stores lenght of common substrings. 
    '''
    result = np.array([[0 for x in range(len(Y)+1)] for x in range(len(X) + 1)], dtype=int)
    
    ending = 0 #stores the ending index of the max substrinng
    maxLength = 0 #stores the max lenght of the substring
  
    #We iterate over two strings and compare each character pairs.
    #For each substring match, we increase hte lenght of substring and fill the table
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if(X[i-1] == Y[j-1] ):
                result[i,j] = result[i-1, j-1] + 1
                if(result[i,j] > maxLength):
                    maxLength = result[i,j]
                    ending = i
    
    return maxLength,  X[ending-maxLength: ending]


def main():
    X = "OldSite:GeeksforGeeks.org";
    Y = "NewSite:GeeksQuiz.com";
    print "\nX: ", X, "\nY: " , Y
    r = LCS(X, Y)
    print "\nMax subsequence is '{}' and is {} character long ".format(r[1], r[0])


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
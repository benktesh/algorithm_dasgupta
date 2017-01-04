##Author: Benktesh
#benktesh1@gmail.com
#1/3/2017

import numpy as np

'''
DPV 6.12

You are given a convex polygon P on n vertices in the plane (specied by their x and y coordinates).
A triangulation of P is a collection of n - 3 diagonals of P such that no two diagonals
intersect (except possibly at their endpoints). Notice that a triangulation splits the polygon's
interior into n - 2 disjoint triangles. The cost of a triangulation is the sum of the lengths of the
diagonals in it. Give an efcient algorithm for nding a triangulation of minimum cost. (Hint:
Label the vertices of P by 1; : : : ; n, starting from an arbitrary vertex and walking clockwise. For
1  i < j  n, let the subproblem A(i; j) denote the minimum cost triangulation of the polygon
spanned by vertices i; i + 1; : : : ; j.)

Solution approach:
The problem is similar to matrix chain multiplications.

Where the recurence relations is as below:
M[i,j] = min_i<=k<=j(M[i,k] + M[k,j] + distance_ik + distance_jk) for M[i,j] min cost of triangulation of polygon spanned by verticies i, j

'''

def distance(i, j, X, Y):    
   
    x1 = X[i]
    y1 = Y[i]

    x2 = X[j]
    y2 = Y[j] 
    d=  ((x1-x2) ** 2 + (y1-y2) **2)**0.5
    #print d
    return d

def convexPolygon(X,Y):
    '''
        Arguements:
            X,Y contain the x- and y- coordiante locations of verticies in clock wise direction.
    '''
    n = len(Y)
    if(n < 3): #there must be at least 3 points.
        return 0
    #M[i,j] stores minimum cost by veritices i, i+1, ..j
    M = np.array([[9999 for x in range(n)] for x in range(n)], dtype=float)

    for i in range(n):
        M[i,i] = 0
        
        
    
    for s in range(n):
       for i  in range( n-s):
            j = i + s; 
            
            #print "     i, j : {} {}".format(i, j)
            if (j < i + 2):
                M[i,j] = 0;
            else:
                M[i,j] = sys.maxint

                for k in range(i+1, j):
                    c = M[i,k] + M[k,j] + distance(i, k, X, Y) + distance(k, j, X, Y) 
                    if (c < M[i,j]):
                        M[i,j] = c
        
    return M[0,n-1]    

def main():
    x= [0, 1, 2, 1, 0]
    y= [0, 0, 1, 2, 2]
    print convexPolygon(x,y)

    

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
    Referece:
    http://users.eecs.northwestern.edu/~dda902/336/hw6-sol.pdf



'''
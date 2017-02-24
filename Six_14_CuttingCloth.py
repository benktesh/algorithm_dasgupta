#Author: Benktesh
#benktesh1@gmail.com
#01/05/2017

import numpy as np

#Six_14_Cutting_Cloths

'''
Cutting cloth. You are given a rectangular piece of cloth with dimensions X  Y , where X and
Y are positive integers, and a list of n products that can be made using the cloth. For each
product i 2 [1; n] you know that a rectangle of cloth of dimensions ai  bi is needed and that the
nal selling price of the product is ci. Assume the ai, bi, and ci are all positive integers. You
have a machine that can cut any rectangular piece of cloth into two pieces either horizontally or
vertically. Design an algorithm that determines the best return on the X Y piece of cloth, that
is, a strategy for cutting the cloth so that the products made from the resulting pieces give the
maximum sum of selling prices. You are free to make as many copies of a given product as you
wish, or none if desired.

'''
def getValue(x, y, X, Y, P):
    if (x in X and y in Y):
        return 1
    return 0


def cuttingCloth():
    '''
        Arguements:
            M: integer, X dimension of Cloth
            N: integer, Y dimension of Cloth
            X: Xi of pieces, pi
            Y: Yi of pieces, pi
            P: Value of pieces, pi
    '''
    x = 5
    y = 5
    Xi = [1,  3]
    Yi = [1,  3]
    Ci = [1, 25]
    n = len(Xi)
   # V = np.array([[0 for j in range(x+1)]for i in range(x+1)]) # stores maximum price that can be obtained from i x j dimension of cloth
    
    V = np.array([[0 for j in range(y+1)] for i in range(x+1)]) #stores the price of i,j dimensions. Returns 0 otherwise.
    for i in range(n):  
        xi = Xi[i]
        yi = Yi[i]
        V[xi, yi] = Ci[i] 
    print V
    for i in range(1,x):
        for j in range(1, y):
            temp = 0
            for p in range(n): 
                xi = Xi[p]
                yi = Yi[p]
                
                if(p < i):                    
                    temp = max(temp, V[xi, j]+V[i-xi, j], V[i,j])
                print "xi, yi", xi , " , ", yi , ", val= ", temp
                if (p < j):
                    temp = max(temp, V[i, j-yi]+V[i, yi], V[i,j])
            V[i,j]  = max(temp, V[i,j])



    #print priceLookup; 
    print V
    print "result " ,V[x-1,y-1]


   
   
    


def main():
    
    cuttingCloth()
    
    pass

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
Reference:

'''
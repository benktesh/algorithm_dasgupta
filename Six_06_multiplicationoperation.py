##Author: Benktesh
#benktesh1@gmail.com
#12/29/2017
#Dasgupta Solutions 6.6

#Some resources:
#   http://web.cs.wpi.edu/~sms/cs584/Problems9.pdf
#   

import numpy as np

def getOperations(x,y):
    '''
        This implements the multiplicaiton table. 
        Arguements:
            X, first string
            Y, second string
        Returns final string as a result of multiplicaiton of x, and y.

    '''
    if (x == 'a'):
        if (y == 'a'):
            return 'b'            
        elif (y == 'b'):
            return 'b'        
        elif (y == 'c'):
            return 'a'
     
    elif (x == 'b'):
        if (y == 'a'):
            return 'c'                
        elif (y == 'b'):
            return 'b'        
        elif (y == 'c'):
            return 'a'
        
    elif (x == 'c'):
        if (y == 'a'):
            return 'a'                
        elif (y == 'b'):
            return 'c'        
        elif (y == 'c'):
            return 'c'

def TestMultTable():
    
    t = getOperations('a','b')
    print t == 'b';

    t = getOperations('b','a')
    print t == 'c';

    t = getOperations('c','c')
    print t == 'c';
    
def multiplicativeOperation(A, a):
    
    '''
        Computes if stringg contains in A can be multiplied to result into a.
        Uses 'getOperations(x,y)' for multiplication.
        returns True if A can be made to a and False otherwise.

    '''
    
    A = list(A)
    n = len(A)
    result = np.array([['' for x in range(n)] for x in range(n)] )
    

    #initialize the result array to have i,i = A[i]. This would be the base case in recursive formulation as multiplication of 1
    #element is same element.
    #Thre result array lists the result of multiplication on a two dimentional array.
    for i in range(n):
        result[i,i] = A[i]
    
    #Suboptimal strcuture is 
    #We look at the the elements one at a time. We can ignonre the buttom half of the traingle. 
    #Iterating from first to last character as outer array
    #Iterature till from first element to n-s elements (i.e., we like ot go fromm 1 <= i <= j <= n)

    for i in range(1, n):
        for j in range(n-i):
            for k in range(j, j+i):
                N = result[j,k]
                B = result[k+1, j+i]
                result[j, j+i] = result[j, j+i] + getOperations(N,B)
                print result
    return result[0,n-1] == a

def main():
    #TestMultTable()
    print "Result ", multiplicativeOperation("bbbba", "a")

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

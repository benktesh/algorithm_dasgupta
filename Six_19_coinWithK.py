

'''
6.19. Here is yet another variation on the change-making problem (Exercise 6.17).
Given an unlimited supply of coins of denominations x1; x2; : : : ; xn, we wish to make change for
a value v using at most k coins; that is, we wish to nd a set of  k coins whose total value is v.
This might not be possible: for instance, if the denominations are 5 and 10 and k = 6, then we
can make change for 55 but not for 65. Give an efcient dynamic-programming algorithm for the
following problem.
Input: x1; : : : ; xn; k; v.
Question: Is it possible to make change for v using at most k coins, of denominations
x1; : : : ; xn?
'''
# m is size of coins array (number of different coins)
def minCoins(coins,V, k):

    '''
        M[i] stores minimum number of coins for a value.
        This table is initilized with max int initially.
        First element of this table is initilized to 0 to indiate that
        value of 0 will have '0' minimum coins.

        For each values in V i.e., 1 to V, we will computer the minimum coins
        required.

        The inner loop will iterature throught each of the available coins for a value in 1 to V
        and find the minimum number of coins required to make the change.
        If the jth coin is larger than vi, we can ignore that coin.  
        

        
    '''
    M = [sys.maxint for x in range(V+1)]
    M[0] = 0
    m = len(coins)
    for i in range(1, V+1):
        for j in range(m):
            if(coins[j] <= i):
                sub = M[i - coins[j]]
                #print M
                if(sub != sys.maxint and sub + 1 < M[i]):
                    M[i] = sub+1
                #else:
                #    print "Either sub is maxint or M[i] > sub + 1 ", M[i]
            #else:
                #print 'skipping', coins[j], " for v = ", i
                    
    
    
    print M
    return M[V]


   
 
 

def  main(): 
    coins =  [9, 6, 5, 1];
    k = 3
    V = 11;
    print "Is possible ?  ", minCoins(coins, V, k);
    


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


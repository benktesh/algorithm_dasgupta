#Auther - Benktesh 
#Contact: benktesh1@gmail.com
#Some programming exercises from Dasgupta book
#6.1
def maxSubArraySum(A):
    l = len(A)
    maxSoFar = A[0]
    currMax = A[0]
    starts = 0
    ends = 0
    for i in range(1, l):
        currMax = max(A[i], currMax + A[i])
        maxSoFar = max(maxSoFar, currMax)

        
        if A[i] >= currMax:
            starts = i
        if(currMax >= maxSoFar):
            ends = i

    subsequence = ", ".join(str(x) for x in A[starts:ends+1]);  
    return subsequence, maxSoFar
def Hotel(A):
    l = len(A)
    penalty = [[0 for i in range (l)] for j in range (l)]
    hotels = [-1 for x in range(l)]
    print hotels
    print penalty
    print "is not complete"

        
#http://users.eecs.northwestern.edu/~dda902/336/hw6-sol.pdf
def Profit(N, P, K):
    l = len(N);
    profit = [0 for x in range(l)]
    alpha = [[0 for i in range (l)] for x in range(l)]
    '''
        alpha stores the constraint mi - mj < k. Thus for each pair of locations i,j
        alpha i,j provides a lookup if the absolaute distance between location i and j
        are greater than equal to or less than k. If the distannce is greater than or equal to k, then
        the value is 1 else it is 0.  
    '''
    for i in range(l):
        for j in range(l):
            if(abs(N[i] - N[j]) >= K):
                alpha[i][j] = 1
            
    '''
    profit[i]: stores the maximum profit at locatio i. The maximum profit is expected profit at location i 
    and includes profit from previous location that satisfy the distance constraint given by alpha[i][j]

    Thus,
    profit[i] = max(max_j < i {profit[j] + alpha[i][j] * P[i]}, pi)

    Sicne we do not need to start at first restaurant, we will start an outer loop to keep track of 
    restaurant's profits. 

    The inner loop will be there for us to iterate from the first restaurant to the ith restraurant in the outerloop.
    Within the inner loop, we attempt to maximize the profit by the following strategy:
        Calculate profit as: profit[j] + expected profit at[i] if restaurant exists.
        If this profit is > than Profit[i] then update the profit. Try next iteration.
        Finally, check if profit < P[i], if that is the case then replace the profit.
        
    '''
    
    for i in range (0,l):        
        for j in range (i):
            temp = profit[j] + alpha[i][j] * P[i]
            if(temp > profit[i]):
                profit[i] = temp
        if profit[i] < P[i]:
            profit[i] = P[i]
    #for i in range(l):
    #    print [val for val in alpha[i]] 
    
    
    #Selected Locations are the ones that are stricting increasing in profits
    temp = [0 for x in range(l)]
    for i in range(l):
        temp[i] = profit[i] - P[i]
       
    locations = [0]
    for i in range(1,l):
        if(temp[i] > temp[i-1]):
            locations.append(i)
        
    #print [val for val in profit] 
    #print [val for val in temp] 
    print "Locations", [val for val in locations]
    return profit[l-1] 

def main():
    #6.1
    One = False
    Two = False
    Three = True

    if(Three):
        N = [10, 20, 25, 30, 40] 
        P =  [100, 101, 102, 110, 120]
        #Profit(N,P,10)

        #TestFrom a resource http://cseweb.ucsd.edu/~dasgupta/101/sol7.pdf
        N = [10, 20, 25, 30, 40] 
        P =  [100, 100, 101, 100, 100]
        print "Profit ", Profit(N,P,10)
        #Selectd locations are 0 , 1, 3, and 4 with total profit of 400
    if(Two):
        a = [10, 100, 200, 300, 400]  
        print "Hotel Problem", Hotel(a)
    
    if(One):
        a = [-2, -3, 4, -1, -2, 1, 5, -3]
        print"Maximum contiguous elements are " , maxSubArraySum(a)[0], " sum is ",  maxSubArraySum(a)[1] 

        a = [5, 15, -30, 10, -5, 40, 10]
        print"Maximum contiguous elements are " , maxSubArraySum(a)[0], " sum is ", maxSubArraySum(a)[1]

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
import time

### Fibnacchi by recustion
def fibRecursion(n):
    if(n-1 <= 1):
        return n-1;
    return fibRecursion(n-1) + fibRecursion(n-2)

def fibDynamic(n):
    F = [0 for x in range(n)]
    F[0] = 0
    F[1] = 1
    for i in range (2, n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]


def contiguousSubsequence(A):
    n = len(A)
    if(n == 0):
        return []

    #initially the result (a list of list of subsequences contains element i)
    result = [[A[y]] for y in range(n)]
    
    for i in range (1, n):
        for j in range (0, i):
            
            pass
    #result = []
    return result

def knapSack(W, w, v, n):
    '''
        Time Complexity is 2^n
    '''
    if (n==0 or W == 0):
        return 0
    
    if(w[n-1] > W):
        return knapSack(W, w, v, n-1)
    else:
        return max(v[n-1] + knapSack(W- w[n-1], w, v, n-1), knapSack(W, w, v, n-1))
def knapSackDP(W, w, v, n):
    K = [[0 for x in range(W+1)] for x in range (n+1)]

    for i in range(n+1):
        for j in range (W+1):
            if(i==0 or w == j):
                K[i][j] = 0
            elif w[i-1] <= j:
                K[i][j] = max(v[i-1] + K[i-1][j -w[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j] 
    print K
    return K[n][W]


def bubbleSort(Arr):
    n = len(Arr)
    for i in range(n):
        
        for j in range(0, n-i-1):
            print "i = {} and => {}".format(i, Arr)
            if(Arr[j] > Arr[j+1]):
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
    

def insertionSort(arr):
     
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key    
    
def main():
    #str = "ABCDEFGHIJKL"
    #visited = [-1] * 256
    
    #print visited

    #for i in range(len(str)):
        #print ord(str[i])
        #visited[ord(str[i])] = i
    #print visited
    #sys.exit(0)
    #nth = 50
    #start_time = time.time()
    #print "Fib By Recursion", fibRecursion(nth)
    #print (time.time() - start_time)

    #start_time = time.time()
    #print "Fib By Dynamic", fibDynamic(nth)
    #print (time.time() - start_time)
    pass
    #A = [5, 15, -30, 10, -5, 40, 10]
    #print contiguousSubsequence(A)
    pass

    #drive for recursive knapsack program
    if(False):
        v  = [60, 100, 120]
        w = [10, 20, 30]
        W = 50
        print knapSackDP(W, w, v, len(w))
    
    BubbleSort = True
    if(BubbleSort):
        Arr = [64, 34, 25, 12, 22, 11, 90]
        bubbleSort(Arr)
        for i in range(len(Arr)):
            print "{}".format(Arr[i])

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

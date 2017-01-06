##Author: Benktesh
#benktesh1@gmail.com
#01/03/2017

import numpy as np

'''
Counting heads. Given integers n and k, along with p1; : : : ; pn 2 [0; 1], you want to determine the
probability of obtaining exactly k heads when n biased coins are tossed independently at random,
where pi is the probability that the ith coin comes up heads. Give an O(n2) algorithm for this
task.2 Assume you can multiply and add two numbers in [0; 1] in O(1) time.

Solution Approach:

#http://stackoverflow.com/questions/13099766/counting-heads-dynamic-programming
Consider the situation when (n-1) coins are tossed together and nth coin is tossed apart and take into account mutual independence.

Combine probabilities of simpler cases to get P(1..n, k) (where P(1..n, k) is the probability of obtaining exactly k heads when n coins)

Then apply this rule and fill all the cells in NxK table

Edit:

There are two possible ways to get exactly k heads with n coins - 

a) if (n-1) coins have k heads, and Nth coin is tail, and

b) if (n-1) coins have k-1 heads, and Nth coin is head

so

P(n, k) = P(n-1, k) * (1 - p[n]) + P(n-1, k-1) * p[n] 



'''
def countingHead(k, P):
    '''
        Returns probability of k head from n biased coins where probability of coins are given in P.

        Arguements:
            n = number of coins
            k = number of heads
            P = prbability of getting head for coins, i.e., p0 p1 p2 p2.... pn-1


            
#http://www.cforcoding.com/2010/08/coin-tosses-binomials-and-dynamic.html
private static void runDynamic() {


02.


long start = System.nanoTime();


03.


double[] probs = dynamic(0.2, 0.3, 0.4);


04.


long end = System.nanoTime();


05.


int total = 0;


06.


for (int i = 0; i < probs.length; i++) {


07.


System.out.printf("%d : %,.4f%n", i, probs[i]);


08.


}


09.


System.out.printf("%nDynamic ran for %d coinsin %,.3f ms%n%n",


10.


coins.length, (end - start) / 1000000d);


11.


}


12.


 


13.


private static double[] dynamic(double... coins) {


14.


double[][] table = new double[coins.length + 2][];


15.


for (int i = 0; i < table.length; i++) {


16.


table[i] = new double[coins.length + 1];


17.


}


18.


table[1][coins.length] = 1.0d; // everything else is 0.0


19.


for (int i = 0; i <= coins.length; i++) {


20.


for (int j = coins.length - 1; j >= 0; j--) {


21.


table[i + 1][j] = coins[j] * table[i][j + 1] +


22.


(1 - coins[j]) * table[i + 1][j + 1];


23.


}


24.


}


25.


double[] ret = new double[coins.length + 1];


26.


for (int i = 0; i < ret.length; i++) {


27.


ret[i] = table[i + 1][0];


28.


}


29.


return ret;


30.


}

    '''
    n = len(P)
    M = np.array([[0 for x in range(k)] for x in range(n)])
    print M
    print "Counting Head Completed k = {} n = {} P = {}".format(k, n, P)

def main():
    kHead = 5
    P = [0.2, 0.3, 0.4]
    countingHead(kHead, P)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
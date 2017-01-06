# coding: utf-8
#Author: Benktesh
#benktesh1@gmail.com
#1/5/2017


import numpy as np

'''
DPV 6.15. 
Suppose two teams, A and B, are playing a match to see who is the rst to win n games (for some
particular n). We can suppose that A and B are equally competent, so each has a 50% chance
of winning any particular game. Suppose they have already played i + j games, of which A has
won i and B has won j. Give an efficient algorithm to compute the probability that A will go on
to win the match. For example, if i = n-1 and j = n-3 then the probability that A will win the
match is 7=8, since it must win any of the next three games.

Solution/Solution approach:

Example:
Lets say it needs 8 wins to win the game. Team A has won 7 games, and Team B has won 5 games. 
Thus, i = n - 1 => 7
and j = n - 3 => 5
And Team(8, 7, 5) should be 7/8.


Subproblem - P(i,j) is subproblem for 1 <= i, j <= n for the probability of A to first win the 
n games, given A has won i games and B has won j games. 

At the beginning, for all P(i,j) = 1 where i == 0 and j > 0, the probability of win is 1 for A has won.
Likewise, for all P(i,j) = 0 where i > 0 and j == 1, the probaility of win is 0 for A as B has won.

For rest of the P(i,j), the probability is obtained by adding the probabitiy of A's winning at A(i,j+1) and A(i+1, j) and increasing 
order of i + j using:
    P[i,j] = 1/2(P[i,j+1] + P[i+1, j])

Here 1/2 is the probability of A's winning at n-i which is same for  all n.

The above equestion is derived from:
    P[i,j] = p(n-i) * P[i,j+1] + (1- p(n-1)*P[i+1, j])
'''
 
def Team(n, I, J):
    '''
        Arguements:
        -----------
        n: integer - Number of wins needed to win the game.
        I: integer - Number of games won so far by team A.
        J: integer - Number of games won so far by team B. 

        Returns:
        ---------
        float: probability of winning the tournament when team has won i games,
            lost j games, and it required n wins to win the tournament.
    
    '''
    if (I > 8 or J > 8 or n == 0):
        return 0
    P = np.array([[0.0 for y in range(n+1)] for x in range(n+1)], dtype=float)
    for i in range(0, n):
        for j in range(0, n):
            temp = 0
            if(i == 0 and j > 0):
                temp = 1
            elif( i > 0 and j == 0):
                temp = 0
            elif(i > 0 and j > 0):
                temp = (P[i-1, j] + P[i,j-1])/2.0
            P[i,j] = temp
    print "Probability Table \n", np.around(P, 4)
    return P[n-I,n-J]    
    
def main():    
    print Team(8, 7, 5)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
    Proof:
    ---------
    We consifer P

    Referece:
    ---------
  
    http://www.cse.scu.edu/~mwang2/algorithm/Dynam10.pdf
    http://www.studfiles.ru/preview/2874532/page:47/
    http://orion.lcg.ufrj.br/Dr.Dobbs/books/book9/mf1210.htm



'''
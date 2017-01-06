# coding: utf-8
#Author: Benktesh
#benktesh1@gmail.com
#1/4/2017


import numpy as np

'''
DPV 6.13. 
Consider the following game. A dealer produces a sequence s1..sn of cards, face up, where
 each card si has a value vi. Then two players take turns picking a card from the sequence, 
but can only pick the first or the last card of the (remaining) sequence. The goal is to collect 
cards of largest total value. (For example, you can think of the cards as bills of different denominations.) 
Assume n is even.
    (a) Show a sequence of cards such that it is not optimal for the first player to start by picking
        up the available card of larger value. That is, the natural greedy strategy is suboptimal.
    (b) Give an O(n2) algorithm to compute an optimal strategy for the first player. Given the
        initial sequence, your algorithm should precompute in O(n2) time some information, and
        then the rst player should be able to make each move optimally in O(1) time by looking
        up the precomputed information.

Solution/Solution approach:
(a) Lets take an example sequence 10, 100, 1, 1. Here if the first player selects 10 (comparing 1 and 10) then The second player 
    will select 100 and win. Instead, if the first player selects the last card of value 1, then the second player will choose
    either 10 or 1 and first player will be able to select 100 to win.

(b)


'''

def cardGame(S):
    '''
        Arguements:
           
    '''
    n = len(S)
    M = np.array([[0 for x in range(n)]for x in range(n)])
    for i in range(n):
        M[i,i] = S[i]
    print M
    for i in range(n):
        for j in range(n, 0, -1):
            pass


def main():
    s= [10, 100, 1, 1]
    
    print cardGame(s)

    

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))


'''
    Referece:
    https://web.cs.dal.ca/~whidden/CS3110/assignments/a8_solution.pdf
    http://vlsicad.ucsd.edu/courses/cse101-w16/hw/hw4_solutions.pdf
    https://www.cs.bgu.ac.il/~michaluz/seminar/Dynamic_programming_and_board_games.pdf
    




'''
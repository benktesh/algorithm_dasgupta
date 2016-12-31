##Author: Benktesh
#benktesh1@gmail.com
#12/29/2017
#Dasgupta Solutions 6.7

#https://sites.google.com/site/indy256/problems/longest_palindrome

import numpy as np

    
def lonestPalidrome(A):
    
    '''
       Finds and returns the longest palindromic subsequence using Dynamic Programming
       maxLength and begins are integer variables which respectively store the lenght of max substring
       and starting position of the max substring. 
    '''
    
    A = list(A)
    n = len(A)
    if(n == 0):
        return False; 
    result = np.array([[0 for x in range(n)] for x in range(n)] )
    #initilize this result array by setting the diagonol to '1' indicating that the
    #one character is palidromic subseuqnce

    for i in range(n): 
        result[i,i] = 1
    maxLength = 1 #default max lenght is 1
    current = A[0] # anycharacer is a valid subsequence
    begins = 0

    for i in range(0, n-1): #checks if two consecutive characters forms palidromes  
        if(A[i] == A[i+1]):
            result[i,i+1] = 1
            maxLength= 2
            begins = i
    
    #This loops check all the three characters and more.
    #The idea is fist we check if three characters form palindrome. For a three characer to be palidrome
    #the first and last chracters should match. Once all the three chracters are done, 
    #We check for four characters and five characters and so one.  
    #While we are checkking more cahracers, we are budiling the table that stores if chekeced charactersa are palindroming. For 
    #example, for three characters, all we need to check are first and last characetrs. Like wise for four characters are palidromic
    #if first and last characters are palindome and the inside chracers (between secondd and second lasts)
    #are palidrome (this shuld have been in our result table fromm previous iterations.)

    for k in range(3, n): #start with 3
        for i in range(n-k+1): # row for result. The iteration start to loop from 0 column to third column in string
            j = i+k-1           #column for result
            if(A[i] == A[j] and result[i+1, j-1] == 1): #firs and last characters match and previous (smaller unit) is palidrome
                result[i,j] = 1
                begins = i      #store the beginning of the characers
                maxLength = k   #store the length of the substring
            print "\n i,j", i, " ", j, " = ", A[i], " " , A[j]
    
    substring = A[begins:maxLength+begins]
    return "".join(substring)
    


def main():
    string = "bananas"
    print "Result for bananas:          ", lonestPalidrome(string)
    #print "Result for forgeeksskeegfor: ", lonestPalidrome("forgeeksskeegfor")

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

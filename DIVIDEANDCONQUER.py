
import math
def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def minDBruteForce(P):
    '''
        Array of point coordinates
    '''
    mind = sys.maxint
    n = len(P)

    for i in range(n):
        for j in range(i+1, n):
            d = dist(P[i], P[j])
            if(d < mind):
                mind = d
    return mind


def main():
    print '123z'.isdigit()
    print (int('123a'))
    P = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    print minDBruteForce(P)
    pass

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
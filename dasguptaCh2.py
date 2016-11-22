import locale

subscript = 10
printDebug = 'True'
called = 0

def leftRightBit(x, k):
    x = str(x)
    xl = x[:k].rjust(k,'0')
    xr = x[-k:].rjust(k, '0')
    if(printDebug == 'True'):
        print "k={},x={}=>{},{}".format(k, x, xl, xr)
    return xl, xr

def multiply(x,y):
    '''
    Input: positive integers x and y. A separate global function must be specified to define the number type. 
    For decimal use 10, for binary use 2 for global variable subscript
    output: their products as string
    '''
    global called
    global subscript    
    global printDebug
    called = called + 1 #keeps track of how many times this function is called
   
    n = max(len(str(x)), len(str(y)))
    x = str(x).rjust(n, '0')
    y = str(y).rjust(n, '0')
    if (n == 1):
        
        result = str(int(x) * int(y)).rjust(2*n,'0')
        if(printDebug == 'True'):
            print "n={}: {} * {} = {}".format(n, x, y, result)
        return result

    xL, xR = leftRightBit(x, n/2)
    yL, yR = leftRightBit(y, n/2)

    p1 = multiply(xL, yL)
    p2 = multiply(xR, yR)
    p3 = multiply(str(int(xL) + int(xR)), str(int(yL) +int(yR)))
    
    temp = str(int(p1) * pow(subscript,n) + (int(p3) - int(p1) - int(p2)) * pow(subscript, n/2) + int(p2))
    if(printDebug == 'True'):
        print "Returns p1={}, p2={}, p3={}, n={}, result={}".format(p1, p2, p3, n, temp)
    return temp
    

def main():
    global subscript
    global printDebug
    global called

    subscript = 10                      #global variable to identiy the number type. For example, 2 for binary and 10 for decimal
    printDebug = "False"                #Controls if debug msg can be printed
    
    result = (multiply('1980', '2315')

    print "Result = {:,} found after {:,} recursive calls".format(int(result), called) 
    

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
import sys
sys.path.append('Coursework/521_Computer_Architecture/Class6')

from bcpu import *
from multi1 import mulasm

def mulpy(r1, r2)->r3:
    r3 = 0 
    while r2 != 0:
        r3 += r1
        r2 -= 1
    return r3

# testing
if __name__ == '__main__': # put all your testing code in main()
    
    ## test case 1
    tot = 0
    testin1 = 2
    testin2 = 3
    
    # python output
    outpy = mulpy(testin1, testin2) #python output
    
    # assembly output
    setr(r1, testin1)
    setr(r2, testin2) 
    startfast(mulasm) #assembly function
    outasm = getr(r3) #OS function getr and put it in python
    
    # compare assembly to python
    print("\nWorking: ", outpy == outasm)
    tot = (tot+1) if outpy == outasm else tot # if out python == out assembly, increase total, else don't.
    print("\nTest Case 1\n Input 1 = {}\n Input 2 = {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testin1, testin2, outpy, outasm, tot))

    ## test case 2
    testin1 = 2
    testin2 = 0
    
    # python output
    outpy = mulpy(testin1, testin2) #python output
    
    # assembly output
    setr(r1, testin1)
    setr(r2, testin2) 
    startfast(mulasm) #assembly function
    outasm = getr(r3) #OS function getr and put it in python
    
    # compare assembly to python
    print("\nWorking: ", outpy == outasm)
    tot = (tot+1) if outpy == outasm else tot # if out python == out assembly, increase total, else don't.
    print("\nTest Case 1\n Input 1 = {}\n Input 2 = {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testin1, testin2, outpy, outasm, tot))
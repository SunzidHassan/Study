import sys
sys.path.append('Coursework/521_Computer_Architecture/Class5')

from bcpu import *

R1 = 0
R2 = 0
# python function
def Abs(inx:r1)->r2:
    outy:r2 = inx
    if inx < 0:
        outy = -inx
    return outy # asm will get the return value from r2

# assembly function
from testq1 import absf

# testing assembly to python
if __name__ == '__main__': # put all your testing code in main()
    
    ## test case 1
    tot = 0
    testcase = -5
    
    # python output
    outp = Abs(testcase) #python output
    
    # assembly output
    setr(r1, testcase) # r1 = testcase
    start(absf) #assembly function
    outa = getr(r2) #OS function getr and put it in python
    
    # compare assembly to python
    print("\nTest Case 1: {}\nPython out: {}\nAssembly out{}\nTest Grade: {}\n".format(testcase, outp, outa, tot))
    tot = (tot+1) if outp == outa else tot # if out python == out assembly, increase total, else don't.
    
    ## test case 2
    testcase = 5
    outp = Abs(testcase)
    
    # assembly output
    setr(R1, testcase)
    start(absf)
    outa = getr(r2) #OS function getr and put it in python
    
    # compare assembly to python
    tot = (tot+1) if outp == outa else tot
    print("\nTest Case 2: {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testcase, outp, outa, tot))
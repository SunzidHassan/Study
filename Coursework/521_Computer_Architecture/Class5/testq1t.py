from bcpu import *

def Abs(inx:r1)->r2:
    outy:r2 = inx
    if inx < 0:
        outy = -inx
    return outy # asm will get the return value from r2

from testq1 import absf

# testing
if __name__ == '__main__':
    # put all your testing code here
    tot = 0
    testcase = -5
    outp = Abs(testcase)
    print("py our: ", outp)
    setr(r1, testcase)
    start(absf)
    # printr(r2)
    outa = getr(r2) #OS function getr and put it in python
    print("asm out:", outa)
    tot = (tot+5) if outp == outa else tot
    
    testcase = 5
    outp = Abs(testcase)
    print("py our: ", outp)
    setr(r1, testcase)
    start(absf)
    # printr(r2)
    outa = getr(r2) #OS function getr and put it in python
    print("asm out:", outa)
    tot = (tot+5) if outp == outa else tot
    
    print("test grade: ", tot)
    
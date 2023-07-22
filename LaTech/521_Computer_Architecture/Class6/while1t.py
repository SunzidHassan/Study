from bcpu import *

def whileloop(inx:r1)->r2:      # pass by reference :r1, :r2
    outy:r2 = 0                 # initialize output = 0
    while inx >= 0:
        outy = outy + 2
        inx = inx - 1           # decreases to 0
    return outy

from while1 import whileloopf

# testing
if __name__ == '__main__': # put all your testing code in main()
    
    ## test case 1
    tot = 0
    testcase = 2
    
    # python output
    outp = whileloop(testcase) #python output
    
    # assembly output
    setr(r1, testcase) # r1 = testcase
    startfast(whileloopf) #assembly function
    outa = getr(r2) #OS function getr and put it in python
    
    # compare assembly to python
    tot = (tot+5) if outp == outa else tot # if out python == out assembly, increase total, else don't.
    print("\nWorking: ", outp == outa)
    print("\nTest Case 1: {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testcase, outp, outa, tot))

    ## test case 2
    tot = 0
    testcase = -1
    
    # python output
    outp = whileloop(testcase) #python output
    
    # assembly output
    setr(r1, testcase) # r1 = testcase
    startfast(whileloopf) #assembly function
    outa = getr(r2) #OS function getr and put it in python
    
    # compare assembly to python
    tot = (tot+5) if outp == outa else tot # if out python == out assembly, increase total, else don't.
    print("\nWorking: ", outp == outa)
    print("\nTest Case 1: {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testcase, outp, outa, tot))


    ## test case 0
    tot = 0
    testcase = 0
    
    # python output
    outp = whileloop(testcase) #python output
    
    # assembly output
    setr(r1, testcase) # r1 = testcase
    startfast(whileloopf) #assembly function
    outa = getr(r2) #OS function getr and put it in python
    
    # compare assembly to python
    tot = (tot+5) if outp == outa else tot # if out python == out assembly, increase total, else don't.
    print("\nWorking: ", outp == outa)
    print("\nTest Case 1: {}\nPython out: {}\nAssembly out: {}\nTest Grade: {}\n".format(testcase, outp, outa, tot))

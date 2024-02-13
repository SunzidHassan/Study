myTechEmail = 'sha040' #omit @latech.edu

# 15 points

from bcpu import * 

def l2l(L:'Laddr:r1, lenL:r2'):
    # in ASM l2l(Laddr:r1, lenL:r2) is used instead of l2l(L)
    # Laddr, lenL will be used in ASM to pass L
    # pass by reference
    # calling program will put Laddr into r1, lenL into r2
    
    i = 0
    Laddr = 0
    lenL = len(L)
    temp = 0
    
    # L = [n+n for n in L]
    
    while i<lenL:
        temp = L[Laddr]
        temp = temp * 2
        L[Laddr] = temp
        Laddr += 1
        i += 1

    return L # calling program will get L for info in r1 and r2
    # no need to translate the return (in-place passing)

# put all the require asm code inside this string
# only the code needed for the about function should be included
# make sure to use #> l2l(L:'Laddr:r1, lenL:r2'): as the first line of the code
ExQ3 = f"""
#> l2l(L:'Laddr:r1, lenL:r2'):
    #:Laddr = r1
    #:lenL = r2
    #:i = r3
    #:temp = r4

    Set(i, 0)
    Set(temp, 0)

    #>while i<lenL:
    #:a_=i
    #:b_=lenL
    #:end_=endwhile
    {a_lt_b_}

        Add(ar, Laddr, i)
        Load(temp, ar)              # temp = L[Laddr]
        Add(temp, temp, temp)       # temp = temp + temp
        Store(ar, temp)             # L[Laddr] = temp
        Addi(i, i, 1)               # i += 1
        #:up_ = while
        {go_up_}
        #>endwhile
    # return L
"""

if __name__ == '__main__':
    # put your testing code within this if
    L = [-20, -10, 0, 20, 40]
    Laddr = 100
    lenL = len(L)
    i = 0
    while i < lenL:
        addr = Laddr + i
        setd(addr, L[i])
        i = i + 1

    setr(r1, Laddr)
    setr(r2, lenL)
    start(ExQ3)
    printd(100,105)

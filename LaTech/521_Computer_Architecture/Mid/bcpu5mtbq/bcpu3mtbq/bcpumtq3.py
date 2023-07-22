myTechEmail = 'sha040' #omit @latech.edu

from bcpu import *

# 15 points

def exp(n:r1,p:r2)->r3:
    # n and p are positive numbers
    npp:r3 = n**p # note 0**0 = 1, 1**0 = 1, 2**0 = 1
    return npp # r3 is used to retrieve the result

# translate the above py program into asm codes
# put all the require asm code inside this string
mtExQ3 = f"""
#>exp(n:r1,p:r2)->r3:
Set(r3, 1)
Set(r5, 0)

#: a_ = r2
#: b_ = r5
#: end_ = endwhile
{a_ne_b_}

Move(r4, r1)
Subi(r2, r2, 1)

#>while r2!= 0: if r2==0 goto endwhile
#: a_ = r2
#: b_ = r5
#:end_ = endwhile
{a_ne_b_}

    #: rd_ = r3 #output
    #: ra_ = r1
    #: rb_ = r4
    {mul_rd_ra_rb_} #r3 = r1*r4
    Move(r4, r3)

    Subi(r2, r2, 1) #r2 -= 1
    #:up_ = while
    {go_up_}

#>endwhile
#return r3
"""

if __name__ == '__main__':
    # put your testing code within this if
    testa1 = 0
    testa2 = 0

    exp(testa1, testa2)
    setr(r1, testa1)
    setr(r2, testa2)
    startfast(mtExQ3)
    getr(3)
    

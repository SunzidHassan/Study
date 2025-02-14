myTechEmail = 'sha040' #omit @latech.edu

from bcpu import *

# 20 points

def ifand(ts:r2)->r3:
    # ts (use r2) is postive input number
    gord:r3 = 0 # set to 0
    if 80 <= ts <= 89: # (80 <= ts) and (ts <= 89)
        gord = 66 # B
    else:
        gord = 67 # C (missing A)
    return gord # will retrieve r3 as output # not need to translate return

# translate the above py program into asm codes
# put all the require asm code inside this string
mtExQ1 = f"""
#:ts=r2
#:gord=r3
Set(gord,0)
#if ts>=80 (if ts<80, goto endif)
Set(cr,80)
Sub(cr,ts,cr)
Addi(ar,pc,?endif)
Moven(pc,ar,cr)
#if ts<=89 (if ts>89, goto endif)
Set(cr,89)
Sub(cr,cr,ts)
Addi(ar,pc,?endif)
Moven(pc,ar,cr)
    Set(gord,66)
    Addi(pc,pc,?done)
#>endif
#else:
   Set(gord,67)
#>done
Move(gord,gord)

"""

if __name__ == '__main__':
    # put your testing code within this if
    test1 = 72
    ifand(test1)
    setr(r2, test1)
    startfast(mtExQ1)
    getr(3)

    test2 = 80
    ifand(test2)
    setr(r2, test2)
    startfast(mtExQ1)
    getr(3)

    test3 = 89
    ifand(test3)
    setr(r2, test3)
    startfast(mtExQ1)
    getr(3)

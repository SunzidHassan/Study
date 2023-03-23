from bcpu import *

# if equals to 11
ifeqal11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx == 11: # (if inx != 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Movex(pc, ar, inx) # if inx != 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 11) # input
setr(r3, 11)
start(ifeqal11then)
printr(r2)

# if not equals to 11
ifneqal11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx != 11: # (if inx == 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Movez(pc, ar, inx) # if inx == 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 11) # input
setr(r3, 11)
start(ifneqal11then)
printr(r2)

# if greater than 11
ifgt11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx > 11: # (if inx <= 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Moven(pc, ar, inx) # if inx <= 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 11) # input
setr(r3, 12)
start(ifgt11then)
printr(r2)


# if less than 11
ifless11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx < 11: # (if inx >= 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Movep(pc, ar, inx) # if inx >= 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 11) # input
setr(r3, 11)
start(ifless11then)
printr(r2)

# if greater than or equal to 11
ifgeq11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx >= 11: # (if inx < 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Moven(pc, ar, inx) # if inx < 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 10) # input
setr(r3, 11)
start(ifgeq11then)
printr(r2)

# if less than or equal to 11
ifleq11then = """
#: inx = r1 # r1 for input
#: outy = r2 # r2 for output
#: var = r3 # r3 for var

Set(outy, 0) # outy = 0
Sub(r1, r1, var)
# if inx <= 11: # (if inx > 11 goto endif)
Addi(ar, pc, ?endif) # ar = address of endif
Movep(pc, ar, inx) # if inx > 11, go to endif
    Set(outy, 1) # else, change outy to 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")
setr(r1, 12) # input
setr(r3, 12)
start(ifleq11then)
printr(r2)
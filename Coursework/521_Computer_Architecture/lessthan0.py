# py program
inx = 0
outy = 0
if inx < 0: #negative number
    outy = 1
print(outy)

# turn this python code into assempty function

# if less than or equals to 0
iflt0then = """
#: inx = r1 # we're going to use r1 for inx
#: outy = r2 # use r2 for outy

Set(outy, 0) # outy = 0

#if inx < 0: (if inx >= 0 goto endif)
Addi(ar, pc, ?endif) # put address of endif into ar
Movep(pc, ar, inx) # if inx the number is positive (including 0), move pc
    Set(outy, 1) # change output from default based on condition: outy = 1
#> endif
Move(outy, outy) #print(outy)
"""

# testing
print("\nRunning the program")

#testing negative number
setr(r1, 0) #os command, not assembly code
start(iflt0then)
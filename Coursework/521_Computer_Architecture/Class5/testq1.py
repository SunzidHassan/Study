absf = """
#> Abs(inx:r1)->r2: # change def to pound greater than sign
    #: inx = r1
    #: outy = r2
    Move(outy, inx) # outy:r2 = inx
    # if inx < 0: (if inx >= goto endif)
    Addi(ar, pc, ?endif)
    Movep(pc, ar, inx)
        Not(outy, inx)
        Addi(outy, outy, 1)
        #outy = -inx
    #> endif
    # return outy # asm will get the return value from r2
"""
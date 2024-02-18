absf = """
#> Abs(inx:r1)->r2: # pound-greater than sign for def
    #: inx = r1
    #: outy = r2
    
    Move(outy, inx) # outy:r2 = inx
    # if inx < 0: (if inx >= goto endif)
    Addi(ar, pc, ?endif) # endif address
    Movep(pc, ar, inx) # if positive, do nothing (send to endif)
        # outy = -inx
        Not(outy, inx) # otherwise: invert+1 for neg
        Addi(outy, outy, 1)
    #> endif
    # return outy # asm will get the return value from r2
"""
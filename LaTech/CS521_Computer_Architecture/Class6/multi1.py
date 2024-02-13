mulasm = """
#> mulpy(r1, r2)->r3:
    #: inx1 = r1
    #: inx2 = r2
    #: outy = r3
    Set(outy, 0)
    #>while r2 != 0: if r2 == 0 goto endwhile
    Addi(ar, pc, ?endwhile)
    Movez(pc, ar, r2)
        Add(outy, outy, inx1)    #r3 += r1
        Subi(inx2, inx2, 1)     #r2 -= 1
        Subi(pc, pc, ?while)
    #>endwhile
    #return outy
"""
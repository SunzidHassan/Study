whileloopf = """
#> whileloop(inx:r1)->r2:
    #: inx = r1
    #: outy = r2
    Set(outy, 0)                # outy:r2 = 0
    #>while inx >= 0:           (if inx < 0 goto endwhile) # the first while is used as label. Names are global: If we have two function with while, we'll have to name them while1, while2
    Addi(ar, pc, ?endwhile)
    Moven(pc, ar, inx)
        Addi(outy, outy, 2)     # outy = outy + 2
        Subi(inx, inx, 1)       # inx = inx - 1
        Subi(pc, pc, ?while)    # jump back to while start
    #>endwhile
    # return outy

"""

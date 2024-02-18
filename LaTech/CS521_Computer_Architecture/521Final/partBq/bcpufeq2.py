myTechEmail = 'sha040' #omit @latech.edu

# 15 points

from bcpu import * 

def minv(L:'Laddr:r1, lenL:r2')->int:
    # in ASM minv(Laddr:r1, lenL:r2) is used instead of minv(L)
    # Laddr, lenL will be used in ASM to pass L
    # pass by reference
    # calling program will put Laddr into r1, lenL into r2
    y:ans = 0 # if L is empty
    if L != []:
        y = min(L)
    else:
        y = 32767
        while i<lenL:
            if L[i] < y:
                y = L[i]
                i += 1
    return y # calling program will get y from ans
    # no need to translate the return (not testing on function calls)

# put all the require asm code inside this string
# only the code needed for the about function should be included
# make sure to use #> minv(L:'Laddr:r1, lenL:r2')->int: as the first line of the code
ExQ2 = f"""
#> minv(L:'Laddr:r1, lenL:r2')->int:
    #:Laddr=r1
    #:lenL=r2
    #:mv=ans

    Set(mv, 0)
    Set(r4, 0)
 
    #:a_=r2
    #:b_=r4
    #:end_=endwhile
    {a_ne_b_}

    #:rd_=mv
    #:pv_=32767
    {set_rd_pv_}
    
    #for n in L:
    #:i=r0
    Set(i,0) #i=0

    #>while i<lenL:
    #:a_=i
    #:b_=lenL
    #:end_=endwhile
    {a_lt_b_}
    
        #s=s+n
        #addr=Laddr+i
        Add(ar,Laddr,i)
        #get n
        #:n=r3
        Load(n,ar)
        #if n>mv:
        #:a_=n
        #:b_=mv
        #:end_=endif
        {a_lt_b_}

        Move(mv,n)
        #>endif
        Addi(i,i,1) #i=i+1

        #go back to while 
        #:up_=while
        {go_up_}
        
    #>endwhile
    #return s
"""

if __name__ == '__main__':
    # put your testing code within this if
    # L = []
    L = [19,2,4,6,100]
    lenL = len(L)
    Laddr = 100
    # for (i = 0; i < lenL; i++)
    i = 0
    while i < lenL:
        addr = Laddr + i
        setd(addr, L[i])
        i = i + 1
    
    setr(r1, Laddr)
    setr(r2, lenL)
    start(ExQ2)
    print(getr(ans))
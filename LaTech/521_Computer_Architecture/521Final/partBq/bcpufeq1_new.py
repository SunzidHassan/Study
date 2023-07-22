myTechEmail = 'yra006' #omit @latech.edu

# 20 points

from bcpu import * 

def inL(x:int, L:'Laddr, lenL')->int:
    # in ASM inL(x, Laddr, lenL) is used instead of inL(x,L)
    # x, Laddr, lenL will be used in ASM to pass x,L
    # pass by COPYING
    # calling program will push x, Laddr, lenL in that order (x first)
    y = 0
    if x in L:
        y = 1
    return y # return value by COPYING

# put all the require asm code inside this string
# only the code needed for the about function should be included
# make sure to use #> inL(x:int, L:'Laddr, lenL')->int: as the first line of the code
ExQ1 = f"""
#> inL(x:int, L:'Laddr, lenL')->int:
    # get return address
    #: returnaddr = r9
    Load(returnaddr, st)
    Subi(st, st, 1)

   #:Laddr=r1
   #:lenL=r2
   #:y=ans
   #:x=r3  
   Set(y,0) #y=0

    # get lenL
    Load(lenL, st)
    Subi(st, st, 1)

    # get Laddr
    Load(Laddr, st)
    Subi(st, st, 1)
    
    # get r3
    Load(x, st)
    Subi(st, st, 1)

   #for n in L:
   #:i=r0
   Set(i,0) #i=0
   #>while i<lenL:
   #:a_=i
   #:b_=lenL
   #:end_=endwhile
   {a_lt_b_}
        
        #addr=Laddr+i
        Add(ar,Laddr,i)
        #get n
        #:n=r7
        Load(n,ar)
        #check if x==n:
        #:a_=x
        #:b_=n
        #:end_=endif
        {a_eq_b_}
            Set(y,1)
            #break
            #:to_=endwhile
            {go_to_}
        #>endif
        Addi(i,i,1) #i=i+1
        #:up_=while
        {go_up_}
        

#>endwhile
    #return ans
    #save ans into stack
    Addi(st, st, 1)
    Store(st, ans)

    #jump back to the calling prog
    Move(pc, returnaddr)

"""
   
maincallfn=f"""
        #:Laddr=r1
        #:lenL=r2       
        
        #:rd_=r3 
        #:pv_=0
        {set_rd_pv_}   #input

        #:rd_=r1 
        #:pv_=120
        {set_rd_pv_}

        #:rd_=r2
        #:pv_=4
        {set_rd_pv_}

        #push input from function into stack
        Addi(st, st, 1)
        Store(st, r3)

        Addi(st, st, 1)
        Store(st, Laddr)
        
        
        Addi(st, st, 1) #store in a stack
        Store(st, lenL)

        #call function
        #:fn_= inL   #use macro to call function
        {call_lib_fn_}

        #>returnhere
        #get the return value
        Load(ans, st)
        Subi(st, st, 1)
        
        Move(ans, ans)        

"""

if __name__ == '__main__':
    # put your testing code within this if
    load(ExQ1) # load is used here for testing only (no load should by used in any other part in this file)
    # put your main asm testing codes here!
    L=[100,200,6,300]
    #int L[4]
    Laddr=120
    lenL=len(L)

    #for (i=0;i<lenL;i++)
    i=0
    while i<lenL:
        addr=Laddr+i
        setd(addr,L[i])
        i+=1
    

    
    import bcpufeq1
    start(maincallfn)
    
    




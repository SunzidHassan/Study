myTechEmail = 'sha040' #omit @latech.edu

from bcpu import *

# 15 points

def fib(n:r2)->ans:
    # n (use r2) is postive # note r2 is used for n
    if n <= 1:
        fn:ans = n # note this is different from homework
    else:
        fn = fib(n-1) + fib(n-2)
    return fn # will retrieve ans (r10) as output # not need to translate return

# translate the above py program into asm codes
# put all the require asm code inside this string
mtExQ2 = f"""
#> fib(n:r2)->ans:
#:n=r2
#:outy=ans
#:a=r3
#:b=r4
#:count=r5


#while n <= 1: (if n>1, goto endif)
Set(cr,1)
Sub(cr,cr,n)
Addi(ar,pc,?endwhile)
Moven(pc,ar,cr)
#if n==0 (if n!=0, goto endif)
    Addi(ar,pc,?endif)
    Movex(pc,ar,n)
        Set(outy,0)
        Addi(pc,pc,?endwhile1)
#>endif
Set(outy, 1)
        
    
#>endwhile

#else: if n>=2 (continue here)
Set(a,0)
Set(b,1)
Set(count,1)
#>while1 count<n:(if count>=n, go to endwhile)
Sub(cr,count,n)
Addi(ar,pc,?endwhile1)
Movep(pc,ar,cr)
    Add(outy,a,b)
    Addi(count,count,1)
    Move(a,b)
    Move(b,outy)
    Subi(pc,pc,?while1)	
    
#>endwhile1
Move(outy,outy)
"""



if __name__ == '__main__':
    # put your testing code within this if
    test = 1
    print(fib(test))

    setr(r2, test)
    startfast(mtExQ2)
    print("ans: ",getr(ans))

    test = 2
    print(fib(test))

    setr(r2, test)
    startfast(mtExQ2)
    print("ans: ",getr(ans))

    test = 10
    print(fib(test))

    setr(r2, test)
    startfast(mtExQ2)
    print("ans: ",getr(ans))


from hashMap import HashMap

# create HashMap to store calculated values

f = HashMap()


# fib(n) = fib(n-1) + fib(n-2)

# fib(5) = fib(4)+ fib(3)
#         = fib(3)+ fib(2) fib(2) + fib(1)
#         = fib(2)+ fib(1) fib(1) + fib(0) + fib(1)+ fib(0) + fib(1)

# if fib(n) in hashmap, return fib(n)
# if fib(0) return 0
# if fib(1) return 1
# if fib(n) = fib(n-1) + fib(n-2) 

# fib(0) = 0

def fib(n):
    # if already calculated for n, then retrieve result from HashMap and return it
    if f["n"] != None:
        fib(n) = f["n"]
        return f["n"]

    # if calculating for 0, then record result to HahsMap and return result
    if n == 0:
      f["n"] = 0
      return 0

    # if calculating for 1, then record result to HahsMap and return result
    if n == 1:
      f["n"] = 1
      return 1
    
    # if calculating for != 0, 1, value that is alredy in HashMap, then
    else:
        f["n"] = fib(n-1) + fib(n-2)        
        return f["n"]

    
    # calculate value according to Fib formula, record the result to HashMap
    # and return the result

def main():
    print(fib(100))

main()

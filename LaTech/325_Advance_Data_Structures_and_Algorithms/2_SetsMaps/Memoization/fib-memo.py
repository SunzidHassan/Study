from hashMap import HashMap

# create HashMap to store calculated values
f = HashMap()

def fib(n):
    # if already calculated for n, then retrieve result from HashMap and return it
    if n in f:
        return f[n]
    # if calculating for 0, then record result to HahsMap and return result
    if n == 0:
        f[n] = 0
        return f[n]
    # if calculating for 1, then record result to HahsMap and return result
    if n == 1:
        f[n] = 1
        return f[n]
    # if calculating for != 0, 1, value that is alredy in HashMap, then calculate value according to Fib formula, record the result to HashMap and return the result
    elif n > 1:
        value = fib(n-1) + fib(n-2)
        f[n] = value
        return f[n]

# used idea from: <https://towardsdatascience.com/memoization-in-python-57c0a738179a>

def main():
    print(fib(100))

main()

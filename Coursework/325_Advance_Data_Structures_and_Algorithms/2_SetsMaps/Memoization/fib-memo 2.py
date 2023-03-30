from hashMap import HashMap

# HashMap for storing calculated values
f = HashMap()
f[0] = 0
f[1] = 1

# fib series: 0, 1, 1, 2, 3, 5, ...
def fib(n):
    if n in f:          # if value is in HashMap, return the value
        return f[n]
    elif n > 1:         # if value not in HashMap and greater than 1, calculate the value, store it in HashMap, return it.
        f[n] = fib(n-1) + fib(n-2)
        return f[n]

def main():
    print(fib(100))

main()
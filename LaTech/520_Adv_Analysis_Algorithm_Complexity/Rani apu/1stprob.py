def nsf(n):
    return [] if n<=0 else nsf(n-1)+[nsf(n-1)]
#solve by choi




print(nsf(3))

#

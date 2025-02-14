myTechEmail = 'sha040' #only your email id, omit @latech.edu
# 20 points

# x^3 problem and function (in python that is x**3)

def xpower3(rmax):
    I = {i for i in range(rmax)}
    S = {s**3 for s in I}
    IxS = {(i,s) for i in I for s in S}
    # i^3 is i to power of 3 problem
    Q = {(i,s) for (i,s) in IxS if i**3 == s}
    # i^3 funciton based on Q
    Qf = lambda i: dict(Q)[i]

    return I,S,IxS,Q,Qf

if __name__ == '__main__':
    # your testing codes within this if
    I, S, IxS, Q, Qf = xpower3(3)

    print("I:", I)
    print("S:", S)
    print("IxS:", IxS)
    print("Q:", Q)
    
    # Print each element of Q
    for (i, s) in Q:
        print(f"Q({i}): {s}")

    # Test Qf for all elements in I
    for i in I:
        print(f"Qf({i}): {Qf(i)}")
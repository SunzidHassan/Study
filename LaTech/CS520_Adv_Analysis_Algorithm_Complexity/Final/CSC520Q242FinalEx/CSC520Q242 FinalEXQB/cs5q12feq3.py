myTechEmail = 'sha040' #only your email id emailID@latech.edu
# cannot contain syntax error

def decision(imax):
    # define a decision problem
    # that decide whether a number in set I is divisible by 5
    I = set(range(imax)) # don't change this I
    S = {'no', 'yes'} # use 'no' and 'yes' 
    IxS = {(i,s) for i in I for s in S}
    Q = {(i,s) for (i,s) in IxS if (i%5 == 0 and s =='yes') or (i%5 != 0 and s == 'no')} 
    Y = {i for (i,s) in Q if s =='yes'} # set
    return S, IxS, Q, Y

if __name__ == "__main__":
    # your testing codes inside this if
    S, IxS, Q, Y = decision(16)
    print(Q)
    print(Y)
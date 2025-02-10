#  All Test Grading
from bcom import *

myName = "Check myName"
myTechID = "Check myTechID"
myTechEmail = "Check myTechEmail"

try:
  from c5mtq0 import myName, myTechID, myTechEmail
except:
  print("import error:")
  print("Check c5mtq0.py file")

testall = []
chksumall = []

# testing Q1
print("testing Q1 ======")
try:
  from c5mtq1 import xpower3
  with open("c5mtq1" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check c5mtq1.py file")

def xpower3t(rmax):
    I = {i for i in range(rmax)}
    S = {i*i*i for i in I}
    IxS = {(i,s) for i in I for s in S}
    Q = {(i,s) for (i,s) in IxS if s==i*i*i}
    Qf = lambda i: dict(Q)[i]
    return I,S,IxS,Q,Qf

# 20 max
try: 
    tg = 0
    I,S,IxS,Q,Qf = xpower3(19)
    It,St,IxSt,Qt,Qft = xpower3t(19)
    tg = 5+tg if S==St else tg
    tg = 5+tg if IxS==IxSt else tg
    tg = 5+tg if Q==Qt else tg
    tg = 5+tg if Qf(9)==Qft(9) else tg
    testall += [tg]
except:
    print("run error")
    testall += [0]
print("++", tg, '\n')


# testing Q2
print("testing Q2 ======")
try:
  from c5mtq2 import Q2q0, Q2df
  with open("c5mtq2" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]  
except:
  print("import error:")
  print("Check c5mtq2.py file")

# fnd max value in seq
# Z={0,1,2}
# Input 01211, where read-write head is on leftmost 0.
# Output 01211_2, where the rightmost 2 is the outputted max number.

# 15 points
try: 
    tg = 0

    Tins = "22"
    Touts = "22_2"
    (q2Touts,q2rwh) = Utm(Tins,Q2df,q0=Q2q0)
    tg = 5+tg if Touts in q2Touts else tg # change == to in
    
    Tins = "0"
    Touts = "0_0"
    (q2Touts,q2rwh) = Utm(Tins,Q2df,q0=Q2q0)
    tg = 5+tg if Touts in q2Touts else tg

    Tins = "010010"
    Touts = "010010_1"
    (q2Touts,q2rwh) = Utm(Tins,Q2df,q0=Q2q0)
    tg = 5+tg if Touts in q2Touts else tg

    testall += [tg]
except:
    print("run error")
    testall += [0]
print("++", tg, '\n')

# testing Q3
print("testing Q3 ======")
try:
  from c5mtq3 import implies, imply
  with open("c5mtq3" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check c5mtq3.py file")

def impliest():
    # return a true table for "A implies B"
    # where A, B, can be True or False
    impliesTT = {(A,B):(not A or B) for A in {True, False} for B in {True, False}}
    return impliesTT

def implyt(A, B):
    # define a function that return the result of "A implies B"
    return not A or B

# 15 points
try: 
    tg = 0

    tg = 10+tg if implies()==impliest() else tg

    tg = 5+tg if imply(True,False)==implyt(True,False) else tg

    testall += [tg]
except:
    testall += [0]
print("++", tg, '\n')


# done all test
print("===================")
try:
  print(myName, myTechID, myTechEmail)
except:
  print("Check name")
print("total:", sum(testall))
i = 1
for g in testall:
    print(f"Q{i} = {g}")
    i += 1

# file output
with open(myTechEmail+'.txt', 'w') as fout:
    fout.write(f"{myName}, {myTechID}, {myTechEmail}\n")
    fout.write(f"total: {sum(testall)}\n")
    i = 1
    for g in testall:
        fout.write(f"Q{i} = {g}\n")
        i += 1
    fout.write("\nChecksums:   \n")
    qchksum = sum(chksumall)
    fout.write(str(qchksum)+"\n")
    print(f"Result writing to {myTechEmail}.txt file")
    print("\nChecksums")
    print(qchksum)

# checksum codes
with open(myTechEmail+'.txt') as fin:
  fr = fin.read()
  txtchksum = sum(ord(c) for c in fr)
  
with open(myTechEmail+'.txt', 'a') as fadd:
  fadd.write(str(txtchksum)+"\n")
  print(txtchksum)


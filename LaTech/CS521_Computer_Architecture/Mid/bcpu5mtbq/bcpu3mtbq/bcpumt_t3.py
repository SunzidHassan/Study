# MT All Test Grading
from bcpu import *

myName = "checkName"
myTechID = "checkCWID"
myTechEmail = "checkEmailID"


try:
  from bcpumtq0 import myName, myTechID, myTechEmail
except:
  print("import error:")
  print("Check bcpumtq0.py file")

testall = []
chksumall = []

# testing Q1
print("testing Q1 ======")
try:
  from bcpumtq1 import mtExQ1
  with open("bcpumtq1" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]  
except:
  print("import error:")
  print("Check bcpumtq1.py file")

def ifand(ts:r2)->r3:
    # ts (use r2) is postive input number
    gord:r3 = 0 # set to 0
    if 80 <= ts <= 89: # (80 <= ts) and (ts <= 89)
        gord = 66 # B
    else:
        gord = 67 # C (missing A)
    return gord # will retrieve r3 as output # not need to translate return


# 20 points
tg = 0
try: 
    load(mtExQ1)

    cv = 99
    anst = ifand(cv)
    setr(2, cv)
    runfast()
    ansr = getr(3)
    tg = 6+tg if anst == ansr else tg
    
    cv = 82
    anst = ifand(cv)
    setr(2, cv)
    runfast()
    ansr = getr(3)
    tg = 8+tg if anst == ansr else tg

    cv = 20
    anst = ifand(cv)
    setr(2, cv)
    runfast()
    ansr = getr(3)
    tg = 6+tg if anst == ansr else tg

    testall += [tg]

except:
    print("run error")
    testall += [0]
print("++", tg, '\n')


# testing Q2
print("testing Q2 ======")
try:
  from bcpumtq2 import mtExQ2
  with open("bcpumtq2" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check bcpumtq2.py file")

def fib(n:r2)->ans:
    # n (use r2) is postive # note r2 is used for n
    if n <= 1:
        fn:ans = n # note this is different from homework
    else:
        fn = fib(n-1) + fib(n-2)
    return fn # will retrieve ans (r10) as output # not need to translate return

# 15 points
tg = 0
try: 
    load(mtExQ2)

    cv = 0
    anst = fib(cv)
    setr(2, cv)
    setr(ans, -1) # reset ans
    runfast()
    ansr = getr(ans)
    tg = 5+tg if anst == ansr else tg

    cv = 20
    anst = fib(cv)
    setr(2, cv)
    runfast()
    ansr = getr(ans)
    tg = 5+tg if anst == ansr else tg

    cv = 15
    anst = fib(cv)
    setr(2, cv)
    runfast()
    ansr = getr(ans)
    tg = 5+tg if anst == ansr else tg

    testall += [tg]
except:
    testall += [0]
print("++", tg, '\n')


# testing Q3
print("testing Q3 ======")
try:
  from bcpumtq3 import mtExQ3
  with open("bcpumtq3" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check bcpumtq3.py file")

def exp(n:r2,p:r3)->ans:
    # n and p are positive numbers
    npp:ans = n**p # note 0**0 = 1, 1**0 = 1, 2**0 = 1
    return npp # ans is used to retrieve the result

# 15 points
tg = 0
try: 
    load(mtExQ3)

    n, p = 0, 0
    anst = exp(n,p)
    setr(1, n)
    setr(2, p)
    setr(3, -1) # make sure it is resetted within asm code
    runfast()
    ansr = getr(3)
    tg = 4+tg if anst == ansr else tg

    n, p = 2, 5
    anst = exp(n,p)
    setr(1, n)
    setr(2, p)
    setr(3, -1) # make sure it is resetted within asm code
    runfast()
    ansr = getr(3)
    tg = 6+tg if anst == ansr else tg

    n, p = 0, 3
    anst = exp(n,p)
    setr(1, n)
    setr(2, p)
    setr(3, -1) # make sure it is resetted within asm code
    runfast()
    ansr = getr(3)
    tg = 2+tg if anst == ansr else tg

    n, p = 1, 4
    anst = exp(n,p)
    setr(1, n)
    setr(2, p)
    setr(3, -1) # make sure it is resetted within asm code
    runfast()
    ansr = getr(3)
    tg = 3+tg if anst == ansr else tg

    testall += [tg]
except:
    print("run error")
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


# fe All Test Grading
from bcpu import *

# test file name:
testfn = 'bcpufe_t3.py'
with open(testfn) as fin:
  fr = fin.read()
  tfchksum = sum(ord(c) for c in fr)


# for Q0
myName = "checkName"
myTechID = "checkCWID"
myTechEmail = "checkEmailID"

try:
  from bcpufeq0 import myName, myTechID, myTechEmail
except:
  print("import error:")
  print("Check bcpufeq0.py file")

testall = []
chksumall = []


# testing Q1
print("testing Q1 ======")
try:
  from bcpufeq1 import ExQ1
  with open("bcpufeq1" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check bcpufeq1.py file")

def inLt(x:int, L:'Laddr, lenL')->int:
    # in ASM intL(x, Laddr, lenL) is used instead of inL(x,L)
    # x, Laddr, lenL will be used in ASM to pass x,L
    # pass by COPYING
    # calling program will push x, Laddr, lenL in that order (x first)
    y = 0
    if x in L:
        y = 1
    return y # return value by COPYING

#load(ExQ1) # load is used here for testing only (no load should by used in any other part in this file)
# put your main testing codes here!

def storeL(L, Laddr, lenL):
    [setd(Laddr+n, L[n]) for n in range(lenL)]
    printd(Laddr, Laddr+lenL)
# testing
L = [2, 4, -1, 6, 7]
print(L)
Laddr = 100
lenL = len(L)
storeL(L, Laddr, lenL)

#main for calling
maintf = f"""
    # test inL asm
    #x = 8
    # push x, Laddr, lenL in this order
##    Set(cr, 1)
##    Not(cr, cr)
##    Addi(cr, cr, 1)
    # pass by ref r1
    Addi(st, st, 1)
    Store(st, r1)
    Set(cr, 100)
    Addi(st, st, 1)
    Store(st, cr)
    Set(cr, 5)
    Addi(st, st, 1)
    Store(st, cr)
    #: fn_ = inL
    {call_lib_fn_}
    # get return value
    Load(ans, st)
    Subi(st, st, 1)
    Move(ans, ans)
"""

tg = 0
try: 
    load(ExQ1) # load first
    load(maintf) # load after

    mv = 4
    pans = inLt(mv, L)
    setr(1, mv)
    runfast()
    pansr = getr(ans)
    tg = 5+tg if pans == pansr else tg

    mv = -1
    pans = inLt(mv, L)
    setr(1, mv)
    runfast()
    pansr = getr(ans)
    tg = 5+tg if pans == pansr else tg

    mv = 7
    pans = inLt(mv, L)
    setr(1, mv)
    runfast()
    pansr = getr(ans)
    tg = 5+tg if pans == pansr else tg

    mv = 10
    pans = inLt(mv, L)
    setr(1, mv)
    runfast()
    pansr = getr(ans)
    tg = 5+tg if pans == pansr else tg        
    
    testall += [tg]
except:
    print("run error")
    testall += [0]
print("++", tg, '\n')


# testing Q2
print("testing Q2 ======")
try:
  from bcpufeq2 import ExQ2
  with open("bcpufeq2" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]  
except:
  print("import error:")
  print("Check bcpufeq2.py file")


def minvt(L:'Laddr:r1, lenL:r2')->int:
    # in ASM minv(Laddr:r1, lenL:r2) is used instead of minv(L)
    # Laddr, lenL will be used in ASM to pass L
    # pass by reference
    # calling program will put Laddr into r1, lenL into r2
    y:ans = 0 # if L is empty
    if L != []:
        y = min(L)
    return y # calling program will get y from ans

def storeL2(L, Laddr, lenL):
    [setd(Laddr+n, L[n]) for n in range(lenL)]
    printd(Laddr, Laddr+lenL)

tg = 0
try: 
    load(ExQ2)

    L = [2, 4, -1, 6, 7, 1]
    print(L)
    Laddr = 100
    lenL = len(L)
    storeL2(L, Laddr, lenL)    
    pans = minvt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = getr(10)
    tg = 5+tg if pans == pansr else tg
    
    L = [2]
    print(L)
    Laddr = 120
    lenL = len(L)
    storeL2(L, Laddr, lenL)    
    pans = minvt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = getr(10)
    tg = 5+tg if pans == pansr else tg

    L = [99,99,22,25,-22]
    print(L)
    Laddr = 120
    lenL = len(L)
    storeL2(L, Laddr, lenL)    
    pans = minvt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = getr(10)
    tg = 5+tg if pans == pansr else tg

    testall += [tg]

except:
    print("run error")
    testall += [0]
print("++", tg, '\n')


# testing Q3
print("testing Q3 ======")
try:
  from bcpufeq3 import ExQ3
  with open("bcpufeq3" + '.py') as fin:
    fr = fin.read()
    chksum = sum(ord(c) for c in fr)
    chksumall += [chksum]
except:
  print("import error:")
  print("Check bcpufeq4.py file")

def l2lt(L:'Laddr:r1, lenL:r2'):
    # in ASM l2l(Laddr:r1, lenL:r2) is used instead of l2l(L)
    # Laddr, lenL will be used in ASM to pass L
    # pass by reference
    # calling program will put Laddr into r1, lenL into r2
    
    L = [n+n for n in L]

    return L # calling program will get L for info in r1 and r2
    # no need to translate the return (in-place passing)

def storeL3(L, Laddr, lenL):
    [setd(Laddr+n, L[n]) for n in range(lenL)]
    printd(Laddr, Laddr+lenL)

def loadL3(Laddr, lenL):
    L = [getd(Laddr+n) for n in range(lenL)]
    return L

tg = 0
try: 
    load(ExQ3)

    L = [2, 4, -1, 6, 7, 1]
    print(L)
    Laddr = 100
    lenL = len(L)
    storeL3(L, Laddr, lenL)    
    pans = l2lt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = loadL3(Laddr, lenL)
    tg = 5+tg if pans == pansr else tg
    
    L = [2]
    print(L)
    Laddr = 120
    lenL = len(L)
    storeL3(L, Laddr, lenL)    
    pans = l2lt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = loadL3(Laddr, lenL)
    tg = 5+tg if pans == pansr else tg

    L = [2,1,2,-2]
    print(L)
    Laddr = 130
    lenL = len(L)
    storeL3(L, Laddr, lenL)    
    pans = l2lt(L)
    setr(1, Laddr)
    setr(2, lenL)
    runfast()
    pansr = loadL3(Laddr, lenL)
    tg = 5+tg if pans == pansr else tg

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

    fout.write("\nTest by "+testfn)
    fout.write("\nChecksums:   \n")
    fout.write(str(tfchksum)+"\n")
    qchksum = sum(chksumall)
    fout.write(str(qchksum)+"\n")
    
    print(f"Result writing to {myTechEmail}.txt file")
    print(f"\nTest by {testfn}")
    print("Checksums")
    print(tfchksum)
    print(qchksum)

# checksum codes
with open(myTechEmail+'.txt') as fin:
  fr = fin.read()
  txtchksum = sum(ord(c) for c in fr)
  
with open(myTechEmail+'.txt', 'a') as fadd:
  fadd.write(str(txtchksum)+"\n")
  print(txtchksum)

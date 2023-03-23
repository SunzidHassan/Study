"""
# BCPU (C) Pr Ben Choi
# Building CPU Simulator:
#   Code, Load, Run
#   BCPU asm programs
#   Multi BCPU cores with share memory

# *** Coding BCPU asm program ***
# A BCPU asm file is a multi-line string defined in a py file
# ASM buildin formats allow 3 types of labels in an asm file
# ASM macros are also allowed (see 4)

# (1) Define var using #:name = value
# Replace 'name' with 'value', eg:
    #:counter = r6  #create var counter
    #:one = 1
    Addi(counter, counter, one)
    # var name can be redefined, eg:
    #:one = 100
    Set(counter, one) # 100 now

# (2) Define label using #>name
# Replace ?name using value of relative offset, eg:
    Set(counter, 15)
    #>while counter >= 0:
    Addi(ar, pc, ?endwhile) # setup jump relative addr in the addr register
    Moven(pc, ar, counter) # goto >endwhile if counter < 0
        # whilepart
        Subi(counter, counter, 1)
        Subi(pc, pc, ?while) # go back to >while
    #>endwhile

# Define function name using #>funcname
#>funcname(...): # define label 'funcname'
    # funcpart
    # ...
    # return using:
    Load(ar, st) # pop return addr
    Subi(st, st, 1) # update stack pointer
    Move(pc, ar) # return back to caller

# call function define in the same file
# from main() call funcname() def before main()
# before calling need to
# push return addr
    Addi(ar, pc, ?returnaddr) # setup relative return addr
    Addi(st, st, 1) # update stack pointer
    Store(st, ar) # push
# calling funcname()
    Set(ar, ?funcname + 1) # relative to next instruction so +1
    Sub(pc, pc, ar) #upward relatve addr
    #>returnaddr

# (3) Define the main function name of a file
# by using the first #> label in the file, eg:
# In a file called mullib.py
#>mul(r2, r3)->r4 # the very first asm label in the file
    # ...
    # return
# The name 'mul' is defined
# by load() for compiling and loading asm into memory

# call function def in other file, eg:
# import the file, eg:
    import mullib
# ...
# calling 'mul'
    Set(ar, ?mul % 256) # absolute addr of the loaded 'mul'
    Seth(ar, ?mul // 256)
    Move(pc, ar)

# (4) Macros asm: (predefined macros included below)
    any string can serve as a macro, eg:
    shiftr2 = 'Addi(r2,r2,r2)'
    use f spring to def main asm file
    in main file use a macro by {shiftr2} 

# *** Saving compiled codes into a file
# Asm file is compiled and saved into a py file, eg
    save(muldef, 'mulcode') # create mulcode.py file 

# *** Loading asm file ***
# Asm file is compiled and loaded into memory, eg
	load(muldef) # where muldef is a multi-line string containing the asm program
# auto allocate memory for multiple loads, eg
    load(file1)
    load(file2)
# define main function name during load, eg
    load(muldef, fname="multify")

# *** Running asm program ***
    run() # auto use just loaded
    run('func') # run the specific loaded func
    runfast() # run without printing each step

# *** Start by load and run asm program ***
    start(file1) # load and run file1
    startfast(file1) # load and runfast file1

# OS functions for testing
    setr(r2, -1234) # set and print a register in int
    setrb(r3, 0b1111_0000_1100_1100) # set and print a register in bin
    getr(2) # get r2 int value
    getrb(2) # get r2 as 16 bit positive value
    printr(r2) # print a register in int
    printrb(r3) # a register in bin
    printd(100, 120) # range in data storage
    setd(100, -123) # set to dada storage
    getd(100) # get from data storage
    printm() # instruction memory

# *** Multiprocessors with share memory ***
    printsd()  # print share data storage
    setsd(1,11) # set sds 1 to 11
    getsd(1) # get data from sds 1
    Set(ar, 100)
    Seth(ar, SDS) # setting an addr in share data storage
    Store(ar, r1) # store r1 in share data storage
    starts(asmf1, asmf2) # run muliple asm files in parallel
    startfasts(p1,p2,p3) # runfast not printing each step
    wait_sdi_ macro for waiting sds index i till not 0
    sleep_pv_ macro for sleep pv times used for async testing
"""
from multiprocessing import Manager, Pool
from os import getpid, getppid

_VER = '5.3.0'

# register address (reserved const)
R0 = r0 = 0
R1 = r1 = 1
R2 = r2 = 2
R3 = r3 = 3
R4 = r4 = 4
R5 = r5 = 5
R6 = r6 = 6
R7 = r7 = 7
R8 = r8 = 8
R9 = r9 = 9
R10 = r10 = 10
R11 = r11 = 11
R12 = r12 = 12
R13 = r13 = 13
R14 = r14 = 14
PC = Pc = pc = 15  # program counter

# Registers
R_ = [0 for _ in range(2 ** 4)] # ***sim unknown undefined value (Cannot assume be 0) ***
R_[pc] = 0 # sim startup clear pc

# Data storage
D_ = [0 for _ in range(2 ** 8)]

# Share data storage for multiprocessing
SD_ = [0 for _ in range(2**8)] # use in non parallel
# replace by next line only in starts and startfasts
#SD_ = Manager().list([SD_[a] for a in range(2**8)])  # copy org SD_

# Instruction memory
M_ = [0 for _ in range(2 ** 16)]

# BIOS ===

# Answer reg
ANS = Ans = ans = R10
# Result reg
RES = Res = res = R11

# Conditional (check) reg
CR = Cr = cr = R12
# Addr reg
AR = Ar = ar = R13

# stack
ST = St = st = R14  # stack top
R_[st] = 0  # empty
D_[0] = 0
"""
# empty if R[st] == 0
# start at D[1] upward
# push:
  Addi(st, st, 1)
  Store(st, r2)
# pop:
  Load(r3, st)
  Subi(st, st, 1)
"""

# data storage I/O address
Di0 = di0 = 210
Di1 = di1 = 211
Di2 = di2 = 212
Di3 = di3 = 213

Do0 = do0 = 220
Do1 = do1 = 221
Do2 = do2 = 222
Do3 = do3 = 223
#

# data storage heap start
Dh0 = dh0 = 230
Dh1 = dh1 = 231
Dh2 = dh2 = 232
Dh3 = dh3 = 233
#

# high bit shared data 
SDS = 1  # uses in Seth as high bit for 256 shared data storage


# Predefined Macros ===

set_rd_pv_ = """
# use #: to def rd_ and pv_ before using this mc
Set(rd_, pv_%256)
Seth(rd_, pv_//256)
"""

setn_rd_pv_ = """
# use #: to def rd_ and pv_ before using this mc
Set(rd_, pv_%256)
Seth(rd_, pv_//256)
Not(rd_, rd_)
Addi(rd_, rd_, 1)
"""

a_eq_b_ = """
# a_ == b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, a_, b_)
Movex(pc, ar, cr)
# true: 
"""

a_ne_b_ = """
# a_ != b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, a_, b_)
Movez(pc, ar, cr)
# true: 
"""

a_lt_b_ = """
# a_ < b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, a_, b_)
Movep(pc, ar, cr)
# true: 
"""

a_gt_b_ = """
# a_ > b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, b_, a_)
Movep(pc, ar, cr)
# true: 
"""

a_le_b_ = """
# a_ <= b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, b_, a_)
Moven(pc, ar, cr)
# true: 
"""

a_ge_b_ = """
# a_ >= b_ # false: goto end_
Set(ar, (?end_-2)%256)
Seth(ar, (?end_-1)//256)
Add(ar, pc, ar)
Sub(cr, a_, b_)
Moven(pc, ar, cr)
# true: 
"""

go_up_ = """
    # go back up_
    Set(ar, (?up_+2)%256)
    Seth(ar, (?up_+1)//256)
    Sub(pc, pc, ar)
"""

go_to_ = """
    # go down to_
    Set(ar, (?to_-2)%256)
    Seth(ar, (?to_-1)//256)
    Add(pc, pc, ar)
"""

return_ = """
# return back to calling prog
Load(ar,st)
Subi(st,st,1)
Move(pc,ar)
"""

call_fn_ = """
    # call function fn_
    # push return addr
    Addi(ar, pc, 6)
    Addi(st,st,1)
    Store(st, ar)
    # go up to fn
    Set(ar, (?fn_+2)%256)
    Seth(ar, (?fn_+1)//256)
    Sub(pc, pc, ar)
    # returning to here
"""

call_lib_fn_ = """
# need to import the lib
# call function fn_ defined and loaded in the lib
    # push return addr
    Addi(ar, pc, 6)
    Addi(st,st,1)
    Store(st, ar)
    # go up to fn
    Set(ar, ?fn_%256)
    Seth(ar, ?fn_//256)
    Move(pc, ar)
    # returning to here
"""

pushrs_ = """
# save r0..r9 in stack
Addi(st,st,1)
Store(st,r0)
Addi(st,st,1)
Store(st,r1)
Addi(st,st,1)
Store(st,r2)
Addi(st,st,1)
Store(st,r3)
Addi(st,st,1)
Store(st,r4)
Addi(st,st,1)
Store(st,r5)
Addi(st,st,1)
Store(st,r6)
Addi(st,st,1)
Store(st,r7)
Addi(st,st,1)
Store(st,r8)
Addi(st,st,1)
Store(st,r9)
# r10, r11, r12 not saved, may use to pass back results by ref
"""

poprs_ = """
# retrieve r9..r0 from stack
# r10, r11, r12 not saved, may use to pass back results by ref
Load(r9,st)
Subi(st,st,1)
Load(r8,st)
Subi(st,st,1)
Load(r7,st)
Subi(st,st,1)
Load(r6,st)
Subi(st,st,1)
Load(r5,st)
Subi(st,st,1)
Load(r4,st)
Subi(st,st,1)
Load(r3,st)
Subi(st,st,1)
Load(r2,st)
Subi(st,st,1)
Load(r1,st)
Subi(st,st,1)
Load(r0,st)
Subi(st,st,1)
"""

mul_rd_ra_rb_ = """
# rd_ = ra_ * rb_ # - or +
# use cr, ar
Set(rd_, 0)
# fix sign # if ra_ < 0
Sub(cr,rd_,rb_) # rd_ is 0
Moven(rb_,cr,ra_) # -rb_
Sub(cr,rd_,ra_)
Moven(ra_,cr,ra_) # -ra_
#
Set(ar,1) #check mask
# bti 0
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 1
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 2
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 3
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 4
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 5
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 6
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 7
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 8
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 9
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 10
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 11
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 12
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 13
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
  Add(ar,ar,ar) #p1 = p1 + p1
  Add(rb_,rb_,rb_) #p3 = p3 + p3
# bti 14
  And(cr,ar,ra_) #p9 = p1 & p2
  Movex(cr, rb_, cr) 
  Add(rd_,rd_,cr) # p4 = p4 + p3 if p9 != 0
# endmul
"""

div_qu_re_nu_de_ = """
# div(nu_,de_) -> (qu_,re_)
# qu_ = nu_ // de_
# re_ = nu_ % de_
# - or +
# use 0, 1, cr, ar
Move(r0, nu_) # save for fix sign
Move(r1, de_)
Set(qu_, 0) #Q = 0
Set(re_, 0) #R = 0
# abs
Sub(nu_, qu_, nu_) # qu_ is 0
Movep(nu_, r0, r0)
Sub(de_, qu_, de_)
Movep(de_, r1, r1)
# bitwise div
# bit 15 ===
  Add(nu_, nu_, nu_)
# bit 14 ===
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1
  Add(nu_, nu_, nu_)
# bit 13 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 12 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 11 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 10 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 9 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 8 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 7 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 6 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 5 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 4 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 3 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 2 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 1 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
  Add(nu_, nu_, nu_)
# bit 0 ===
  Add(qu_, qu_, qu_) # << 1
  Add(re_, re_, re_) # << 1
  Addi(cr,re_,1)
  Moven(re_, cr, nu_)
  Sub(cr, re_, de_)
  Movep(re_, cr, cr) # re_ -= de_
  Addi(ar, qu_, 1) # so can shift, not rotate
  Movep(qu_, ar, cr) # qu_ += 1  
# done bitwise
# fix sign
Set(nu_, 0)
Sub(cr, nu_, re_)
Moven(re_, cr, r0)
Sub(cr, nu_, qu_)
Moven(qu_, cr, r0)
Sub(cr, nu_, qu_)
Moven(qu_, cr, r1)
# divide by 0
Movez(qu_, r1, r1)
Movez(re_, r1, r1)
# enddiv
"""

wait_sdi_ = """
# wait for share data index i till not eq 0
# need to def sdi_ before using this mc
# use ar, cr, res
# res will contain the checked share data
Set(cr, 1000%256) # tmax for time out
Seth(cr, 1000//256)
Set(res, 0)
# while cr >= 0:
# if cr < 0 : goto endwhile
Addi(ar,pc,11)
Moven(pc, ar, cr)
	Move(res, res) # nop
	Move(res, res)
	Move(res, res)
	Subi(cr, cr, 1)
	# check the flag
	Set(ar,sdi_)
	Seth(ar, SDS)
	Load(res, ar)
	# if flag is != 0 then break
	Subi(ar, pc, 9)
	Movez(pc, ar, res)
# endwhile
Move(res,res) # print out flag
"""

sleep_pv_ = """
# sleep for pv_ times # use for async testing
# need to def pv_ (positive value) before using this mc
# use ar, cr
Set(cr, pv_%256) # tmax for time out
Seth(cr, pv_//256)
# while cr >= 0:
# if cr < 0 : goto endwhile
Addi(ar,pc,7)
Moven(pc, ar, cr)
	Move(cr, cr) # nop
	Move(cr, cr)
	Move(cr, cr)
	Subi(cr, cr, 1)
	Subi(pc, pc, 6)
# endwhile
"""
#

# simulator functions ===

# constants used for simultor 
_SDSB = 0b00000001_00000000 # check bit for share data
_H = 0b1111111111111111  # 16 bits
_B15 = 0b1000000000000000  # sign bit
_Err = "_Err_"
_PRI = True  # printi or not


# printing interger + - number
def printi(d, a='', b=''):
    """Print a 16-bit integer"""
    if not _PRI: return  # not print
    if d & _B15: d = -(-d & _H)
    if (a != '') and a & _B15: a = -(-a & _H)
    if (b != '') and b & _B15: b = -(-b & _H)
    print(d, a, b)


# get interger + - number, out of 16 bits
def geti(b):
    """Get a 16-bit int value"""
    n = b
    if b & _B15: n = -(-b & _H)  # bit15 is sign bit
    return n


# printing a 16-bit binary number
def printb(n):
    """Print 16 bits"""
    ns = '0000000000000000' + bin(n)[2:]
    print(ns[-16:-12], ns[-12:-8], ns[-8:-4], ns[-4:])


# get 16 bits out of + - number
def getb(n):
    """Get 16 bits"""
    b = n & _H
    return b


# Instructions 16 defs ===
_OPNAMES = ['Move', 'Not', 'And', 'Or',
           'Add', 'Sub', 'Addi', 'Subi',
           'Set', 'Seth', 'Store', 'Load',
           'Movez', 'Movex', 'Movep', 'Moven']


def Move(Rd, Ra):
    """ Rd = Ra """
    vRa = R_[Ra]
    R_[Rd] = R_[Ra]
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa)


def Not(Rd, Ra):
    """ Rd = ~Ra """
    vRa = R_[Ra]
    R_[Rd] = (~R_[Ra]) & _H
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa)


def And(Rd, Ra, Rb):
    """ Rd = Ra & Rb """
    vRa, vRb = R_[Ra], R_[Rb]
    R_[Rd] = R_[Ra] & R_[Rb]
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Or(Rd, Ra, Rb):
    """ Rd = Ra | Rb """
    vRa, vRb = R_[Ra], R_[Rb]
    R_[Rd] = R_[Ra] | R_[Rb]
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Add(Rd, Ra, Rb):
    """ Rd = Ra + Rb """
    vRa, vRb = R_[Ra], R_[Rb]
    R_[Rd] = (R_[Ra] + R_[Rb]) & _H
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Sub(Rd, Ra, Rb):
    """ Rd = Ra - Rb"""
    vRa, vRb = R_[Ra], R_[Rb]
    R_[Rd] = (R_[Ra] + (-R_[Rb]) & _H) & _H
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Addi(Rd, Ra, v):
    """ Rd = Ra + v """
    if not (0 <= v <= 15):
        print("Value should be 0...15")
        return _Err
    vRa = R_[Ra]
    R_[Rd] = (R_[Ra] + v) & _H
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, v)


def Subi(Rd, Ra, v):
    """ Rd = Ra - v """
    if not (0 <= v <= 15):
        print("Value should be 0...15")
        return _Err
    vRa = R_[Ra]
    R_[Rd] = (R_[Ra] - v) & _H
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa, v)


def Set(Rd, v):
    """ Rd = v """
    if not (0 <= v <= 255):
        print("Value should be 0...255")
        return _Err
    R_[Rd] = v
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], v)


def Seth(Rd, v):
    """ Rd = v*256 + Rd%256 """
    if not (0 <= v <= 255):
        print("Value should be 0...255")
        return _Err
    R_[Rd] = v * 256 + R_[Rd] % 256
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], v)


def Store(Rd, Ra):
    """ D[Rd] = Ra """
    a = R_[Rd] % 256
    if R_[Rd] & _SDSB: # shared
        SD_[a] = R_[Ra]
    else:
        D_[a] = R_[Ra]
    R_[Pc] += 1
    printi(R_[Rd], R_[Ra])


def Load(Rd, Ra):
    """ Rd = D[Ra] """
    vRa = R_[Ra]
    a = R_[Ra] % 256
    if R_[Ra] & _SDSB: # shared
        R_[Rd] = SD_[a]
    else:
        R_[Rd] = D_[a]
    if Rd != Pc: R_[Pc] += 1
    printi(R_[Rd], vRa)


def Movez(Rd, Ra, Rb):
    """ Rd = Ra if Rb == 0 """
    vRa, vRb = R_[Ra], R_[Rb]
    if R_[Rb] == 0:
        R_[Rd] = R_[Ra]
        if Rd != Pc: R_[Pc] += 1
    else:
        R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Movex(Rd, Ra, Rb):
    """ Rd = Ra if Rb != 0 """
    vRa, vRb = R_[Ra], R_[Rb]
    if R_[Rb] != 0:
        R_[Rd] = R_[Ra]
        if Rd != Pc: R_[Pc] += 1
    else:
        R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Movep(Rd, Ra, Rb):
    """ Rd = Ra if Rb >= 0 """
    vRa, vRb = R_[Ra], R_[Rb]
    if R_[Rb] & _B15 == 0:
        R_[Rd] = R_[Ra]
        if Rd != Pc: R_[Pc] += 1
    else:
        R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


def Moven(Rd, Ra, Rb):
    """ Rd = Ra if Rb < 0 """
    vRa, vRb = R_[Ra], R_[Rb]
    if R_[Rb] & _B15:
        R_[Rd] = R_[Ra]
        if Rd != Pc: R_[Pc] += 1
    else:
        R_[Pc] += 1
    printi(R_[Rd], vRa, vRb)


# os ===

# pre def Addr (allow the addr to be accessed between files)
class Addr:
    pass


"""
# lib function def as, eg
# first in lib function file, eg mul file
#>mul(r2,r3)->r4: # the top label of a file def func name
  # ...
  # return 
# last in mul func file
load(mul)

# from main file, call the func
  # import the mullib file
  # ...
  # call
  Set(ar, ?mul % 256)
  Set(ar, ?mul // 256)
  Move(pc, r10)
"""

# memory management
_PROGMEM0 = 100  # prog mem start at and up
Addr.justloaded = _PROGMEM0  # the prog just loaded (Addr. needed for multi files)
_memmap = {}  # 'fname':(addrbeg, addrend)
"""
# auto allocate memory for muliple loads, eg
load(mul) # auto find func name from top label
load(div)
load(main)
# run just loaded
run()
# run mul
run('mul') # or
run(Addr.mul) # auto defined addr for mul func
"""


# os functions ===

def printr(r=None):
    """Print registers"""
    if r is None:
        for i in range(15):
            print('R' + str(i) + ':', end=' ')
            printi(R_[i])
        print('PC:', R_[pc])
    else:
        if r != pc:
            print(f"R{r}:", end=' ')
            printi(R_[r])
        else:
            print('PC:', R_[pc])


def printrb(r=None):
    """Print registers bitwise"""
    if r is None:
        for i in range(15):
            print('R' + str(i) + ':', end=' ')
            printb(R_[i])
        print('PC:', end=' ')
        printb(R_[pc])
    else:
        if r != pc:
            print(f"R{r}:", end=' ')
        else:
            print(f'PC:', end=' ')
        printb(R_[r])


def printd(a=None, z=None):
    """Print data storage"""
    if a is None and z is None:
        a = 0; z = 256
        print(f'D[{a}:{z}]:', end=' ')
        for n in D_[a:z]:
            if n & _B15: n = -(-n & _H)
            print(n, end=', ')
        print()
    elif z is None:
        a = a%256
        print(f'D[{a}]:', geti(D_[a]))
    else:
        a = a%256; z = z%256
        print(f'D[{a}:{z}]:', end=' ')
        for n in D_[a:z]:
            if n & _B15: n = -(-n & _H)
            print(n, end=', ')
        print()

def printsd(a=None, z=None):
    """Print data storage"""
    if a is None and z is None:
        a = 0; z = 256
        print(f'SD[{a}:{z}]:', end=' ')
        for n in SD_[a:z]:
            if n & _B15: n = -(-n & _H)
            print(n, end=', ')
        print()
    elif z is None:
        a = a%256
        print(f'SD[{a}]:', geti(SD_[a]))
    else:
        a = a%256; z = z%256
        print(f'SD[{a}:{z}]:', end=' ')
        for n in SD_[a:z]:
            if n & _B15: n = -(-n & _H)
            print(n, end=', ')
        print()

def printm(a=None):
    """Print memory"""
    a = Addr.justloaded if a is None else a
    while M_[a] != 0:  # 0 no instuction
        print(M_[a], '[' + str(a) + ']')
        a += 1


def setr(r, v=0):
    R_[r] = getb(v)
    printr(r)


def setrb(r, v=0):
    R_[r] = getb(v)
    printrb(r)


def getr(r):
    return geti(R_[r])


def getrb(r):
    return R_[r]


def setd(a, v=0):
    a = a%256
    D_[a] = getb(v)
    printd(a)


def getd(a):
    a = a%256
    return geti(D_[a])


def setsd(a, v=0):
    a = a%256
    SD_[a] = getb(v)
    printsd(a)


def getsd(a):
    a = a%256
    return geti(SD_[a])


# ===

def run(a=None):
    """Run program """
    a = Addr.justloaded if a is None else a
    if type(a) == str:
        if a in vars(Addr):
            a = vars(Addr)[a]
        else:
            print(f"*** Run stopped: {a} not loaded")
            return _Err
    R_[Pc] = a
    while M_[a] != 0:  # 0 no instuction
        print(M_[a], '[' + str(a) + ']')
        try:
            ret = eval(M_[a])
        except:
            print("*Err: Asm code syntax error")
            break
        if ret == _Err:
            print("*** Run stopped due to above error ***")
            break
        a = R_[Pc]


def runfast(a=None, maxi=123000):
    """Run program, not printi, with limit"""
    a = Addr.justloaded if a is None else a
    if type(a) == str:
        if a in vars(Addr):
            a = vars(Addr)[a]
        else:
            print(f"*** Runfast stopped: {a} not loaded")
            return _Err
    global _PRI
    _PRI = False  # not printi
    print('*** Running fast, no trace ***')
    mx = 0
    R_[Pc] = a
    while M_[a] != 0:  # 0 no instuction
        try:
            ret = eval(M_[a])
        except:
            print(M_[a], '[' + str(a) + ']')
            print("*Err: Asm code syntax error")
            break
        if ret == _Err:
            print("*Err: Run stopped due to above error")
            break
        a = R_[Pc]
        # run limit in case infinite loop
        mx += 1
        if mx > maxi:
            print("*Err: Run stopped at limit", maxi)
            print("*Err: May due to infinite loop")
            break
    print(f"  * Done in {mx} steps *")
    _PRI = True  # printi resume
    return mx


def bcompile(ps):
    """Translating program into instructions"""
    # program format:
    # (1) label: #>name
    # replaceement of offset: ?name
    # else (2) replace ?name with value of pre def Addr.name
    # (3) label #:name = value replace name with value

    # auto define function name
    FNAME0 = 'main' # default fn name
    fname = FNAME0  # default fn name

    pl = ps.splitlines()
    pl = [s.strip() for s in pl]
    pl = [s for s in pl if s != '']

    # create labal dict for #:name = value
    nvli = []
    for i in range(len(pl[:])):
        if pl[i][:2] == '#:':
            nvli = [(pl[i], i)] + nvli # high line number to low
    
    nvls = [s for (s,i) in nvli]
    for s in nvls:
        if '=' not in s:
            print(s)
            print("*** Compile Stop: missing = sign ***")
            return _Err
    nvi = [(s.split(sep='=', maxsplit=1),i) for (s,i) in nvli]
    nvi = [(k[2:].strip(), v, i) for ([k,v],i) in nvi]
    nvi = [(k, v.split(sep='#', maxsplit=1)[0].strip(), i) for (k, v, i) in nvi]
    for x in range(len(nvi)):
        if nvi[x][1] == '':
            print(nvls[x])
            print("*** Compile Stop: missing value ***")
            return _Err
    # done: nvi list of (k,v,i)
    
    # allowing #:name = name1 #:name1 = value1
    mi = len(nvi) # max recursive
    more = True
    while mi > 0 and more:
        more = False
        for x in range(len(nvi)):
            (kx, vx, ix) = nvi[x]
            for y in range(len(nvi)):
                (ky, vy, iy) = nvi[y]
                if vx == ky:
                    nvi[x] = (kx, vy, ix)
                    more = True
        mi -= 1
        
    # replace name with value from #:name
    for i in range(len(pl[:])):
        if pl[i][0] != '#':
            if '(' not in pl[i]:
                print(pl[i])
                print(f'*** Compile Stop: not an ASM code, ( not found ***')
                return _Err
            sp = pl[i].split(sep='(', maxsplit=1)
            fn = sp[0]  # function name
            opname = fn.strip()
            if opname not in _OPNAMES:
                print(pl[i])
                print(f'*** Compile Stop: Function is not an ASM operation ***')
                return _Err
            sp1s0 = sp[1]
            comment = ''
            if '#' in sp[1]:
                sp1s = sp[1].split(sep='#', maxsplit=1)
                sp1s0 = sp1s[0]
                comment =  '#' + sp1s[1]
            if ')' not in sp1s0:
                print(pl[i])
                print('*** Compile Stop: not an ASM code, ) not found ***')
                return _Err
            sp = sp1s0.rsplit(sep=')', maxsplit=1)
            rest = sp[1]
            args0 = sp[0]
            if args0 == '':
                print(pl[i])
                print('*** Compile Stop: missing args ***')
                return _Err            
            # multi name replace # seq search
            # convert args0 to list of fields to find names
            args = ''
            for c in args0:
                c = c if (c.isalnum() or c=='_') else ' '
                args += c
            argnl = args.split()
            argsl = list(args)
            for ci in range(len(argsl)):
            	argsl[ci] = str(ci)+',' if argsl[ci] != ' ' else ' '
            argsls = ''.join(argsl)
            argnli = argsls.split()
            argnlis = [int(ns.split(sep=',')[0]) for ns in argnli]
            argss = list(args0)
            for ni in range(len(argnlis)-1, -1, -1):
            	argss.insert(argnlis[ni]+len(argnl[ni]), '$')
            	argss.insert(argnlis[ni], '$')
            argss = ''.join(argss)
            argssl = argss.split(sep='$') # list of fields
            
            # find the nearest above def name
            # allow to redefine name
            for fi in range(len(argssl)):
                fs = argssl[fi]
                if fs!='' and (fs[0].isalnum() or fs[0]=='_'):
                	name = fs
	                for (k,v,idn) in nvi:
	                     if (idn<i) and (k==name):
	                         value = v
	                         # replace name with value
	                         argssl[fi] = value
	                         break # done one
            args1 = ''.join(argssl)
            pl[i] = fn + '(' + args1 + ')' + rest + comment
    
    # keep #> lines remove rest # lines
    for i in range(len(pl)):  # keep #> line
        if pl[i][:2] == '#>':
            pl[i] = '_' + pl[i]
    pl = [s for s in pl if s[0] != '#']

    # create label dict for #>name or #> name
    labdict = []
    for _ in range(len(pl[:])):
        for i in range(len(pl)):
            if pl[i][0] == '_':
                slb = pl[i][3:].strip()
                lb = ''
                for s in slb:
                    if s.isalnum():
                        lb += s
                    else:
                        break
                # check redef label
                for x in range(len(labdict)):
                    if lb == labdict[x][0]:
                        print(pl[i][1:])
                        print(f"*** Compile Stop: redefining #>{lb} label (try rename this label) ***")
                        return _Err
                labdict += [(lb, i)]
                # get fn name as the top label, only once
                if i == 0 and fname==FNAME0:
                	fname = lb
                del pl[i]
                break # get one label at a time
    labdict = dict(labdict)

    # fix line with ?name
    # ***(? is now reserved keyword)
    for i in range(len(pl[:])):
        pli = pl[i]
        comment = ''
        if '#' in pli:
            plis = pli.split(sep='#', maxsplit=1)
            pli = plis[0]
            comment =  '#' + plis[1]
        if ')' not in pli:
            print(pl[i])
            print(f'*** Compile Stop: not a ASM code, ) not found ***')
            return _Err
        sfl = pli.rsplit(')', maxsplit=1) # fix only part before )
        if '?' in sfl[0]:
            sl = sfl[0].split('?', maxsplit=1)
            lb = ''
            for s in sl[1]:  # fix only 1st ?
                if s.isalnum():
                    lb += s
                else:
                    break
            if lb in labdict.keys():
                lbv = abs(labdict[lb] - i)  # label relative offset
            elif lb in vars(Addr):
                lbv = vars(Addr)[lb]  # pre def label, absolute addr
            else:
                print(f'*** Compile Stop: Label for ?{lb} not found ***')
                return _Err
            sl[1] = sl[1].replace(lb, str(lbv), 1)
            sfl[0] = ''.join(sl)
        pl[i] = sfl[0] + ')' + sfl[1] + comment

    # Check args for registers numbers and values
    for i in range(len(pl[:])):
        sp = pl[i].split(sep='(', maxsplit=1)
        fn = sp[0]  # function name
        opname = fn.strip()
        sp1s0 = sp[1]
        #comment = ''
        if '#' in sp[1]:
            sp1s = sp[1].split(sep='#', maxsplit=1)
            sp1s0 = sp1s[0]
            #comment =  '#' + sp1s[1]
        sp = sp1s0.rsplit(sep=')', maxsplit=1)
        #rest = sp[1]
        args0 = sp[0]
        try:
            argsv = eval('['+args0+']')
        except:
            print(pl[i])
            print(f'*** Compile Stop: Error in args: {args0} ***')
            return _Err
        # check args and ranges
        if opname in {'Move', 'Not', 'Set', 'Seth', 'Store', 'Load'}:
            if len(argsv) != 2:
                print(pl[i])
                print(f'*** Compile Stop: need 2 args ***')
                return _Err
        else:
            if len(argsv) != 3:
                print(pl[i])
                print(f'*** Compile Stop: need 3 args ***')
                return _Err
        if opname in {'Set', 'Seth'}:
            if not (0 <= argsv[0] <= 15):
                print(pl[i])
                print(f'*** Compile Stop: reg need to be 0..15 ***')
                return _Err
            if not (0 <= argsv[1] <= 255):
                print(pl[i])
                print(f'*** Compile Stop: set value need to be 0..255 ***')
                return _Err
        else:
            for v4 in argsv:
                if not (0 <= v4 <= 15):
                    print(pl[i])
                    print(f'*** Compile Stop: arg values need to be 0..15 ***')
                    return _Err
        # R not allowed inside value (not allow to access reg in setting value)
        argsl = args0.split(sep=',')
        if opname in {'Addi', 'Subi', 'Set', 'Seth'}:
            if ('R' in argsl[-1]) or ('r' in argsl[-1]):
                print(pl[i])
                print(f'*** Compile Stop: last arg: {argsl[-1]} need to be a value, cannot be a reg ***')
                return _Err
            
    ##
    return fname, pl


def allocate(fname, flen, addr) -> 'addr':
    """Finding a location for loading program"""
    # find slot in memmap to load func
    # update memmap with loaded func
    # auto define Addr.{fname} = {addr}

    global _memmap  # PROGMEM0, Addr.
    # remove conflict
    if fname in _memmap:
        print("*Replacing memory with new code:", fname)
        del _memmap[fname]
    # force into addr space
    if addr is not None:
        # check conflict
        fr = (addr, addr + flen)
        for k in _memmap:
            mv = _memmap[k]
            if (mv[0] <= fr[0] <= mv[1]) or (mv[0] <= fr[1] <= mv[1]):
                print(f"*** Addr {addr} conflit with loaded code: {k}")
                print("  * Try giving a higher address")
                return _Err
        # free to add
        _memmap.update({fname: (addr, addr + flen)})
        try:
        	exec(f'Addr.{fname} = {addr}')
        except:
        	print(f"***Error:  *{fname}* cannot be used as function name")
        	return _Err        
        return addr
    # find a space to fit prog
    # empty case
    if _memmap == {}:
        addr = _PROGMEM0
        _memmap.update({fname: (addr, addr + flen)})
        try:
        	exec(f'Addr.{fname} = {addr}')
        except:
        	print(f"***Error: *{fname}* cannot be used as function name")
        	return _Err
        return addr
    # check memmap for slot
    mmv = list(_memmap.values())
    mmv += [(0, _PROGMEM0 - 1), (2 ** 16 - 1, 2 ** 16 - 1)]
    mmv = sorted(mmv)
    for i in range(len(mmv) - 1):
        if (mmv[i + 1][0] - mmv[i][1]) > (flen + 1):  # adde 1 for 0 end
            addr = mmv[i][1] + 1
            _memmap.update({fname: (addr, addr + flen)})
            try:
            	exec(f'Addr.{fname} = {addr}')
            except:
            	print(f"***Error: *{fname}* cannot be used as function name")
            	return _Err
            return addr
    #
    return _Err


def load(ps, addr=None, fname=None):
    """Loading asm codes in memory"""
    # (1) compile
    # (2) allocate
    # (3) load

    bret = bcompile(ps)
    if bret == _Err:
        print("*** Load Stop: Compile error ***")
        return _Err
    (fname0, pl) = bret

    fname = fname0 if fname is None else fname
    flen = len(pl)
    # allocate mem
    addr = allocate(fname, flen, addr)
    if addr == _Err:
        print("*** Load Stop: Cannot Allocate memory ***")
        return _Err

    Addr.justloaded = addr
    # load to memory
    a0 = a = addr
    for s in pl:
        M_[a] = s
        a += 1
    M_[a] = 0  # end

    print("*** Loaded in memory:", (a0, a))
    print("  * Function name is:", fname)
    return (fname, (a0, a))  # allowing load after this addr


def start(asm):
    """Load and Start running the aam code"""
    rc = load(asm)
    if rc != _Err:
        run()


def startp_(asm):
    """Load and Start running the aam code"""
    print(f'module: {__name__} ppid: {getppid()} pid: {getpid()}')
    rc = load(asm)
    if rc != _Err:
        run()
    print(f"pid {getpid()} R: {R_}")
    return R_


def starts(*asms):
    """Load and Start running multiple asm files in parallel
    *only work in linux* """
    global SD_ # share data
    prs = []
    try:
        SD_ = Manager().list([SD_[a] for a in range(2**8)]) # copy of org SD_
        with Pool() as ps:
            for pr in ps.map(startp_, asms):
                prs.append(pr)
    except:
        print("***Err: This function only works in Linux***")
    return prs

def startfast(asm):
    """Load and Start fast running the aam code"""
    rc = load(asm)
    mx = 0 # run steps
    if rc != _Err:
        mx = runfast()
    return mx

def startfastp_(asm):
    """Load and Start running the aam code"""
    print(f'module: {__name__} ppid: {getppid()} pid: {getpid()}')
    rc = load(asm)
    mx = 0 # run steps
    if rc != _Err:
        mx = runfast()
        print(f"*{__name__} pid: {getpid()} done in {mx} steps *")
    return mx, R_


def startfasts(*asms):
    """Load and Start running multiple asm files in parallel
    *only work in linux* """
    global SD_ # share data
    prs = []
    try:
        SD_ = Manager().list([SD_[a] for a in range(2**8)]) # copy of org SD_
        with Pool() as ps:
            for pr in ps.map(startfastp_, asms):
                prs.append(pr)
    except:
        print("***Err: This function only works in Linux***")
    return prs
    

def save(ps, fname=None):
    """save compiled asm codes in py file"""
    # (1) compile
    # (2) save

    bret = bcompile(ps)
    if bret == _Err:
        print("*** Save Stop: Compile error ***")
        return _Err
    (fname0, pl) = bret

    fname = fname0 if fname is None else fname
    
    try:
        fout = open(fname+'.py', 'x')
    except FileExistsError:
        print(f'Save Stop: {fname}.py file exists')
        return _Err
    
    # saving ps org
    fout.write(fname+'asm = """\n')
    fout.write(ps)
    fout.write('"""\n\n')
    
    # saving compiled codes
    fout.write(fname+'_ = """\n')
    for aline in pl:
        fout.write(aline+'\n')
    fout.write('"""\n\n')    
    
    fout.close()
    print(f"{fname}.py write completed")

# ready
print(f"*** BCPU {_VER} startup completed ***")

# testing ===

#if __name__ == '__main__':
#    testprog = """
#    Set(R1, 7)

#    # logical operation
#    Move(R2, R1)  # R2=R1
#    Not(R3, R2) # R3=NOT(R2)
#    And(R4, R1, R1) # R4= R1 AND R1
#    Or(R5, R3, R4) # R5 = R3 OR R4
#    
#      # arithmetic operation
#      Add(R7, R1, R1) # R7=R1+R1
#      Sub(R8, R7, R2) # R8 = R7 - R2
#      Addi(R9, R8, 2) # R9=R8+2
#      Subi(R10, R9, 0x3) # 0x hex no.

#    Set(R11, 42)  # R11=42
#    Seth(R12, 0b1111) # 0b bin no.

#      Store(R1, R11) # R1 is address to store data in R11
#      Load(R6,R1) # R6 is data load from address R1

#    # conditional operation
#    Movez(R13, R2, R0) # R12=R2 if R0 = 0
#    Movex(R13, R3, R1) # R13=R3 if R1 != 0
#    Movep(R14, R3, R1) # R14=R3 if R1>=0
#    Moven(R10, PC, R3) # R10 = PC if R3<0
#    """

#    # testing process
#    print("...Loading asm program into memory...")
#    load(testprog)
#    printm()
#    printr()
#    print("...Runing test program...")
#    run()
#    printr()
#    printd()

#    # pp
#    pt0 = """
#    Set(r0, 100)
#    Set(r1, 0)
#    Seth(r1, SDS)
#    Store(r1,r0)
#    Load(r11, r1)
#    """
#    pt1 = """
#    Set(r0, 101)
#    Set(r1, 1)
#    Seth(r1, SDS)
#    Store(r1,r0)
#    Load(r11, r1)
#    """
#    pt2 = """
#    Set(r0,202)
#    Set(r1, 2)
#    Seth(r1, SDS)
#    Store(r1,r0)
#    Load(r12, r1)
#    """
#    pt4 = """
#    Set(ar, 0)
#    Seth(ar, SDS)
#    Load(r0, ar)
#    Set(ar, 1)
#    Seth(ar, SDS)
#    Load(r1, ar)
#    Set(ar, 2)
#    Seth(ar, SDS)
#    Load(r2, ar)
#    Add(r3,r0,r1)
#    Add(r3,r3,r2)
#    Set(ar, 3)
#    Seth(ar, SDS)
#    Store(ar,r3)
#    """
#    pt11 = """
#    Set(r0, 111)
#    Set(r1, 4)
#    Seth(r1, SDS)
#    Store(r1,r0)
#    Load(r11, r1)
#    """
#    pt12 = """
#    Set(r0, 112)
#    Set(r1, 5)
#    Seth(r1, SDS)
#    Store(r1,r0)
#    Load(r11, r1)
#    """
#    print(f'module: {__name__} ppid: {getppid()} pid: {getpid()}')
#    start(pt0)
#    printr()
#    printsd(0,15)
#    startfasts(pt1,pt2)
#    printsd(0,15)
#    printr()
#    start(pt4)
#    printr()
#    printsd(0,15)
#    starts(pt12, pt11)
#    printsd(0,15)

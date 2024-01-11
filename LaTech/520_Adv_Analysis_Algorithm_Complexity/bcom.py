"""
# BCOM (C) Pr Ben Choi
# Building COMputer
#     Simulated as UTM
# 	Code, Run TM

# TM descriptions
# tape: require def: T, rwh
T = "input string"
rwh = 0  # read write head initial location

q0 = 0  # startup state
# def delta function as dict 
df = {(q,ins):(qn,outs,move), ....}
# present_state q, input_str map to
# next_state qn, outpu_str, move_rwh
"""
VER = 1.5

# require def: b, 'halt', 1, -1
b = '_'  # b for blank chr
h = 'halt'  # 'halt' for halt_state
R = 1  # 1 for move rwh right
L = -1  # -1 for move rwh left

def Utm(T:str, df:dict, rwh=0, q0=0)-> (str,int):
  """ Universal Turing Machine """
  Tl = list(T) # tape as list of chr
  # make sure ins, outs are str
  df = dict(((q, str(ins)),(qn,str(outs),move)) for ((q,ins),(qn,outs,move)) in list(df.items()))
  
  q = q0 # present state q
  while q != 'halt':
    # add a blank when needed
    if rwh < 0: 
      Tl = [b] + Tl
      rwh = 0
    elif rwh >= len(Tl):
      Tl = Tl + [b]
      rwh = len(Tl) - 1
    
    # 5 steps for UTM
    ins = Tl[rwh] # read ins
    qn, outs, move = df[(q, ins)]
    Tl[rwh] = outs # write outs
    q = qn # next state qn
    rwh += move # read_write head
    
  # done
  T = ''.join(Tl) # list to tape str
  return T, rwh


def run(T:str, df:dict, rwh=0, q0=0)-> (str,int, int):
  """ Run TM with step limit """
  MAXSTEPS = 99999 #  steps limit  in case infinite loop
  steps = 0
  print(T, rwh,  steps)
  Tl = list(T) # tape as list of chr
  # make sure ins, outs are str
  df = dict(((q, str(ins)),(qn,str(outs),move)) for ((q,ins),(qn,outs,move)) in list(df.items()))
  
  q = q0 # present state q
  while q != 'halt' and steps<=MAXSTEPS:
    # add a blank when needed
    if rwh < 0: 
      Tl = [b] + Tl
      rwh = 0
    elif rwh >= len(Tl):
      Tl = Tl + [b]
      rwh = len(Tl) - 1
    
    # 5 steps for UTM
    ins = Tl[rwh] # read ins
    if (q,ins) not in df:
    	print(f"***Error: missing {(q,ins)} in df ***")
    	break
    qn, outs, move = df[(q, ins)]
    Tl[rwh] = outs # write outs
    q = qn # next state qn
    rwh += move # read_write head
    
    #  done a step 
    steps += 1
  
  #  done run loop
  if q == 'halt': 
  	print("Halt",  steps)
  else: 
  	steps = -steps #  - to indicate not halt
  	print("***Not halt***",  steps)
  
  # done
  T = ''.join(Tl) # list to tape str
  print(T, rwh,  steps)
  return T, rwh, steps


def start(T:str, df:dict, rwh=0, q0=0)-> (str,int, int):
  """ Start runing TM, print each steps """
  MAXSTEPS = 99999 #  steps limit  in case infinite loop
  steps = 0
  print(T, rwh,  steps)
  Tl = list(T) # tape as list of chr
  # make sure ins, outs are str
  df = dict(((q, str(ins)),(qn,str(outs),move)) for ((q,ins),(qn,outs,move)) in list(df.items()))
  
  q = q0 # present state q
  while q != 'halt' and steps<=MAXSTEPS:
    # add a blank when needed
    if rwh < 0: 
      Tl = [b] + Tl
      rwh = 0
    elif rwh >= len(Tl):
      Tl = Tl + [b]
      rwh = len(Tl) - 1
    
    # 5 steps for UTM
    ins = Tl[rwh] # read ins
    if (q,ins) not in df:
    	print(f"***Error: missing {(q,ins)} in df ***")
    	break
    qn, outs, move = df[(q, ins)]
    print(f"{(q,ins)}->{(qn,outs,'R' if move==1 else 'L')}  : {steps}")
    Tl[rwh] = outs # write outs
    q = qn # next state qn
    rwh += move # read_write head
    
    #  done a step 
    steps += 1
  
  #  done run loop
  if q == 'halt': 
  	print("Halt with steps:",  steps)
  else: 
  	steps = -steps #  - to indicate not halt
  	print("***Not halt*** with steps:",  steps)
  
  # done
  T = ''.join(Tl) # list to tape str
  print(T, rwh,  steps)
  return T, rwh, steps


# ready
print(f"*** BCOM {VER} startup completed ***")

""" eg TM file 
# in the TM file
# from bcom import *

# TM descriptions
# eg: parity tm def 

# tape: require def T, rwh
T = "01101"
rwh = 0

q0 = 0 # startup
# req def df (ps,ins):(ns,outs,move)
df = {(0,0):(0,0,R), (0,1):(1,1,R), (0,b):(2,b,R), 
(1,0):(1,0,R), (1,1):(0,1,R), (1,b):(3,b,R),
(2,b):(h,0,R), (3,b):(h,1,R)}

# testing
print(T,rwh)
print(Utm(T,df))

# """

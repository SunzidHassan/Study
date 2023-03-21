# Push 11
Set(cr, 11) # the value to be stored
Addi(st, st, 1) #store 1 index above the existing stack
Store(st, cr)

# push 22
Set(cr, 22) # the value to be stored
Addi(st, st, 1) #store 1 index above the existing stack
Store(st, cr)

# push 33
Set(cr, 33) # the value to be stored
Addi(st, st, 1) #store 1 index above the existing stack
Store(st, cr)

# push 44
Set(cr, 44) # the value to be stored
Addi(st, st, 1) #store 1 index above the existing stack
Store(st, cr)
printd()

# pop into r1
Load(r1, st) # get the top stack and put it into r1
Subi(st, st, 1) # Pop the topmost value out
printr(1)
printd()

# pop into r2
Load(r2, st) # get the top stack and put it into r1
Subi(st, st, 1) # Pop the topmost value out
printr(2)
printd()

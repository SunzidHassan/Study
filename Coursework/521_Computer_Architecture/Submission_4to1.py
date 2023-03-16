# r1 = 0b1100_1111_1100_0111
Set(r1, 0b1100_0111)
Seth(r1, 0b1100_1111)
printrb(1)

#Put your code here to set r1 bit 4 to 1 using Mask
Set(r2, 0b0001_0000)
Or(r1, r1, r2)
printrb(r1)
# r1 = 0b1100_1111_1100_0111
Set(r1, 0b1100_0111)
Seth(r1, 0b1100_1111)
printrb(1)

# clear r1 bit 8 and bit 10 to 0
Set(r2, 0b1100_0111)
Seth(r2, 0b1100_1010)

# put your code here
And(r1, r1, r2)
printrb(1)
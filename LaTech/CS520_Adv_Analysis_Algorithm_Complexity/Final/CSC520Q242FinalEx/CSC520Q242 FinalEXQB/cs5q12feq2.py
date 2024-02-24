myTechEmail = 'sha040' #only your email id emailID@latech.edu
# cannot contain syntax error

# 20 points

"""
In math, natural numbers can be defined as sets within sets.
In Python, we will define natural numbers as lists within lists.
Define a fuction using lambda to map:
0 to []
1 to [[]]
2 to [[], [[]]]
3 to [[], [[]], [[], [[]]]]
... and so on
"""
# Note: using only one line of code to get that done!

Nl = lambda n: None if n < 0 else [] if n < 1 else Nl(n-1) + [Nl(n-1)]


# test your code with numbers less then 10 as this def is computational costly
if __name__ == "__main__":
    # your testing codes inside this if
    print(Nl(0))
    print(Nl(1))
    print(Nl(2))
    print(Nl(3))
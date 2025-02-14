myTechEmail = 'sha040' #only your email id emailID@latech.edu
from bcom import *

# 15 points

# cannot contain syntax error

# 1. This question is based on your state diagram on part A question 1.
# Based on your state diagram, code a TM, that can be run on bcom.

Q1q0 = 0 # e.g. Q1q0 = 0


Q1df = {
    (0, 'A'): (1, 'a', 1),
    (0, 'B'): (2, 'b', 1),
    (0, '_'): (6, '_', -1),
    
    (1, 'A'): (1, 'A', 1),
    (1, 'B'): (1, 'B', 1),
    (1, '_'): (3, '_', 1),
    
    (2, 'A'): (2, 'A', 1),
    (2, 'B'): (2, 'B', 1),
    (2, '_'): (4, '_', 1),
    
    (3, 'A'): (3, 'A', 1),
    (3, 'B'): (3, 'B', 1),
    (3, '_'): (5, 'A', -1),
    
    (4, 'A'): (4, 'A', 1),
    (4, 'B'): (4, 'B', 1),
    (4, '_'): (5, 'B', -1),
    
    (5, 'A'): (5, 'A', -1),
    (5, 'B'): (5, 'B', -1),
    (5, '_'): (5, '_', -1),
    (5, 'a'): (0, 'a', 1),
    (5, 'b'): (0, 'b', 1),
    
    (6, 'a'): (6, 'A', -1),
    (6, 'b'): (6, 'B', -1),
    (6, '_'): (h, '_', 1)} # Q1df is a dict


if __name__ == '__main__':
    # your testing codes within this if
    T1 = "AABBBA"
    result_tape, result_rwh = Utm(T1, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T2 = "BBBBBB"
    result_tape, result_rwh = Utm(T2, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T3 = "AAAAAA"
    result_tape, result_rwh = Utm(T3, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T4 = "ABABAB"
    result_tape, result_rwh = Utm(T4, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T6 = "A"
    result_tape, result_rwh = Utm(T6, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T7 = "B"
    result_tape, result_rwh = Utm(T7, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T5 = ""
    result_tape, result_rwh = Utm(T5, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code

    T8 = "_"
    result_tape, result_rwh = Utm(T5, Q1df, 0, Q1q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh) # replay this line with your code




myTechEmail = 'sha040' #only your email id, omit @latech.edu
from bcom import *

# 15 points

# 2(b). This question is based on your state diagram on part A 2(a).
# Based on your state diagram, code a TM, that can be run on bcom.py. 

Q2q0 = 0

Q2df = {
    (0, '0'): (0, '0', 1),
    (0, '1'): (1, '1', 1),
    (0, '2'): (2, '2', 1),
    (0, '_'): (3, '_', 1),

    (1, '0'): (1, '0', 1),
    (1, '1'): (1, '1', 1),
    (1, '2'): (2, '2', 1),
    (1, '_'): (4, '_', 1),

    (2, '0'): (2, '0', 1),
    (2, '1'): (2, '1', 1),
    (2, '2'): (2, '2', 1),
    (2, '_'): (5, '_', 1),

    (3, '_'): (h, '0', 1),
    (4, '_'): (h, '1', 1),
    (5, '_'): (h, '2', 1),
}

if __name__ == '__main__':
    result_tape, result_rwh = Utm("01211", Q2df, q0=Q2q0)
    print("Result Tape:", result_tape)
    print("Final Read-Write Head Position:", result_rwh)
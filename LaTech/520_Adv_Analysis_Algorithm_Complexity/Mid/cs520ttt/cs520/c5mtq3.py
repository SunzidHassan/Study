myTechEmail = 'sha040' #only your email id, omit @latech.edu

# 15 points

def implies():
    # return a true table for "A implies B"
    # where A, B, can be True or False
    Z = {False,True}
    permutations = [(y3, y2, y1, y0) for y3 in Z for y2 in Z for y1 in Z for y0 in Z]
    functions = [{(a,b):y[2*a+b] for a in Z for b in Z} for y in permutations]

    impliesTT = functions[13] # e.g. {(Flase,Flase):True, ...}
    return impliesTT # note: returning a dict

def imply(A, B):
    # define a function that return the result of "A implies B"
    return not A or B

if __name__ == '__main__':
    # your testing codes within this if
    implies_table = implies()
    print("Implies Truth Table:", implies_table)

    # Testing imply function
    test_cases = [(False, False), (False, True), (True, False), (True, True)]
    print("\nTesting the imply function:")
    for A, B in test_cases:
        result = imply(A, B)
        print(f"A: {A}, B: {B} => A implies B: {result}")
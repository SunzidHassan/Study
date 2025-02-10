# Provide your information as the values of these variables:
myName = 'Sunzid, Hassan'
myTechID = '10407862'
myTechEmail = 'sha040' #only your email id omit @latech.edu
###########################################################

import sys
from hashSet import HashSet

def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
    
  return col

def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])
        
  return square

def getGroups(matrix):
  groups = []
  # get rows
  for i in range(9):
    groups.append(list(matrix[i]))
  # get columns
  for i in range(9):
    groups.append(getColumn(matrix,i))
  # get squares
  # squares are processed left-right, up-down
  for i in range(0,9,3): 
    for j in range(0,9,3):
      groups.append(getSquare(matrix,i,j))     

  return groups

def cardinality(x):
  return len(x)

def rule1(group):
  changed = False
  for i in range(len(group)):
    if cardinality(group[i]) < 9: # if cardinality of the set is less than 9
      d = 1 # set duplicate counter to 1
      for j in range(len(group)):
        if (group[i] != group[j]) and (group[i]).issuperset(group[j]) and (group[j]).issuperset(group[i]):  # check duplicate
            d += 1 # increase duplicate counter
      if cardinality(group[i]) == d: # if duplicates = cardinality
        for k in range(len(group)):
          if group[k] != group[i]: # if they're not the same set
            if not(group[i].issuperset(group[k]) and group[k].issuperset(group[i])): # if they're not duplicate
              if cardinality(group[k]) > 1: # if cardinality of the set to be updated is greater than 1
                group[k].difference_update(group[i]) # update the set
                changed = True
              else:
                changed = False
  return changed
  
def rule2(group):
  changed = False
  temp = HashSet()

  for i in range(len(group)):
    n = cardinality(group[i]) # cardinality of current set
    if n > 1:
      temp.clear()
      temp.update(group[i]) # record the current set
      t = 0
      for j in range(len(group)):
        if group[j] != group[i]: # if ith and jth element is not the same:
          temp.difference_update(group[j])
      t = cardinality(temp) # check cardinality of t
      if (t > 0) and (t < n): # if cardinality of temp is greater than 0
        group[i].clear()
        group[i].update(temp)

  return changed

def reduceGroup(group):
  changed = False 
  # this sorts the sets from smallest to largest based cardinality
  group.sort(key=cardinality)
  changed = rule2(group)
  changed = rule1(group)
  
  return changed

def reduceGroups(groups):
  changed = False
  for group in groups:
    if reduceGroup(group):
      changed = True
      
  return changed

def reduce(matrix):
    changed = True
    groups = getGroups(matrix)
    
    while changed:
        changed = reduceGroups(groups)

def printMatrix(matrix):
  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) != 1:
        sys.stdout.write("x ")
      else:
        for k in matrix[i][j]:
          sys.stdout.write(str(k) + " ")

    sys.stdout.write("\n")

def main():
  file = open("test-3.txt", "r")
  matrix = []

  for line in file:
    lst = line.split()
    row = []

    for val in lst:
      if val == 'x':
        s = HashSet(range(1,10))
      else:
        s = HashSet([eval(val)])
      row.append(s)

    matrix.append(row)

  print("Solving this puzzle:")
  printMatrix(matrix)

  reduce(matrix)  

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()

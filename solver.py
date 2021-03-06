'''  
  Backtracking program in python to solve any given Soduko
'''

# check the given Sodoku array in a specific row for the same number
def check_row (arr, row, num):
  for i in range(9):
    if arr[row][i] == num:
      return False
  return True


# check the given Sodoku array in a specific column for the same number
def check_column (arr, col, num):
  for i in range(9):
    if arr[i][col] == num:
      return False
  return True


# check for matches with the assigned number in its 3X3 box
def check_box (arr, row, col, num):
  rowStart = (row/3) * 3
  colStart = (col/3) * 3
  for i in range(3):
    for j in range(3):
      if arr[rowStart + i][colStart + j] == num:
        return False
  return True


# check if number is valid 
# AKA no match in row, column and box
# if there's no match returns true
# if there's another entry with the same number returns false
def is_safe(arr, row, col, num):
  return check_row(arr, row, num) and check_column(arr, col, num) and check_box(arr, row, col, num)


# find the next unassigned entry 
def find_unassigned_entry(arr, unassigned):
  for r in range(9):
    for c in range(9):
      if arr[r][c] == 0:
        unassigned[0] = r
        unassigned[1] = c
        return True
  return False


# main recursive function
# arr: partially filled in grid, where unassigned entries are digit 0
def solve(arr):
  # initialize the unassigned entry to location 0,0
  unassigned = [0, 0]

  # if there are no more empty spots we're done
  if not find_unassigned_entry(arr, unassigned):
    return True


  row = unassigned[0]
  col = unassigned[1]

  for i in range(1, 10):
    if is_safe(arr, row, col, i):

      arr[row][col] = i

      if solve(arr):
        return True

      # if recursion failed, reset the entry
      arr[row][col] = 0

  # if the grid is unsolvable, backtrack
  return False


def print_solved_soduko(arr):
  for i in range(9):
    for j in range(9):
      print arr[i][j],
    print '\n'


if __name__ == "__main__":
  arr = [[0 for x in range(9)] for y in range(9)]

  test = [[0,0,0,2,6,0,7,0,1],
          [6,8,0,0,7,0,0,9,0],
          [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0],
          [0,0,4,6,0,2,9,0,0],
          [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4],
          [0,4,0,0,5,0,0,3,6],
          [7,0,3,0,1,8,0,0,0]]

  if solve(test):
    print_solved_soduko(test)
  else:
    print "Sorry! I was unable to find a solution for this test"



  



""" 
Soduko Solver
Usage: python main.py <filename>
where <filename> is the name of the file containing the Soduko matrix.
"""
import sys
import getopt
import solver 

class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

# make a 2D matrix from an input file
def parseGrid(filename):
  file = open(filename, 'r')
  arr = [ map(int, line.split(',')) for line in file ]
  return arr

def main(argv=None):
  if argv is None:
    argv = sys.argv

  #parse command line options
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "h", ["help"])
    except getopt.error, msg:
      raise Usage(msg)
    for o,a in opts:
      if o in ("-h", "--help"):
        print __doc__
        return 0
    if (len(args) != 1):
      raise Usage("A single file name argument is required")
    filename = args[0]

    grid = parseGrid(filename)
    if not grid: 
      print "Failure: Unable to parse file! please make sure the format of file is correct."
    else:
      if solver.solve(grid):
        solver.print_solved_soduko(grid)
      else:
        print "Sorry! I was unable to find a solution for this test"
  
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "For help use --help"
    return 2


if __name__ =="__main__":
  sys.exit(main())
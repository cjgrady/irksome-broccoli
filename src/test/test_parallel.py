"""
@summary: Tests for serial Dijstra single tile
@author: CJ Grady
@status: alpha
"""
import time

from singleTile.parallelDijkstra import SingleTileParallellDijkstraLCP

# .............................................................................
if __name__ == "__main__":
   
   #inFn = '/home/cjgrady/git/irksome-broccoli/testData/testGrid.asc'
   inFn = '/home/cjgrady/thesis/fl_east_gom_crm_v1.asc'
   #outFn = '/home/cjgrady/git/irksome-broccoli/testData/paralleloutputGrid4.asc'
   outFn = '/home/cjgrady/thesis/testOut.asc'
   
   def costFn(i, x, y, z):
      c = max(i, y)
      #print i, x, y, z, c
      return c
   
   #costFn = lambda x,y,z: min(x,y)
   a = time.clock()
   t1 = SingleTileParallellDijkstraLCP(inFn, outFn, costFn)
   
   t1.findSourceCells()
   
   print "t1"
   print t1.sourceCells
   t1.setStepSize(100)
   
   print "Attempting to calculate"
   t1.calculate()
   
   b = time.clock()
   
   print b-a
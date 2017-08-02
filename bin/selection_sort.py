#!/usr/bin/env python
#=======================================================================
#  Statement:
#  Given a disordered list of integers (or any other items),
#  rearrange the integers in natural order.
#
#  Sample Input: [18,5,3,1,19,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,18,19]
#
#  Time Complexity of Solution:
#  Best O(n^2); Average O(n^2); Worst O(n^2).
#
#  Approach:
#  Selection sort is a step up from insertion sort from a memory
#  viewpoint. It only swaps elements that need to be swapped. In terms
#  of time complexity, however, insertion sort is better.
#======================================================================= 
def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    # System.out.println("i: " + i + " min: " + minIndex);
    print ("i: %s min: %s" % (i, least))
    for k in range( i + 1 , len( aList ) ):
      print k
      # print aList[k], aList[least]  
      if aList[k] < aList[least]:
        print "curMin: " + str(least) + " newMin: " + str(k)
        least = k
        
    swap( aList, least, i )
    print A
    
  return A
     
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

A =  [18,5,3,1,19,6,0,7,4,2,5]  
print A
print selectionsort(A)

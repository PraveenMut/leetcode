# Squash into a 1D Array and conduct a binary search.
# Squashing time Complexity = O(n)
# Binary Search time complexity = O(log(n))
# Total Time complexity = O(log(n)) + O(n) => Ω(n)
from typing import List
import unittest

def flatten(ary_of_ary):
    flattened_list = []
    for ary in ary_of_ary:
      flattened_list += ary
    return flattened_list


def bin_search(ary, target):
  lower = 0
  upper = len(ary)-1
  if target > ary[-1]: return False
  if target < ary[0]: return False
  while lower <= upper:
    pivot = lower+(upper-lower)//2
    if ary[pivot] == target:
      return True
    elif ary[pivot] < target:
      lower = pivot + 1
    else:
      upper = pivot - 1
  return False

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return bin_search(flatten(matrix),target)

test_cases = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)
    ]

class TestSolution(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(Solution().searchMatrix(matrix=test_cases[0][0],target=test_cases[0][1]),True)
    def test_sad(self):
        self.assertEqual(Solution().searchMatrix(matrix=test_cases[1][0],target=test_cases[1][1]),False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
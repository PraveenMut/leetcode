# Squash into a 1D Array and conduct a binary search.
# Squashing time Complexity = O(n)
# Binary Search time complexity = O(log(n))
# Total Time complexity = O(log(n)) + O(n) => Ω(n)
from typing import List, Optional
from collections import namedtuple
import unittest
from xml.dom import NotFoundErr

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


class LinearSolution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return bin_search(flatten(matrix),target)

class LogarithmicSolution:
  _matrix: Optional[list] = None
  _target: Optional[int] = None

  '''
  _Synthentically_ search through the 2D matrix
  as if it were a 1D array.
  '''
  def synthetic_bin_search(self, lower: int, upper: int):
    if lower > upper:
      return False

    mid = (lower + upper) // 2
    elements_length = len(self._matrix[0])
    row, column = divmod(mid,elements_length)
    current_value = self._matrix[row][column]

    if self._target == current_value:
      return True

    if self._target < current_value:
      return self.synthetic_bin_search(lower, mid - 1)
    elif self._target > current_value:
      return self.synthetic_bin_search(mid + 1, upper)

    raise RuntimeError("Value was not found or an unexpected exception has occured")

  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    self._matrix = matrix
    self._target = target
    total_elements = (len(matrix[0]) * len(matrix)) - 1
    if target > matrix[-1][-1] or target < matrix[0][0]: return False
    self.synthetic_bin_search(0,  total_elements)


TestCase = namedtuple("TestCase", "case target")

case1 = TestCase([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
case2 = TestCase([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)

# test_cases = [
#     ([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3),
#     ([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)
#     ]

class TestSolution(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(LinearSolution().searchMatrix(matrix=case1.case,target=case1.target),True)
        self.assertEqual(LogarithmicSolution().searchMatrix(matrix=case1.case,target=case1.target),True)
    def test_sad(self):
        self.assertEqual(LinearSolution().searchMatrix(matrix=case2.case,target=case2.target),False)
        self.assertEqual(LogarithmicSolution().searchMatrix(matrix=case2.case,target=case2.target),False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
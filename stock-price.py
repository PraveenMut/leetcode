# To test
# arr = [random.randrange(1,10000) for i in range(0,100000)]

# naive af solution
def maxProfit(prices):
  min_price = min(prices)
  max_price = max(prices)
  index_min = prices.index(min_price)
  index_max = prices.index(max_price)
  while index_min > index_max:
    if len(prices) == 1:
      return 0
    prices.pop(index_max)
    max_price = max(prices)
    index_max = prices.index(max_price)
  
  return max_price - min_price


# clean solution by slicing the array from min_index at O(n), that being t0
# and then finding the max at O(n). Thus 2 * O(n)
def sliceProfit(prices):
  min_price_index = prices.index(min(prices))
  constrained_prices = prices[min_price_index:]
  return max(constrained_prices) - constrained_prices[0]


# Use logical deduction whereby the delta of the prices cannot be less than 0
# Thus, the best output becomes from employing and (i,j) tuple kind of mindset
# where the max_delta (output or result) becomes maximum of the current max delta
# and the found max delta by comparing 2 values.

# Note that this is now O(n) as the min and max comparisons are not on iterables

def compareProfit(prices):
  max_delta = 0
  min_iter = prices[0]
  for price in prices:
    min_iter = min(min_iter, price)
    max_delta = max(max_delta, price - min_iter)
  return max_delta

# Recursive approach
# I'm tired af. Do it later.


# Functional Programming Approach
# I dunno, for fun? later.

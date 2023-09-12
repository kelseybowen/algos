# REMOVE DUPLICATES FROM SORTED ARRAY
def removeDuplicates(nums):
    k = 0
    for i in range(len(nums))[1:]:
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k+1

# BEST TIME TO BUY AND SELL STOCK II
def maxProfit(prices):
    profit = 0
    curr = 0
    future = 1
    while future < len(prices):
        if prices[future] > prices[curr]:
            diff = prices[future] - prices[curr]
            profit += diff
        curr += 1
        future += 1
    return profit

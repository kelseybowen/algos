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

# REVERSE ARRAY
def reverse_array(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = 0, k -1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

# CONTAINS DUPLICATE
def containsDuplicate(nums):
        nums.sort()
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            else:
                l += 1
                r += 1
        return False

# INTERSECTION OF ARRAYS II
def intersect(nums1, nums2):
    count = {}
    result = []
    for num in nums1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in nums2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result
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

# PLUS ONE
def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        str_dig = ""
        for dig in digits:
            str_dig += str(dig)
        res = int(str_dig) + 1
        digits = []
        for dig in str(res):
            digits.append(int(dig))
    return digits

# MOVE ZEROES
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == 0:
            count += 1
            nums.pop(i)
        else:
            i += 1
    for i in range(count):
        nums.append(0)
    # slower solution
    # l, r = 0, 1
    # while r < len(nums):
    #     if nums[l] == 0:
    #         if nums[r] == 0:
    #             r += 1
    #             continue
    #         else:
    #             nums[l], nums[r] = nums[r], nums[l]
    #             l += 1
    #     else:
    #         l += 1
    #     r += 1

# TWO SUM
def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in seen:
            return [seen[comp], i]
        else:
            seen[nums[i]] = i

# MAX DEPTH OF BINARY TREE
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
    maxDep = 1
    def maxDepth(self, root):
        if not root:   
            return 0
        
        def dft(root, depth):
            if root.left:
                dft(root.left, depth+1)
            if root.right:
                dft(root.right, depth+1)
            if depth > self.maxDep:
                self.maxDep = depth

        dft(root, 1)
        return self.maxDep
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

# VALID BINARY SEARCH TREE
class Solution:
    curr = None
    def isValidBST(self, root):
        if root.val == None:
            return False
        
        def inOrder(root):
            isValid = True
            if root.left:
                if not inOrder(root.left):
                    isValid = False
                    
            if self.curr == None or self.curr < root.val:
                self.curr = root.val
            else:
                isValid = False
                
            if root.right:
                if not inOrder(root.right):
                    isValid = False
            return isValid
            
        return inOrder(root)

# SYMMETRICAL TREE
def isSymmetric(self, root):
    
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return(left.val == right.val and 
                dfs(left.left, right.right) and
                dfs(left.right, right.left))
        
    return dfs(root.left, root.right)

# BINARY TREE LEVEL ORDER TRAVERSAL
def levelOrder(self, root):
    result = []
    level = 0
    
    def lot(root, level):
        if root:
            if len(result) < level+1:
                result.append([])
        
            result[level].append(root.val)
            if root.left:
                lot(root.left, level+1)
            if root.right:
                lot(root.right, level+1)
        return result
        
    return lot(root, level)

# SORTED ARRAY TO BST
def sortedArrayToBST(self, nums):
    
    def helper(l, r):
        if l > r:
            return None
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = helper(l, m-1)
        root.right = helper(m+1, r)
        return root
    
    return helper(0, len(nums)-1)

# MERGE SORTED ARRAY
def merge(self, nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last = m + n - 1
    
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1
    
    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1
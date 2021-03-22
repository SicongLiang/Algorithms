# -*- coding: UTF-8 -*-
# =================================================='''
# 35.搜索插入位置 https://leetcode-cn.com/problems/search-insert-position/
# @Author ：Sicong LIANG
# @Date   ：2021/3/13 9:51
# =================================================='''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bsearch(nums, len(nums), target)
    
    def bsearch(self, nums, n, target): # n 为数组长度，targe 为要找到的目标
        low = 0
        high = n - 1
        while low <= high:
            # mid = (low + high) / 2
            mid = low + ((high -low) >> 1) # 使用位运算，优化速度
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == n - 1 or nums[mid + 1] > target: # # 找到插入的位置
                    return mid + 1
                low = mid + 1 # 继续二分查找
            else:
                if mid == 0 or nums[mid - 1] < target: # 找到插入的位置
                    return mid
                high = mid -1 # 继续二分查找
        return -1 # 未找到
    
    # 二分查找，时间复杂度：O(logn)，空间复杂度：O(1)

# Testing
test = Solution()
print(test.searchInsert([1,3,5,6], 0))  # 0
print(test.searchInsert([1,3,5,6], 2))  # 1
print(test.searchInsert([1,3,5,6], 5))  # 2
print(test.searchInsert([1,3,5,6], 7))  # 4


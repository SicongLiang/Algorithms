# -*- coding: UTF-8 -*-
# =================================================='''
# 35.搜索插入位置 https://leetcode-cn.com/problems/search-insert-position/
# @Author ：Sicong LIANG
# @Date   ：2021/3/13 9:51
# =================================================='''
class Solution:
    def searchInsert(self, nums, target):
        return self.bsearch(nums, len(nums), target)
    
    # Using binary search algorithm
    def bsearch(self, nums, n, target):
        low = 0
        high = n - 1
        while low <= high:
            # mid = (low + high) / 2
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == n - 1 or nums[mid + 1] > target:
                    return mid + 1
                low = mid + 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                high = mid - 1
        return -1

# Testing
test = Solution()
print(test.searchInsert([1,3,5,6], 0))  # 0
print(test.searchInsert([1,3,5,6], 2))  # 1
print(test.searchInsert([1,3,5,6], 5))  # 2
print(test.searchInsert([1,3,5,6], 7))  # 4

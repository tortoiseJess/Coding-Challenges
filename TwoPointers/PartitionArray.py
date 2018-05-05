"""
cat: Two Pointers
idea:
arr = like a wall such that elements after it is greater/equal to target
the other pointer is just runs through the whole array, 
each iteration, we evalute the subarray up till the runner
If the new number is smaller than the target, swap the element in the wall index with this smaller number. 
the wall index is shifted to the right by 1
cases:
[1,2,3,4] target = 4 or 5
[1,4,2,3], target =2 
[1,1,,1], target =1
"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Note:
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
If all elements in nums are smaller than k, then return nums.length

Example:
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge:
partition the array in-place and in O(n)
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        arr = 0
        for i in range(0, len(nums)):
            if nums[i] < k:
                tmp = nums[i]
                nums[i] = nums[arr]
                nums[arr] = tmp
                arr +=1
        return arr
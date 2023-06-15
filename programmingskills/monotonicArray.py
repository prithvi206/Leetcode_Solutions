# 896. Monotonic Array


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        low=0
        high=len(nums)-1
        if nums[low]<nums[high]:
            for i in range(high):
                if nums[i]>nums[i+1]:
                    return False
        else:
            for i in range(high):
                if nums[i]<nums[i+1]:
                    return False
        return True
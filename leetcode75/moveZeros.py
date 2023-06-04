# 283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0 and nums[slow] == 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]

            if nums[slow]!=0:
                slow+=1
        return nums
# 11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        current =0
        l=0
        r = len(height)-1
        while l<r:
            current = (r-l) * min(height[l],height[r])
            max_area = max(current,max_area)
            if(height[l]<=height[r]):
                l+=1
            else:r -=1
        return max_area

import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        while low<=high:
            total=0
            mid=low+(high-low)//2
            for num in nums:
                total+=((num+mid-1)//mid)
            if total<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low

        
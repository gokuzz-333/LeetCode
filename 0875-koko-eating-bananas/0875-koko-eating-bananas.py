class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        while low<=high:
            total=0
            mid=low+(high-low)//2
            for num in piles:
                total+=((num+mid-1)//mid)
            if total<=h:
                high=mid-1
            else:
                low=mid+1
        return low
        
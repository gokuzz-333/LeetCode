class Solution(object):
    def possible(self,nums,t):
        count=1
        sum=0
        for num in nums:
            if sum+num>t:
                count+=1
                sum=num
            else:
                sum+=num
        return count
    def splitArray(self, nums, k):
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.possible(nums,mid)>k:
                low=mid+1
            else:
                high=mid-1
        return high+1

        
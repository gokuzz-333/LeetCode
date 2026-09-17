class Solution(object):
    def maxProduct(self, nums):
        suff=1
        pref=1
        n=len(nums)
        ans=float('-inf')
        for i in range(0,n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[n-i-1]
            ans=max(ans,max(suff,pref)) 
        return ans
        
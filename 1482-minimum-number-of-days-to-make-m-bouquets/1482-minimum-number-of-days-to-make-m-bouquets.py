class Solution(object):
    def possible(self,bloomDay,day,k):
        count=0
        b=0
        for num in bloomDay:
            if num<=day:
                count+=1
            else:
                b+=count//k
                count=0
        b+=count//k
        return b
    def minDays(self, bloomDay, m, k):
        if len(bloomDay)<m*k:
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=max(bloomDay)
        while(low<=high):
            mid=low+(high-low)//2
            if(self.possible(bloomDay,mid,k)>=m):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
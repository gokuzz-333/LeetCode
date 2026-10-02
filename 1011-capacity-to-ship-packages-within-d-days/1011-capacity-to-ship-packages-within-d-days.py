class Solution(object):
    def possible(self,weights,cap):
        load=0
        day=1
        for w in weights:
            if load+w>cap:
                day+=1
                load=w
            else:
                load+=w
        return day
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=low+(high-low)//2
            if(self.possible(weights,mid)<=days):
                high=mid-1
            else:
                low=mid+1
        return low
        
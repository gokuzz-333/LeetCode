class Solution(object):
    def findMin(self, arr):
        ans=100000
        n=len(arr)
        low=0
        high=n-1
        ind=-1
        while low<=high:
            mid=(low+high)//2
            if arr[low]<=arr[mid]:
                ind=low
                ans=min(ans,arr[low])
                low=mid+1
            else:
                ind=mid
                ans=min(ans,arr[mid])
                high=mid-1
        return ans
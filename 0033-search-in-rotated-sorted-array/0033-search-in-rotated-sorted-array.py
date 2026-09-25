class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target<=nums[high] and target>=nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        return -1 



        
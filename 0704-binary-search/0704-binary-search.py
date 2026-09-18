class Solution(object):
    def search(self, nums, target):
        high=len(nums)-1
        low=0
        while low<=high:
            mid=(low+high)/2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high=mid-1
            elif target>nums[mid]:
                low=mid+1

        return -1
        
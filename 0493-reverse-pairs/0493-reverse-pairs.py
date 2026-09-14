class Solution(object):
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        # Merge both sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted temp into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def countpairs(self,nums,low,mid,high):
        cnt=0
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and nums[i]>2*nums[right]:
                right+=1
            cnt+=(right-(mid+1))
        return cnt

    def mergeSort(self, arr, low, high):
        cnt=0
        if low >= high:
            return 0
        mid = (low + high) // 2
        
        cnt+=self.mergeSort(arr, low, mid)
        cnt+=self.mergeSort(arr, mid + 1, high)
        cnt+=self.countpairs(arr,low,mid,high)

        self.merge(arr, low, mid, high)
        return cnt

    def reversePairs(self, nums):
        n=len(nums)
        return self.mergeSort(nums,0,n-1)

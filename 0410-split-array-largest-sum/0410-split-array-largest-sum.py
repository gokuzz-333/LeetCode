class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            count = 1
            current = 0

            for num in nums:
                if current + num > mid:
                    count += 1
                    current = num
                else:
                    current += num

            if count > k:
                low = mid + 1
            else:
                high = mid - 1

        return low
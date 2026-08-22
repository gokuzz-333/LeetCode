class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        st = set(nums)
        max_count = 0
        for j in st:
            if (j - 1) not in st:
                count = 1
                while (j + count) in st:
                    count += 1
                max_count = max(max_count,count) 
                if max_count > n//2:
                    return max_count
        return max_count
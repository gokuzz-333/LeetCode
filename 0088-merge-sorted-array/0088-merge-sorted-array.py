class Solution(object):
    def merge(self, nums1, m, nums2, n):
        num=nums1[:m]+nums2
        num.sort()
        for i in range(m+n):
            nums1[i]=num[i]
        
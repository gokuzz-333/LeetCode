class Solution(object):
    def longestConsecutive(self, nums):
        num=set(nums)
        n=len(num)
        result=0
        for x in num:
            if x-1 not in num:
                y=x+1
                while y in num:
                    y=y+1
                result=max(result,y-x)
                if result>n//2:
                    return result
        return result


        
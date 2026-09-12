class Solution(object):
    def majorityElement(self, nums):
        el1=float('-inf')
        el2=float('-inf')
        count1=0
        count2=0
        for num in nums:
            if count1==0 and el2!=num:
                count1=1
                el1=num
            elif count2==0 and el1!=num:
                count2=1
                el2=num
            elif num==el1:
                count1+=1

            elif num==el2:
                count2+=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for num in nums:
            if num==el1:
                count1+=1
            elif num==el2:
                count2+=1

        mini=len(nums)//3+1
        result=[]
        if count1>=mini:
            result.append(el1)
        if count2>=mini and el2!=el1:
            result.append(el2)
        return result


        
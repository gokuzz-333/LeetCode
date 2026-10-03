class Solution:
    def findMedianSortedArrays(self, arr1: list[int], arr2: list[int]) -> float:
        if len(arr1)>len(arr2):
            return self.findMedianSortedArrays(arr2,arr1)
        n1=len(arr1)
        n2=len(arr2)
        low=0
        high=n1
        while low<=high:
            cut1=(low+high)//2
            cut2=((n1+n2+1)//2)-cut1

            if cut1==0:
                l1=float("-inf")
            else:
                l1=arr1[cut1-1]


            if cut2==0:
                l2=float("-inf")
            else:
                l2=arr2[cut2-1]

            if cut1==n1:
                r1=float("inf")
            else:
                r1=arr1[cut1]

            if cut2==n2:
                r2=float("inf")
            else:
                r2=arr2[cut2]
            
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=cut1-1
            else:
                low=cut1+1

class Solution(object):
    def nthrow(self,N):
        row=[]
        val=1
        row.append(val)
        for i in range(1,N):
            val=val*(N-i)
            val=val//i
            row.append(val)
        return row
    
    def generate(self, numRows):
        fans=[]
        for i in range(1,numRows+1):
            ans=self.nthrow(i)
            fans.append(list(ans))
        return list(fans)
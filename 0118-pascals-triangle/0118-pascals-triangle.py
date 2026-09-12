class Solution:

    def generate(self, r):
        result = []

        for i in range(1, r + 1):
            ans = [1]
            res = 1

            for col in range(1, i):
                res = res * (i - col)
                res = res // col
                ans.append(res)

            result.append(ans)

        return result
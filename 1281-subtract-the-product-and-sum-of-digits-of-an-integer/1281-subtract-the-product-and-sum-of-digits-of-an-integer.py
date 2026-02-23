class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        product = 1
        s = 0
        while temp>0:
            r  = temp%10
            product*=r
            s +=r
            temp//=10
        return product - s
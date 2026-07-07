class Solution:
    def reverse(self, x: int) -> int:
        ispos=x>=0
        x=abs(x)
        res=0
        while x>0:
            res=(res*10)+x%10
            x=x//10
        if ispos:
            if res<(2**31):
                return res
            else:
                return 0
        else:
            if -res>=-2**31:
                return -res
            else:
                return 0

        

class Solution:
    def hasDuplicate( self,num):
     y=len(num)
     for i in range(y):
        for j in range(i+1,y):
            if num[i]==num[j]:
                return True
     return False
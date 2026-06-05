class Solution:
    def isAnagram(self, s,t):
        o=len(s)
        p=len(t)
        if o!=p:
         return False
        
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        
        for i in range(o):
            if s_list[i] != t_list[i]:
                return False
        return True
#Lc problem link: https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        happy = 0
        i = j = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                happy += 1
                i += 1
                j += 1
            else:
                j += 1
        return happy
            

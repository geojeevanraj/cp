#lc problem link: https://leetcode.com/problems/get-equal-substrings-within-budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        left = 0
        running_cost = 0
        for right in range(len(s)):
            running_cost += abs(ord(s[right]) - ord(t[right]))
            while running_cost > maxCost:
                 running_cost -= abs(ord(s[left]) - ord(t[left]))
                 left += 1

            max_len = max(max_len,right - left + 1)
        return max_len

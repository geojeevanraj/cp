#lc problem link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_num = float('-inf')
        vowel_count = 0
        vowels = "aeiouAEIOU"
        left = 0
        for right in range(len(s)):
            if s[right] in vowels:
                vowel_count += 1
            if right - left + 1 == k:
                max_num = max(max_num, vowel_count)
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
        return max_num
                

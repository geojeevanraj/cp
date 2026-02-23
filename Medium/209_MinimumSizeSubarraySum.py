#lc problem link: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        temp_len = 0
        left = 0
        _sum = 0
        for right in range(len(nums)):
            _sum += nums[right]
            while _sum >= target:
                min_len = min(min_len, right - left + 1)
                _sum -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len

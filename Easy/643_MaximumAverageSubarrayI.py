#lc problem link: https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[left]
                left += 1
        return max_sum/k

#Lc problem link :https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                curr_count = 0
            count = max(count, curr_count)
        return count

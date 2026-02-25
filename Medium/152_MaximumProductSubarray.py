#lc problem link: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            temp_max = prev_max
            temp_min = prev_min

            prev_max = max(
                nums[i],
                temp_max * nums[i],
                temp_min * nums[i]
            )

            prev_min = min(
                nums[i],
                temp_max * nums[i],
                temp_min * nums[i]
            )

            result = max(result,prev_max)
        return result

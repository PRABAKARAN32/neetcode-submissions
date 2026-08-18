class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_count = nums[0]
        count = 0

        for i in range(len(nums)):
            if count < 0:
                count = 0
            count += nums[i]
            max_count = max(max_count,count)

        return max_count

        
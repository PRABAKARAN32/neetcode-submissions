class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # if nums[0] <  nums[n-1]:
        #     return nums[0]
        
        r = n-1
        l = 0

        while l < r:
            mid = (l+r)//2
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]

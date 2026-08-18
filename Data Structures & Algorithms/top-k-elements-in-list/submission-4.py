class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        n = len(nums)

        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1

        bucket = [[] for i in range(n)]

        for num, freq in hash_map.items():
            bucket[freq-1].append(num)

        # print(bucket)
        
        r = n-1

        ans = []

        while r >= 0 and k > 0:
            if bucket[r]:
                for num in bucket[r]:
                    ans.append(num)
                    k -= 1
            r -= 1
        return ans



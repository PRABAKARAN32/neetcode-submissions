class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_arr = [0]*26
        l,r = 0,0

        max_count = 0

        max_freq = 0

        while r < len(s):
            hash_arr[ord(s[r]) - ord('A')] += 1

            max_freq = max(max_freq, hash_arr[ord(s[r]) - ord('A')])

            if (r-l+1) - max_freq > k:
                hash_arr[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_count = max(max_count, r-l+1)
            r += 1
        return max_count
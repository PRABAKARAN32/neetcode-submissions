class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(t),len(s)

        hash_arr = [0]*256

        for ch in t:
            hash_arr[ord(ch)] += 1
        
        l,r = 0,0
        count  = 0
        min_length = float('inf')
        sIndex = -1

        while r < n:

            if hash_arr[ord(s[r])] > 0:
                count += 1
            
            hash_arr[ord(s[r])] -= 1

            while (count == m):
                if min_length > (r-l+1):
                    min_length = (r-l+1)
                    sIndex = l
                hash_arr[ord(s[l])] += 1

                if hash_arr[ord(s[l])] > 0:
                    count -= 1
                l += 1
            r += 1

        return s[sIndex:sIndex+min_length] if sIndex != -1 else ""


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for words in strs:
            s += str(len(words)) + '#' + words
        
        return s

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # Starting index
            j += 1
            #s[j:j+length] the j+length is equal to index but defaulty the last one is exclusive it will be like (j+length-1). so it will work
            result.append(s[j:j+length])
            i = j+length
        return result
        

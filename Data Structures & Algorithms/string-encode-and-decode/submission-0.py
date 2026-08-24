class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            length = len(s)
            encoded.extend([str(length), "#", s])
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = length + start
            result.append(s[start:end])
            i = end
            

        return result



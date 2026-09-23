import itertools

class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        NUMS_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
        }
        if not digits or len(digits) > 4 or "1" in digits or "0" in digits:
            return []
        
        if len(digits) == 1:
            return list(NUMS_MAP[digits])
        
        letters = []
        for digit in digits:
            if not digit.isdigit():
                return []
            letters.append(NUMS_MAP[digit])
        
        output = []
        cartesian_product = itertools.product(*letters)

        for v in cartesian_product:
            output.append("".join(v))
        return output

            


        
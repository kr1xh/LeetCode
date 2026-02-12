class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        result = [""]
        for digit in digits:
            temp = []
            for prefix in result:
                for char in phone[digit]:
                    temp.append(prefix + char)
            result = temp
        return result
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter_dict = {
                        '2': ['a','b','c'],
                        '3': ['d','e','f'],
                        '4': ['g','h','i'],
                        '5': ['j','k','l'],
                        '6': ['m','n','o'],
                        '7': ['p','q','r', 's'],
                        '8': ['t','u','v'],
                        '9': ['w','x','y','z']
                      }

        ans = letter_dict[digits[0]]
        
        for i in range(1, len(digits)):
            temp_ans = []
            for combo in ans:
                for letter in letter_dict[digits[i]]:
                    temp_ans.append(combo + letter)
            ans = temp_ans
            
        return ans
            